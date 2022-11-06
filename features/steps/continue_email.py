# import re
# import time
# from behave import *
# from selenium import webdriver
#
# @given(u'user able to launch browser')
# def step_impl(context):
#     context.driver = webdriver.Chrome(executable_path=r"C:\Users\khada\PycharmProjects\BookMyShowSprint2\drivers\chromedriver.exe")
#     context.driver.get("https://in.bookmyshow.com/explore/home/bengaluru")
#
#
# @when(u'user able to click on signin button')
# def step_impl(context):
#     context.driver.find_element("xpath", "//div[text()='Sign in']").click()
#     time.sleep(5)
#
#
# @then(u'user able to click on the continue with email')
# def step_impl(context):
#     context.driver.find_element('xpath',"//div[text()='Continue with Email']").click()
#     context.driver.implicitly_wait(10)
#
#
# @then(u'user enter the valid "{email}"')
# def step_impl(context,email):
#     e_mail = r"\w+@email\.com"
#     res = re.findall(e_mail, email)
#     assert res, "invalid mail"
#     context.driver.find_element('xpath', "//input[@id='emailId']").send_keys(email)
#     time.sleep(1)
#
#
# @then(u'user able to the click on continue button')
# def step_impl(context):
#     context.driver.find_element('xpath','//button[text()="Continue"]').click()
#     time.sleep(1)
#
