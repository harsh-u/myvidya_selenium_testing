from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://www.myvidya.org/")

username = driver.find_element(By.ID, "userid")
password = driver.find_element(By.ID, "password")

username.send_keys("rajharsh662@gmail.com")
password.send_keys("harsh")

time.sleep(5)


login = driver.find_element(By.XPATH, '//button[text()="LOG IN"]')
login.click()

time.sleep(10)

driver.close()
