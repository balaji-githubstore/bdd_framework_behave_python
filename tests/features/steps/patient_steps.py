from assertpy import assert_that
from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@when(u'I click on Patient menu')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[text()='Patient']").click()


@when(u'I click on New search menu')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[text()='New/Search']").click()


@when(u'I fill the form')
def step_impl(context):
    context.driver.switch_to.frame(context.driver.find_element(By.XPATH, "//iframe[@name='pat']"))
    context.driver.find_element(By.CSS_SELECTOR, "#form_fname").send_keys(context.table.rows[0]["firstname"])
    context.driver.find_element(By.CSS_SELECTOR, "#form_lname").send_keys(context.table.rows[0]["lastname"])
    context.driver.find_element(By.CSS_SELECTOR, "#form_DOB").send_keys(context.table.rows[0]["dob"])

    Select(context.driver.find_element(By.CSS_SELECTOR, "#form_sex")).select_by_visible_text(
        context.table.rows[0]["gender"])


@when(u'I click on create new patient')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//*[@id='create']").click()
    context.driver.switch_to.default_content()


@when(u'I click on Confirm Create New Patient')
def step_impl(context):
    context.driver.switch_to.frame(context.driver.find_element(By.XPATH, "//iframe[@id='modalframe']"))
    context.driver.find_element(By.XPATH, "//input[@value='Confirm Create New Patient']").click()
    context.driver.switch_to.default_content()


@when(u'I handle the alert')
def step_impl(context):
    WebDriverWait(context.driver,20).until(expected_conditions.alert_is_present())
    print(context.driver.switch_to.alert.text)
    context.alert_text=context.driver.switch_to.alert.text
    context.driver.switch_to.alert.accept()


@when(u'I handle the happybirthday pop if available')
def step_impl(context):
    print('hbd')


@then(u'alert message should contains "{text}"')
def step_impl(context, text):
    print(context)
    assert_that(context.alert_text).contains(text)


@then(u'I should see the added patient details as "{text}"')
def step_impl(context, text):
    print(context)
    context.driver.switch_to.frame(context.driver.find_element(By.XPATH, "//iframe[@name='pat']"))
    actual_text=context.driver.find_element(By.XPATH, "//*[contains(text(),'Record')]").text
    assert_that(actual_text).contains(text)
