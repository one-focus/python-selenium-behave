import configparser
from selenium import webdriver


# TODO check all context attributes on https://behave.readthedocs.io/en/latest/context_attributes.html#user-attributes
def before_all(context):
    context.driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    context.driver.implicitly_wait(5)
    # read config
    parser = configparser.ConfigParser()
    parser.read('behave.ini')
    context.config = parser


def before_scenario(context, scenario):
    context.driver.delete_all_cookies()


def after_all(context):
    context.driver.quit()
