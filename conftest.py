import pytest
from selenium import webdriver
import os
from src.configs.enviroment_settings import EnvironmentSettings
import allure

def env_vars():
    return EnvironmentSettings().get_env_variable_dict()

@pytest.fixture(scope="session")
def get_tokensfarm_url():
    return env_vars()['TOKENS_FARM_URL']

@pytest.fixture(scope="session")
def get_hord_url():
    return env_vars()['HORD_URL']



@pytest.fixture(autouse=True)
def init_driver(request):
    supported_browsers = ['chrome', 'firefox', 'ie']
    browser = env_vars()['BROWSER']

    if not browser:
        raise Exception("the env variable BROWSER must be set.")

    browser = browser.lower()

    if browser not in supported_browsers:
        raise Exception(f"provided browser {browser} is not one of the supported. {supported_browsers}")

    if browser == 'chrome' and browser in supported_browsers:
        driver = webdriver.Chrome()

    elif browser == 'firefox' and browser in supported_browsers:
        driver = webdriver.Firefox()

    elif browser == 'ie' and browser in supported_browsers:
        driver = webdriver.Ie()

    request.cls.driver = driver
    yield



