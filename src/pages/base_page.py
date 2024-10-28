import pytest
from src.helpers.selenium_helper import SeleniumHelper
from selenium import webdriver

class BasePage:

    def __init__(self, driver: webdriver):
        self.driver = driver
        self.selenium_helper = SeleniumHelper(self.driver)

    def open_home_page(self, url: str):
        self.driver.get(url)
        self.driver.maximize_window()


