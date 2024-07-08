from selenium.webdriver.common.by import By
from selenium import common as c

from infra.base_page import BasePage


class BasePageApp(BasePage):
    YOUTUBE_LOGO = '//ytd-masthead//a[@class="yt-simple-endpoint style-scope ytd-topbar-logo-renderer"]'
    MENU_BUTTON = '//ytd-masthead//yt-icon[@id="guide-icon"]'
    SEARCH_BAR_INPUT = '//div[@id="search-input"]'
    SEARCH_BUTTON = '//ytd-searchbox//button//yt-icon[@class="style-scope ytd-searchbox"]'

    def _init_(self, driver):
        super().__init__(driver)
        try:
            self._youtube_logo = self._driver.find_element(By.XPATH, self.YOUTUBE_LOGO)
            self._menu_button = self._driver.find_element(By.XPATH, self.MENU_BUTTON)
            self._search_bar_input = self._driver.find_element(By.XPATH, self.SEARCH_BAR_INPUT)
            self._search_button = self._driver.find_element(By.XPATH, self.SEARCH_BUTTON)

        except c.NoSuchElementException as e:
            print("NoSuchElementException", e)

    def click_menu_button(self):
        self._menu_button.click()

    def click_youtube_logo(self):
        self._youtube_logo.click()

    def fill_search_bar_input(self):
        self._search_bar_input.click()

    def click_search_button(self):
        self._search_button.click()
