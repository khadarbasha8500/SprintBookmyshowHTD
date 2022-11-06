# import re
# import time
# from behave import *
# from selenium import webdriver
#
#
# @given(u'user able to launch browser')
# def step_impl(context):
#     path = r"C:\Users\khada\PycharmProjects\BookMyShowSprint2\drivers\chromedriver.exe"
#     context.driver = webdriver.Chrome(executable_path=path)
#
#     url = "https://in.bookmyshow.com/explore/home/bengaluru"
#     context.driver.get(url)
#
#
# @when(u'user able to click on signin button')
# def step_impl(context):
#     context.driver.find_element("xpath", "//div[text()='Sign in']").click()
#     time.sleep(3)
#
#
# @then(u'user able to click on the continue with apple')
# def step_impl(context):
#     context.driver.find_element('xpath','//div[text()="Continue with Apple"]').click()
#     time.sleep(1)
#
#
# @when(u'user enter the  apple id "{apple_id}"')
# def step_impl(context,apple_id):
#     cloud = r"\w+@icloud\.com"
#     res = re.findall(cloud, apple_id)
#     assert res, "invalid apple id "
#     context.driver.find_element('id',"account_name_text_field").send_keys(apple_id)
#
#
# @when(u'user click on the next icon')
# def step_impl(context):
#     context.driver.find_element('id',"sign-in").click()
#     time.sleep(2)
#
# @then(u'user enter the apple id password "{password}"')
# def step_impl(context,password):
#     context.driver.find_element("xpath","//input[@class='form-textbox form-textbox-text ']").send_keys(password)
#     time.sleep(1)
#
#
# @then(u'user click on the next button')
# def step_impl(context):
#     context.driver.find_element('xpath', '//button[@id="sign-in"]').click()
