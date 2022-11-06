import time

from Library.read_excel import ReadExcel
from Library.config import Config

class SigninWithPhoneNumber:
    read_excel = ReadExcel()
    phone_locators = read_excel.read_locaters(Config.PHONE_LOCATORS)

    def __init__(self,driver):
        self.driver = driver

    def click_on_signIn(self):
        locator = self.phone_locators["click_on_signIn"]
        self.driver.find_element(*locator).click()

    def click_continueWith_phoneNumber(self,phone_number):
        if isinstance(phone_number,(float,int,str)):
            phone_number = str(int(phone_number))
        assert len(phone_number) == 10 ,"enter the valid 10 digits phone number "
        locator = self.phone_locators["click_continueWith_phoneNumber"]
        self.driver.find_element(*locator).send_keys(phone_number)

    def click_continue_button(self):
        locator = self.phone_locators["click_continue_button"]
        time.sleep(5)