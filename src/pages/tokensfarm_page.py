from src.helpers.selenium_helper import SeleniumHelper
from src.locators.tokensfarm_locator import TokensFarmLocator
from src.pages.base_page import BasePage

class TokensFarmPage(TokensFarmLocator, BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def scroll_to_on_what_chain_selector_by_css_selector(self):
        element = self.selenium_helper.get_list_of_elements(self.ON_WHAT_CHAIN_IS_TOKEN_OF_THIS_FARM_CSS_SELECTOR)
        self.selenium_helper.move_to_element(element[0])


    def scroll_to_on_what_chain_selector_by_xpath_selector(self):
        element = self.selenium_helper.get_list_of_elements(self.ON_WHAT_CHAIN_IS_TOKEN_OF_THIS_FARM_XPATH)
        self.selenium_helper.move_to_element(element[0])

