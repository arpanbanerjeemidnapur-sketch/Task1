from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

try:
    driver.get("https://www.saucedemo.com/")

    if "saucedemo" in driver.current_url:
        print("Website loaded successfully")

    if driver.title == "Swag Labs":
        print("Title is correct")

    logo = driver.find_element(By.CLASS_NAME, "login_logo")
    if logo.text == "Swag Labs":
        print("Logo text is correct")

    time.sleep(3)

finally:
    driver.quit()
