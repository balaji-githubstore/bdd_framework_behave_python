from pages.login_page import LoginPage
from pages.main_page import MainPage
from behave.log_capture import capture

def init_page_objects(context):
    context.login_page = LoginPage(context.driver)
    context.main_page = MainPage(context.driver)


def before_all(context):
    context.config.setup_logging()

# @capture
# def after_scenario(context):
