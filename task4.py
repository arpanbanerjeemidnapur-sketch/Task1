import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#  Replace with your actual BrowserStack credentials
USERNAME = "YOUR_BROWSERSTACK_USERNAME"
ACCESS_KEY = "YOUR_BROWSERSTACK_ACCESS_KEY"

BROWSERSTACK_URL = f"https://{USERNAME}:{ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub"


class SwagLabsTest(unittest.TestCase):

    def setUp(self):

        #  Change browser here: chrome / firefox / edge / safari
        self.browser = "chrome"

        bstack_options = {
            "os": "Windows",
            "osVersion": "11",
            "projectName": "Swag Labs Cross Browser Testing",
            "buildName": "Build 1",
            "sessionName": f"{self.browser} - Full Flow Test"
        }

        # Select browser options
        if self.browser == "chrome":
            options = webdriver.ChromeOptions()

        elif self.browser == "firefox":
            options = webdriver.FirefoxOptions()

        elif self.browser == "edge":
            options = webdriver.EdgeOptions()

        elif self.browser == "safari":
            options = webdriver.SafariOptions()
            bstack_options["os"] = "OS X"
            bstack_options["osVersion"] = "Ventura"

        else:
            raise Exception("Unsupported Browser")

        # Set W3C capabilities
        options.set_capability("browserName", self.browser)
        options.set_capability("browserVersion", "latest")
        options.set_capability("bstack:options", bstack_options)

        # Start Remote Driver
        self.driver = webdriver.Remote(
            command_executor=BROWSERSTACK_URL,
            options=options
        )

        self.wait = WebDriverWait(self.driver, 20)

    def test_login_add_cart_continue(self):
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

        # Add item to cart
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        ).click()

        # Open cart
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Wait for cart page
        self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "cart_list"))
        )

        # Click Continue Shopping
        self.wait.until(
            EC.element_to_be_clickable((By.ID, "continue-shopping"))
        ).click()

        # Verify back to inventory page
        self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
        )

        self.assertIn("inventory", driver.current_url)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
