from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import HtmlTestRunner
# import smtplib


class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://www.myvidya.org/")

    def test_login(self):
        t1 = time.time()
        username = self.driver.find_element(By.ID, "userid")
        password = self.driver.find_element(By.ID, "password")

        username.send_keys("rajharsh662@gmail.com")
        password.send_keys("harsh")
        t2 = time.time()

        print("Username and password entering time: ", t2 - t1)
        time.sleep(5)

        login = self.driver.find_element(By.XPATH, '//button[text()="LOG IN"]')
        login.click()

        t3 = time.time() - 5
        print("Time taken in Login: ", t3 - t2)
        time.sleep(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/harsh/PycharmProjects/myvidya_selenium_testing/reports'))



