import datetime
import pytest
from Library.read_excel import ReadExcel
from Library.config import Config
from POM.email import SigninWithEmail


class Test_ContinueWithEmail:

    read_xl = ReadExcel()
    data = read_xl.read_test_data(Config.EMAIL_DATA)

    @pytest.mark.parametrize("email",data)
    def test_email(self,email,init_driver):
        driver = init_driver
        # cwe = SigninWithEmail(driver)

        try:
            cwe = SigninWithEmail(init_driver)
            cwe.click_on_signIn()
            cwe.click_continueWith_Email()
            cwe.click_enter_email(email)
            cwe.click_enterButton()

        except BaseException as err_msg:
            td = datetime.datetime.now()
            name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
            driver.save_screenshot(Config.SCREENSHOT_PATH + name)
            raise err_msg
