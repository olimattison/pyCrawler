from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import random
import time

first_names = ["Lebron", "Quan", "Sam", "Carl", "Scott", "Loretta", "Stone", "Matt", "Matthew", "Taylor", "Lucy"]
last_names = ["James", "Smith", "Brown", "Johnson", "Stevenson", "Hernandez", "Garcia", "Martin", "Jones", "Moore"]
delay = random.randint(5, 35) / 10


def create_account_info():
    first_name = first_names[random.randint(0, len(first_names) - 1)]
    last_name = last_names[random.randint(0, len(last_names) - 1)]
    username = f"{first_name}{last_name}{random.randint(100, 99999)}"
    return first_name, last_name, username


def getIP(driver):  # https://whatismyip.com
    try:
        what = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'the-ipv4'))
        )
        element = driver.find_element(By.CLASS_NAME, 'the-ipv4')
        ip_addr = element.text
        print(f"successfully grabbed ip ({ip_addr})...")
        return ip_addr
    except TimeoutException:
        print(f"(getIP) - Could not get ip address!")


def navigate_to_signup(driver):
    driver.get("https://gmail.com")

    try:  # create acc button
        what = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[2]/div/div/div[1]/div/button'))
        )
        element = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[2]/div/div/div[1]/div/button')
        print("found create account button...")
        element.click()
    except TimeoutException:
        print(f"(navigate_to_signup) - Could not find create acc button!")

    try:  # personal use button
        what = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[2]/div/div/div[2]/div/ul/li[1]"))
        )
        element = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div[2]/div/div/div[2]/div/ul/li[1]")
        print("found personal use button, clicking...")
        element.click()
    except TimeoutException:
        print(f"(navigate_to_signup) - Could not find personal use acc button![2]")


def fill_out_signup(driver, password):
    first_name, last_name, username = create_account_info()

    try:  # first name element
        what = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.ID, 'firstName'))
        )
        element = driver.find_element(By.ID, "firstName")
        print("found firstName field...")
        element.send_keys(first_name)
    except TimeoutException:
        print("(fill_out_signup) - error could not find first name element")

    time.sleep(delay)

    try:  # last name element
        element = driver.find_element(By.ID, "lastName")
        print("found lastName field...")
        element.send_keys(last_name)
    except BaseException as error:
        print(f"(fill_out_signup) - error could not find last name element: {error}")

    time.sleep(delay)

    try:  # continue btn
        element = driver.find_element(By.XPATH, '//*[@id="collectNameNext"]/div/button')
        print("found continue btn...")
        element.click()
    except BaseException as error:
        print(f"(fill_out_signup) - error clicking continue btn: {error}")

    time.sleep(3)
    try:  # month dropdown selection
        what = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.ID, 'month'))
        )
        element = driver.find_element(By.ID, "month")
        print("found month selection...")
        element.click()
        select = Select(element)
        select.select_by_value(str(random.randint(1, 12)))
    except TimeoutException:
        print("(fill_out_signup) - error could not find month selection element")

    time.sleep(delay)

    try:  # day input
        element = driver.find_element(By.ID, 'day')
        print("found day input...")
        element.send_keys(random.randint(1, 28))
    except BaseException as error:
        print(f"(fill_out_signup) - error inputting birth day: {error}")

    try:  # year input
        element = driver.find_element(By.ID, 'year')
        print("found year input...")
        element.send_keys(random.randint(1971, 2005))
    except BaseException as error:
        print(f"(fill_out_signup) - error inputting birth year: {error}")

    time.sleep(delay)

    try:  # gender dropdown selection
        element = driver.find_element(By.ID, 'gender')
        print("found year input...")
        select = Select(element)
        select.select_by_value(str(random.randint(1, 2)))
    except BaseException as error:
        print(f"(fill_out_signup) - error selecting gender: {error}")

    time.sleep(delay)

    try:  # next btn
        element = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div/div/div/button')
        print("found next button...")
        element.click()
    except BaseException as error:
        print(f"(fill_out_signup) - error clicking next button: {error}")

    time.sleep(delay)

    try:  # username input
        what = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section/div/div/div/div[1]/div/div[1]/div/div[1]/input'))
        )
        element = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section/div/div/div/div[1]/div/div[1]/div/div[1]/input")
        print("found username input...")
        element.send_keys(username)
    except TimeoutException:
        print("(fill_out_signup) - error could not find username input")

    time.sleep(delay)

    try:  # next(2) btn
        element = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div/div/div/button')
        print("found next(2) button...")
        element.click()
    except BaseException as error:
        print(f"(fill_out_signup) - error clicking next(2) button: {error}")

    time.sleep(delay)
    try:  # password input
        what = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[1]/input"))
        )
        element = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section/div/div/div/div[1]/div/div/div[1]/div/div[1]/div/div[1]/input")
        print("found password input...")
        element.send_keys(password)
    except TimeoutException:
        print("(fill_out_signup) - error could not find password input")

    time.sleep(delay)
    
    try:  # confirm password input
        element = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[2]/div/div/div/form/span/section/div/div/div/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
        print("found confirm password input...")
        element.send_keys(password)
    except BaseException as error:
        print(f"(fill_out_signup) - error inputting confirm password: {error}")

    time.sleep(delay)

    try:  # next btn(3)
        element = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/c-wiz/div/div[3]/div/div/div/div/button")
        print("found next(3) button...")
        element.click()
    except BaseException as error:
        print(f"(fill_out_signup) - error clicking next(3) button: {error}")


















