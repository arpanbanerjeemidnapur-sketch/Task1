import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 🔐 Replace with your real BrowserStack credentials
USERNAME = "YOUR_BROWSERSTACK_USERNAME"
ACCESS_KEY = "YOUR_BROWSERSTACK_ACCESS_KEY"

BROWSERSTACK_URL = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"


class SwagLabsTest(unittest.TestCase):

    def setUp(self):

        # 👉 Change browser here if needed
        self.browser = "Chrome"   # Chrome / Firefox / Edge / Safari

        # Create correct browser options
        if self.browser == "Chrome":
            options = webdriver.ChromeOptions()
            os_name = "Windows"
            os_version = "11"

        elif self.browser == "Firefox":
            options = webdriver.FirefoxOptions()
            os_name = "Windows"
            os_version = "11"

        elif self.browser == "Edge":
            options = webdriver.EdgeOptions()
            os_name = "Windows"
            os_version = "11"

        elif self.browser == "Safari":
            options = webdriver.SafariOptions()
            os_name = "OS X"
            os_version = "Ventura"

        else:
            raise Exception("Unsupported Browser")

        # BrowserStack capabilities
        options.set_capability("browserName", self.browser)
        options.set_capability("browserVersion", "latest")

        options.set_capability("bstack:options", {
            "os": os_name,
            "osVersion": os_version,
            "projectName": "Swag Labs Cross Browser Testing",
            "buildName": "Build 1",
            "sessionName": f"{self.browser} - Login & Add To Cart Test"
        })

        # Start Remote WebDriver
        self.driver = webdriver.Remote(
            command_executor=BROWSERSTACK_URL,
            options=options
        )

        self.wait = WebDriverWait(self.driver, 20)

    def test_login_and_add_to_cart(self):
        driver = self.driver

        # Open website
        driver.get("https://www.saucedemo.com/")

        # Login
        self.wait.until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys("standard_user")

        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Wait for inventory page
        self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
        )

        # Add to cart
        add_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        add_button.click()

        # Verify cart badge
        cart_badge = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
        )

        self.assertEqual(cart_badge.text, "1")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
