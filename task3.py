from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start browser
driver = webdriver.Chrome()
driver.maximize_window()

try:
    print("Opening website...")
    driver.get("https://www.saucedemo.com/")

    # Test 1: Check website loads
    if "saucedemo" in driver.current_url:
        print("Test 1 Passed: Website loaded successfully")
    else:
        print("Test 1 Failed")

    # Test 2: Check title
    if driver.title == "Swag Labs":
        print("Test 2 Passed: Title is correct")
    else:
        print("Test 2 Failed")

    # Test 3: Check logo text
    logo = driver.find_element(By.CLASS_NAME, "login_logo")
    if logo.text == "Swag Labs":
        print("Test 3 Passed: Logo text is correct")
    else:
        print("Test 3 Failed")

    time.sleep(3)

finally:
    driver.quit()
    print("Browser closed.")
