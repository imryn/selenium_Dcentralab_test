import pytest
from src.pages.base_page import BasePage
from src.pages.hord_page import HordPage
from src.locators.hord_locator import HordLocator
from src.configs.hord_enum import HordEnum

@pytest.mark.usefixtures("init_driver")
class TestHord:

    def test01_verify_sidbear_is_expanded(self, get_hord_url: str):
        hord_page = HordPage(self.driver)
        hord_page.open_home_page(get_hord_url)
        hord_page.click_sidebar_toggler()
        res = hord_page.check_first_item_in_list_is_exist_after_sidebar_opened()
        if not res:
            raise Exception("ETH Staking does not displayed, so sidebar is not expanded")


    def test02_verify_sidbear_is_collapsing(self, get_hord_url: str):
        hord_page = HordPage(self.driver)
        hord_page.open_home_page(get_hord_url)
        hord_page.click_sidebar_toggler()
        hord_page.click_sidebar_toggler()
        element = hord_page.check_invisibilty_of_sidebar_wrapper()
        assert element == None, "the element is still displayed, so the sidebar still opened"

    def test_verify_the_FAQ_section(self, get_hord_url: str):
        hord_page = HordPage(self.driver)
        hord_page.open_home_page(get_hord_url)
        hord_page.move_to_faq_section()
        questions = hord_page.get_faq_questions()
        for item, q in zip(questions, HordEnum.QUESTIONS_VALUES.value):
            if item.text not in q['title']:
                 raise Exception(f"the title value of the questions is wrong. look at {item.text}")

