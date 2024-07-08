from selenium.webdriver.common.by import By
from selenium import common as C

from infra.base_page import BasePage


class HomePage(BasePage):
    SHORTS_BUTTON = '//ytd-guide-section-renderer//a[@title="Shorts"]'
    VIDEO_SELECT = ''

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._shorts_button = self._driver.find_element(By.XPATH, self.SHORTS_BUTTON)
            self._video_select = self._driver.find_element(By.XPATH, self.VIDEO_SELECT)

        except C.NoSuchElementException as e:
            print("NoSuchElementException")

    def click_on_shorts_button(self):
        self._shorts_button.click()

    def click_on_video(self):
        self._video_select.click()


