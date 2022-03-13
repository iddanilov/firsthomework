import pytest
import time
from base import BaseCase
from ui.locators import basic_locators


class TestMyTarget(BaseCase):
    def test_login(self):
        self.login()
        elem =  self.find(basic_locators.USER_BUTTON)
        assert elem.

    def test_logout(self):
        self.login()
        self.logout()
        assert 'No results found' not in self.driver.page_source

    @pytest.mark.skip('skip')
    def test_negative_search(self):
        self.search('adasdasdasdasdasda')
        assert 'No results found' not in self.driver.page_source

    @pytest.mark.UI
    def test_page_change(self):
        self.click(basic_locators.GO_BUTTON_LOCATOR)