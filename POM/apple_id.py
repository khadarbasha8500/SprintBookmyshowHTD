import re
import time
from Library.read_excel import ReadExcel
from Library.config import Config

class SigninWithApple:
    read_xl = ReadExcel()
    apple_locators = read_xl.read_locaters(Config.APPLE_LOCATORS)

    def __init__(self, driver):
        self.driver = driver

    def click_on_signIn(self):
        locator = self.apple_locators["click_on_signIn"]
        self.driver.find_element(*locator).click()
        self.driver.implicitly_wait(30)

    def click_continueWith_apple(self):
        locator = self.apple_locators["click_continueWith_appleAccount"]
        self.driver.find_element(*locator).click()

    def enter_apple_id(self,apple_Id):
        condition = r'\w+@icloud\.com'
        res = re.findall(condition, apple_Id)
        assert res != [], "invalid emailid"

        locator = self.apple_locators["enter_apple_id"]
        self.driver.find_element(*locator).send_keys(apple_Id)
        self.driver.implicitly_wait(30)


    def click_next_icon(self):
        locator = self.apple_locators["click_next_icon"]
        self.driver.find_element(*locator).click()
        time.sleep(1)

    def enter_apple_password(self,password):
        locator = self.apple_locators["enter_apple_password"]
        self.driver.find_element(*locator).send_keys(password)
        self.driver.implicitly_wait(30)
        time.sleep(2)


    def click_on_next(self):
        locator = self.apple_locators["click_on_next"]
        self.driver.find_element(*locator).click()



