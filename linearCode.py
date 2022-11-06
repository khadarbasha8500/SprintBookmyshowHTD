import time
from selenium import webdriver

path = r"C:\Users\khada\PycharmProjects\BookMyShowSprint2\drivers\chromedriver.exe"
driver = webdriver.Chrome(executable_path=path)

url = "https://in.bookmyshow.com/explore/home/bengaluru"
driver.get(url)

driver.find_element("xpath", "//div[text()='Sign in']").click()  #sign in
time.sleep(3)
# driver.implicitly_wait(5)

"""continue with G-mail"""

# driver.find_element('xpath','//div[text()="Continue with Google"]').click()
# driver.implicitly_wait(5)
# time.sleep(5)
# handles = driver.window_handles
# # print(handles)
# driver.switch_to.window(handles[1])
#
# driver.find_element('xpath','//input[@id="identifierId"]').send_keys("abdulkhadar8161@gmail.com")
# time.sleep(1)
# driver.find_element('xpath','//span[text()="Next"]').click()
# time.sleep(5)



"""continue with E-mail"""
#
# driver.find_element('xpath',"//div[text()='Continue with Email']").click()
# driver.find_element('xpath',"//input[@id='emailId']").send_keys("abdulkhadar8161@email.com")
# driver.implicitly_wait(3)
# driver.find_element('xpath','//button[text()="Continue"]').click()
# time.sleep(3)
# handles = driver.window_handles
# print(handles)


'''continue with apple account'''


# driver.find_element('xpath','//div[text()="Continue with Apple"]').click()
#
# driver.find_element('id',"account_name_text_field").send_keys("michael_cavanna@icloud.com")
# driver.find_element('id',"sign-in").click()
# time.sleep(1)
# driver.find_element("xpath","//input[@class='form-textbox form-textbox-text ']").send_keys("abc123")
# time.sleep(1)
# driver.find_element('xpath','//button[@id="sign-in"]').click()


'''continue with phone number'''

# driver.find_element('id','mobileNo').send_keys('7981613572')
# #
# '''continue button'''
# driver.find_element('xpath',"//button[text()='Continue']/..").click()


# print(driver.window_handles)
time.sleep(5)
driver.close()









