from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import HtmlTestRunner
import smtplib
import glob
import os
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

class LoginTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("https://www.myvidya.org/")

    def setUp(self):
        self.driver.get("https://www.myvidya.org/")

    def test_title(self):
        t1 = time.time()
        assert 'MyVidya' == self.driver.title
        print("Time Taken: ",time.time()-t1)

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

    # def test_enroll_course(self):


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == "__main__":
    unittest.main(exit=False, testRunner=HtmlTestRunner.HTMLTestRunner(report_name="MyVidya_report", output='/home/harsh/PycharmProjects/myvidya_selenium_testing/reports'))

    list_of_files = glob.glob('/home/harsh/PycharmProjects/myvidya_selenium_testing/reports/*')
    latest_file = max(list_of_files, key=os.path.getctime)

    fromaddr = "manmeetkundra7959@gmail.com"
    toaddr = ["varun.mishra@traxof.com","manis.kumar@gmail.com"]

    for addr in toaddr:
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = addr
        msg['Subject'] = "MyVidya Test Report"
        body = "This is test Report of myvidya.org"
        msg.attach(MIMEText(body, 'plain'))
        filename = latest_file
        attachment = open(filename,"rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, "Manmeet@321")
        text = msg.as_string()
        s.sendmail(fromaddr, addr, text)
        s.quit()
