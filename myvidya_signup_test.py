from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://www.myvidya.org/")

name = driver.find_element(By.ID, "fullName")
email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "newPassword")
cnfrm_pass = driver.find_element(By.ID, "newPasswordConfirm")


name.send_keys("testing")
email.send_keys("testing@gmail.com")
password.send_keys("testing")
cnfrm_pass.send_keys("testing")

time.sleep(5)

signup = driver.find_element(By.XPATH, '//button[text()="Get started"]')
signup.click()

time.sleep(10)

driver.close()