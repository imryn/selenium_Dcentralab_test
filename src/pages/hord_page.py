from src.helpers.selenium_helper import SeleniumHelper
from src.locators.hord_locator import HordLocator
from src.pages.base_page import BasePage
import time

class HordPage(HordLocator, BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def click_sidebar_toggler(self):
        element = self.selenium_helper.get_list_of_elements(self.SIDE_BAR_TOGGLER)
        self.driver.execute_script("arguments[0].click();", element[0])

    def check_first_item_in_list_is_exist_after_sidebar_opened(self):
        elements = self.selenium_helper.get_list_of_elements(self.SIDE_BAR_FIRST_ITEM)
        return elements[0]

    def check_invisibilty_of_sidebar_wrapper(self):
        self.selenium_helper.invisibility_of_element(self.SIDE_BAR_FIRST_ITEM)

    def move_to_faq_section(self):
        element = self.selenium_helper.get_list_of_elements(self.FAQ)
        self.selenium_helper.move_to_element(element[0])

    def get_faq_questions(self):
        elements = self.selenium_helper.get_list_of_elements(self.FAQ_QUESTIONS)
        return elements