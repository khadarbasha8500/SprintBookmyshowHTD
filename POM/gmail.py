import re
import time
from Library.read_excel import ReadExcel
from Library.config import Config


class SigninWithGmail:
    read_xl = ReadExcel()
    gmail_locators = read_xl.read_locaters(Config.GMAIL_LOCATORS)

    def __init__(self, driver):
        self.driver = driver

    def click_on_signIn(self):
        locator = self.gmail_locators["click_on_signIn"]
        self.driver.find_element(*locator).click()
        time.sleep(5)
        # time.sleep(3)


    def click_continueWith_Gmail(self):
        locator = self.gmail_locators["click_continueWith_Gmail"]
        print(locator)
        self.driver.execute_script("arguments[0].click()",self.driver.find_element(*locator))
        # self.driver.find_element(*locator).click()
        time.sleep(10)


    def click_enter_Gmail(self, gmail):
        handles = self.driver.window_handles
        print(handles)
        time.sleep(10)
        self.driver.switch_to.window(handles[1])
        time.sleep(1)
        condition = r"\w+@gmail\.com"
        res = re.findall(condition,gmail)
        assert res != [],"invalid g-mail"
        locator = self.gmail_locators["click_enter_Gmail"]
        self.driver.find_element(*locator).send_keys(gmail)

    def click_signIn_button(self):
        self.driver.implicitly_wait(5)
        locator = self.gmail_locators["click_signIn_button"]
        self.driver.find_element(*locator).click()



