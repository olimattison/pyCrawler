"""
pyCrawler V1.0
  - Gmail is now requiring QR code verification from a mobile device. No longer maintaining.
"""

import gmail_functions as gmail_functions
import undetected_chromedriver as uc
import time


task_count = 1
password = "Password123"
proxy = "x.x.x.x:xxxx"  # this proxy returns a different ip for each task during initiation


drivers = []


def initiate(proxy):    
    options = uc.ChromeOptions()
    # options.add_argument("--headless")
    options.add_argument(f"--proxy-server={proxy}")

    driver = uc.Chrome(options=options, use_subprocess=False)
    print("driver initiated...")
    return driver


def main():
    print("Welcome to PyCrawler!")
    for i in range(task_count):
        driver = initiate(proxy)
        drivers.append(driver)

    for driver in drivers:
        gmail_functions.navigate_to_signup(driver)

    for driver in drivers:
        gmail_functions.fill_out_signup(driver, password)

    for driver in drivers:
        driver.quit()


if __name__ == "__main__":
    main()
