from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import json
import random
import time

delay = random.randint(5, 25) / 10  # random delay
sms_number = "123-456-7890"

first_names = ["Lebron", "Quan", "Sam", "Carl", "Scott", "Loretta", "Stone", "Matt", "Matthew", "Taylor", "Lucy"]
last_names = ["James", "Smith", "Brown", "Johnson", "Stevenson", "Hernandez", "Garcia", "Martin", "Jones", "Moore"]
generated_accounts = {}


def create_account_info():
    x = 0
    first_name = first_names[random.randint(0, len(first_names) - 1)]
    last_name = last_names[random.randint(0, len(last_names) - 1)]
    username = f"{first_name}{last_name}{random.randint(100, 99999)}"

    return first_name, last_name, username


def get_verification_code():
    pass


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

    time.sleep(delay)

    try:  # phone verification input
        what = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(
                (By.ID, "phoneNumberId"))
        )
        element = driver.find_element(By.ID, "phoneNumberId")
        print("found phone verification input...")
        element.send_keys(sms_number)
    except TimeoutException:
        print("(fill_out_signup) - error could not find phone verification input")

    time.sleep(delay)

    try:  # next btn(4)
        element = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[3]/div/div/div/div/button')
        print("found next(4) button...")
        element.click()
    except BaseException as error:
        print(f"(fill_out_signup) - error clicking next(4) button: {error}")

    time.sleep(1)

    try:  # phone number used too many times  HANDLE THIS BETTER
        what = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="yDmH0d"]/c-wiz/div/div[2]/div/div/div[1]/form/span/section/div/div/div[2]/div/div[2]/div[2]/div'))
        )
        print("(fill_out_signup) - error phone number used too many times")
    except TimeoutException:
        print("phone number accepted")

    # Update account information in accounts.json
    with open('accounts.json', 'r') as file:
        data = json.load(file)

    account_information = {
        "first_name": first_name,
        "last_name": last_name,
        "username": username,
        "verified_with": sms_number}

    data.append(account_information)

    with open('accounts.json', 'w') as file:
        json.dump(data, file, indent=4)

    print(f"{username} successfully created!")

























