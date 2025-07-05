import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time
import os

class LoginTestSuite(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = Options()
        options.use_chromium = True
        cls.driver = webdriver.Edge(options=options)
        cls.driver.maximize_window()

    def setUp(self):
        path = os.path.abspath("login.html")
        self.driver.get(f"file:///{path}")
        time.sleep(1)

    def test_manual_login_and_redirect(self):
        input("Enter username and password in the browser, click Login, then press ENTER here to continue...")

        time.sleep(3)
        current_url = self.driver.current_url.lower()

        if "flipkart.com" in current_url:
            self.assertIn("flipkart.com", current_url)
        else:
            self.fail("Did not redirect to Flipkart. Login might have failed or was not submitted.")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()