import datetime
import pytest
from Library.config import Config
from Library.read_excel import ReadExcel
from POM.phone_num import SigninWithPhoneNumber

class Test_continueWithPhonenumber:

    read_xl = ReadExcel()
    data = read_xl.read_test_data(Config.PHONE_DATA)

    @pytest.mark.parametrize("phone_number",data)
    def test_phonenumber(self,phone_number,init_driver):
        driver = init_driver
        cwp = SigninWithPhoneNumber(driver)

        try:
            cwp = SigninWithPhoneNumber(init_driver)
            cwp.click_on_signIn()
            cwp.click_continueWith_phoneNumber(phone_number)
            cwp.click_continue_button()

        except BaseException as err_msg:
            td = datetime.datetime.now()
            name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
            driver.save_screenshot(Config.SCREENSHOT_PATH+name)
            raise err_msg

