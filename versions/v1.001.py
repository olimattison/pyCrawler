"""
pyCrawler V1.001
  - uses selenium to open whatismyip.com and return the current ip.
  - includes handling for authenticated proxies

  TODO:
   - Needs better anti-bot evasion, starting new script using undetected_chromedriver!

"""

from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import ua_generator
import zipfile
import json
import random
import time


num = 1  # number of tasks
url = "https://whatismyip.com"
proxies = ["geo.iproyal.com:12321:XPhoqPHAAYolwiZk:Jck0DHaNBQlkCrni"]
use_proxy_file = False  # not working yet

resolutions_list = ["1920,1080", "1280,720", "1850,1080"]
drivers = []


def newProxy():
    if use_proxy_file:
        with open('proxies.json', 'r') as a:
            proxy_list = json.load(a)
    else:
        proxy_list = proxies

    try:
        myProxy = proxy_list[-1]
        print(f"MYPROXY ==== {myProxy}")
    except IndexError as error:
        print(f"No proxies in proxies file! Error: {error}")
        exit()


    credentials = str(myProxy).split(':')
    PROXY_HOST = credentials[0]
    PROXY_PORT = credentials[1]
    PROXY_USER = credentials[2]
    PROXY_PASS = credentials[3]

    if use_proxy_file:
        with open('usedproxies.json', 'a') as b:
            b.writelines(myProxy)

        removed_last_line = proxy_list[:-1]
        with open('proxies.json', 'w') as c:
            c.writelines(removed_last_line)

    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome Proxy",
        "permissions": [
            "proxy",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequest",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"22.0.0"
    }
    """

    background_js = """
    var config = {
            mode: "fixed_servers",
            rules: {
            singleProxy: {
                scheme: "http",
                host: "%s",
                port: parseInt(%s)
            },
            bypassList: ["localhost"]
            }
        };
    chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});
    function callbackFn(details) {
        return {
            authCredentials: {
                username: "%s",
                password: "%s"
            }
        };
    }
    chrome.webRequest.onAuthRequired.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking']
    );
    """ % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)

    return manifest_json, background_js


def initiate(use_proxy, user_agent):
    options = webdriver.ChromeOptions()
    # options.add_argument("start-maximized")
    # options.add_argument("--headless")  # NOT SUPPORTED YET
    random_resolution = resolutions_list[random.randint(0, len(resolutions_list)) - 1]
    print(f"random_resolution: {random_resolution}")
    options.add_argument(f"--window-size={random_resolution}")  # RAND RES

    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    if use_proxy:
        pluginfile = 'proxy_auth_plugin.zip'
        manifest_json, background_js = newProxy()
        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json", manifest_json)
            zp.writestr("background.js", background_js)

        options.add_extension(pluginfile)

    if user_agent:
        options.add_argument('--user-agent=%s' % user_agent)

    driver = webdriver.Chrome(options=options)
    return driver


def getIP(driver):
    try:
        what = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'the-ipv4'))  # Replace with the actual element locator
        )
        print("Element is ready to interact with!")
        element = driver.find_element(By.CLASS_NAME, 'the-ipv4')
        return element
    except TimeoutException:
        print("Loading took too much time!")


def run_tasks():
    for i in range(num):
        print(f"iteration {i}")
        ua = ua_generator.generate()
        print(f"user agent  =====  {ua}")
        driver = initiate(True, ua)
        drivers.append(driver)

    for driver in drivers:
        driver.get(url)

    for driver in drivers:
        ipCheck = getIP(driver)
        if ipCheck:
            print(ipCheck)
        else:
            print("Unable to get ip")



    for driver in drivers:
        driver.quit()


if __name__ == '__main__':
    run_tasks()
