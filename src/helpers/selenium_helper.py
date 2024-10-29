from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.webelement import WebElement

import time

class SeleniumHelper:

    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 10

    def wait_and_click_element(self, locator: str):
        WebDriverWait(self.driver, self.default_timeout).until(
            EC.visibility_of_element_located(locator)
        ).click()

    def visibility_of_element(self, locator: str):
        WebDriverWait(self.driver, self.default_timeout).until(
            EC.visibility_of_element_located(locator))

    def invisibility_of_element(self, locator: str):
        WebDriverWait(self.driver, self.default_timeout).until(
            EC.invisibility_of_element(locator))

    def get_list_of_elements(self, locator: str):
        elements = WebDriverWait(self.driver, self.default_timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
        return elements

    def move_to_element(self, element: WebElement):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()






