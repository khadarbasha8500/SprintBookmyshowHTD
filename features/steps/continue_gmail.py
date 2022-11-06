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
# @when(u'user able click on sign in button')
# def step_impl(context):
#     context.driver.find_element("xpath","//div[text()='Sign in']").click()
#     time.sleep(5)
#
#
# @then(u'user able to click on the continue with the google')
# def step_impl(context):
#     context.driver.find_element('xpath','//div[text()="Continue with Google"]').click()
#     context.driver.implicitly_wait(5)
#     time.sleep(5)
#
#
# @then(u'user enter the valid gmail"{gmail}"')
# def step_impl(context,gmail):
#     handles = context.driver.window_handles
#     context.driver.switch_to.window(handles[1])
#     g_mail = r"\w+@gmail\.com"
#     res = re.findall(g_mail, gmail)
#     assert res, "invalid mail"
#     context.driver.find_element('xpath','//input[@id="identifierId"]').send_keys(gmail)
#     time.sleep(1)
#
#
# @then(u'user able to click on next button')
# def step_impl(context):
#     context.driver.find_element('xpath','//span[text()="Next"]').click()
#     time.sleep(5)
#     context.driver.close()
#
#
