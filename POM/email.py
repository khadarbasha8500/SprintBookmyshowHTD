import re
import time

from Library.read_excel import ReadExcel
from Library.config import Config


class SigninWithEmail:
    read_xl = ReadExcel()
    email_locators = read_xl.read_locaters(Config.EMAIL_LOCATORS)

    def __init__(self, driver):
        self.driver = driver

    def click_on_signIn(self):
        locator = self.email_locators["click_on_signIn"]
        self.driver.find_element(*locator).click()

    def click_continueWith_Email(self):
        locator = self.email_locators["click_continueWith_Email"]
        self.driver.find_element(*locator).click()

    def click_enter_email(self,email):
        e_mail = r'\w+@email\.com'
        res = re.findall(e_mail, email)
        assert res != [], "invalid emailid"

        locator = self.email_locators["click_enter_email"]
        self.driver.find_element(*locator).send_keys(email)
        time.sleep(1)

    def click_enterButton(self):
        locator = self.email_locators["click_continueButton"]
        self.driver.find_element(*locator).click()
