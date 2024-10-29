import pytest
from src.pages.base_page import BasePage
from src.pages.tokensfarm_page import TokensFarmPage
from src.locators.tokensfarm_locator import TokensFarmLocator


@pytest.mark.usefixtures("init_driver")
class TestTokensFarm:

    def test_scroll_to_on_what_chain_by_css_selector(self, get_tokensfarm_url: str):
        tokens_farm_page = TokensFarmPage(self.driver)
        tokens_farm_page.open_home_page(get_tokensfarm_url)
        tokens_farm_page.scroll_to_on_what_chain_selector_by_css_selector()


    def test_scroll_to_on_what_chain_by_xpath_selector(self, get_tokensfarm_url: str):
        tokens_farm_page = TokensFarmPage(self.driver)
        tokens_farm_page.open_home_page(get_tokensfarm_url)
        tokens_farm_page.scroll_to_on_what_chain_selector_by_xpath_selector()


