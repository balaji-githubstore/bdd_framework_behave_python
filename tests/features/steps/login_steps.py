from assertpy import assert_that
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from pages.main_page import MainPage
from tests.features.conf.environment import init_page_objects


@given(u'I have browser with openemr application')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)
    context.driver.get("https://demo.openemr.io/b/openemr")
    init_page_objects(context)


@when(u'I enter username as "{text}"')
def step_impl(context, text):
    # context.driver.find_element(By.ID, "authUser").send_keys(text)
    context.login_page.enter_username(text)


@when(u'I enter password as "{text}"')
def step_impl(context, text):
    context.driver.find_element(By.CSS_SELECTOR, "#clearPass").send_keys(text)


@when(u'I click on login')
def step_impl(context):
    context.driver.find_element(By.ID, "login-button").click()


@then(u'I should get access to dashboard with "{text}"')
def step_impl(context, text):
    assert_that(text).is_equal_to(context.driver.title)


@then(u'I should not get access to dashboard with "{expect_error}"')
def step_impl(context, expect_error):
    assert_that(context.driver.page_source).contains(expect_error)
