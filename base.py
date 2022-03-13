import pytest
import time
from ui.locators import basic_locators
from ui.locators import pop_up_locators
from selenium.common.exceptions import StaleElementReferenceException


CLICK_RETRY = 3
EMAIL = 'penem41580@siberpay.com'
PASSWORD = 'QAZwsx123'


class BaseCase:
    driver = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver):
        self.driver = driver

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)



    def login(self):
        time.sleep(2)
        elem = self.find(basic_locators.LOGIN_BUTTON)
        elem.click()
        time.sleep(2)
        elem = self.find(pop_up_locators.EMAIL_FIELD)
        elem.send_keys(EMAIL)
        elem = self.find(pop_up_locators.PASSWORD_FIELD)
        elem.send_keys(PASSWORD)
        elem = self.find_elements(pop_up_locators.LOGIN_BUTTON)
        elem[1].click()

    def login(self):
        time.sleep(2)
        elem = self.find(basic_locators.LOGIN_BUTTON)
        elem.click()
        time.sleep(2)
        elem = self.find(pop_up_locators.EMAIL_FIELD)
        elem.send_keys(EMAIL)
        elem = self.find(pop_up_locators.PASSWORD_FIELD)
        elem.send_keys(PASSWORD)
        elem = self.find_elements(pop_up_locators.LOGIN_BUTTON)
        elem[1].click()


    def click(self, locator):
        for i in range(CLICK_RETRY):
            try:
                elem = self.find(locator)
                # if i < 2:
                #     self.driver.refresh()
                elem.click()
                return
            except StaleElementReferenceException:
                if i == CLICK_RETRY - 1:
                    raise