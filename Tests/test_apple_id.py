import datetime
import pytest
from Library.read_excel import ReadExcel
from Library.config import Config
from POM.apple_id import SigninWithApple

class Test_ContinueWithApple:
    read_xl = ReadExcel()
    data = read_xl.read_test_data(Config.APPLE_DATA)

    @pytest.mark.parametrize("apple_Id,password",data)
    def test_appleid(self,init_driver,apple_Id,password):
        driver = init_driver
        cwa = SigninWithApple(driver)

        try:
            cwa = SigninWithApple(init_driver)
            cwa.click_on_signIn()
            cwa.click_continueWith_apple()
            cwa.enter_apple_id(apple_Id)
            cwa.click_next_icon()
            cwa.enter_apple_password(password)
            cwa.click_on_next()

        except BaseException as err_msg:
            td = datetime.datetime.now()
            name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
            driver.save_screenshot(Config.SCREENSHOT_PATH + name)
            raise err_msg