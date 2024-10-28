import pytest
from src.pages.base_page import BasePage
from src.pages.hord_page import HordPage
from src.locators.hord_locator import HordLocator


@pytest.mark.usefixtures("init_driver")
class TestHord:

    def test01_verify_sidbear_is_expanded(self, get_hord_url):
        hord_page = HordPage(self.driver)
        hord_page.open_home_page(get_hord_url)
        hord_page.click_sidebar_toggler()
        hord_page.check_expended_class_name_displayed_on_element_after_sidebar_opened()


    def test02_verify_sidbear_is_collapsing(self, get_hord_url):
        hord_page = HordPage(self.driver)
        hord_page.open_home_page(get_hord_url)
        hord_page.click_sidebar_toggler()
        hord_page.click_sidebar_toggler()
        element = hord_page.check_invisibilty_of_sidebar_wrapper()
        assert element == None, "the element is still displayed, so the sidebar still opened"

