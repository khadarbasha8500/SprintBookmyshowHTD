import datetime
import pytest
from POM.gmail import SigninWithGmail
from Library.read_excel import ReadExcel
from Library.config import Config


class Test_ContinueWithGmail:
    read_xl = ReadExcel()
    data = read_xl.read_test_data(Config.GMAIL_DATA)

    @pytest.mark.parametrize("gmail", data)
    def test_gmail_cases(self, gmail, init_driver):
        driver = init_driver

        try:
            cwg = SigninWithGmail(init_driver)
            cwg.click_on_signIn()
            cwg.click_continueWith_Gmail()
            cwg.click_enter_Gmail(gmail)
            cwg.click_signIn_button()

        except BaseException as err_msg:
            td = datetime.datetime.now()
            name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
            driver.save_screenshot(Config.SCREENSHOT_PATH+ name)
            raise err_msg
