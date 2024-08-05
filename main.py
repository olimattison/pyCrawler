"""
pyCrawler V1.xx

Features:
  - None!

Working on:
  - Gmail account generation
"""
from selenium import webdriver
import zipfile

num = 3
url = "https://google.com"
drivers = []


def newProxy():
    with open('proxies.txt', 'r') as a:
        proxyList_unstripped = a.readlines()
    # proxyList = [prox.rstrip('\n') for prox in proxyList_unstripped]
    # removed_last_line = proxyList[:-1]
    proxyList = proxyList_unstripped
    removed_last_line = proxyList[:-1]
    print(removed_last_line)

    try:
        myProxy = proxyList[-1]
    except IndexError as error:
        print(f"No proxies in proxies file! Error: {error}")
        exit()


    credentials = str(myProxy).split(':')
    PROXY_HOST = credentials[0]
    PROXY_PORT = credentials[1]
    PROXY_USER = credentials[2]
    PROXY_PASS = credentials[3]

    print(f"proxy: {myProxy}, {credentials}")
    with open('usedproxies.txt', 'a') as b:
        b.write(str(myProxy))

    with open('proxies.txt', 'w') as c:
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
    options.add_argument("start-maximized")
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


def run_tasks():
    for i in range(num):
        print(f"iteration {i}")
        ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        driver = initiate(True, ua)
        drivers.append(driver)

    for driver in drivers:
        driver.get(url)


    for driver in drivers:
        driver.quit()