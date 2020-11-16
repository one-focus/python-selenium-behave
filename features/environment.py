import configparser

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# TODO check all context attributes on https://behave.readthedocs.io/en/latest/context_attributes.html#user-attributes
def before_all(context):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.implicitly_wait(5)
    # read config
    parser = configparser.ConfigParser()
    parser.read('behave.ini')
    context.config = parser


def before_scenario(context, scenario):
    context.driver.delete_all_cookies()


def after_step(context, step) -> None:
    if step.status == "failed":
        try:
            allure.attach(context.driver.get_screenshot_as_png(),
                          name=f'{context.driver.desired_capabilities["platformVersion"]}',
                          attachment_type=allure.attachment_type.PNG)
        except:
            pass


def after_all(context):
    context.driver.quit()
