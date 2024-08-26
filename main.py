"""
pyCrawler V1.002
  - Started using undetected_chromedriver


  TODO:
    - Add phone number verification
    - Add support for saving account info

"""

import functions
import undetected_chromedriver as uc
import time


task_count = 1
password = "Quintin1942$"
proxy = "23.146.144.102:12321"  # this proxy returns a different ip for each task during initiation


drivers = []


def initiate(proxy):
    options = uc.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument(f"--proxy-server={proxy}")

    driver = uc.Chrome(options=options, use_subprocess=False)
    print("driver initiated...")
    return driver


def main():
    for i in range(task_count):
        driver = initiate(proxy)
        drivers.append(driver)

    for driver in drivers:
        functions.navigate_to_signup(driver)

    for driver in drivers:
        functions.fill_out_signup(driver, password)

    time.sleep(3000)

    for driver in drivers:
        driver.quit()


if __name__ == "__main__":
    main()
