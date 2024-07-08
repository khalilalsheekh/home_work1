from selenium import webdriver
from selenium import common as C

from infra.config_provider import ConfigProvider


class BrowserWrapper:
    def __init__(self):
        self.driver = None
        self.config = ConfigProvider.load_config_json()

    def get_driver(self, url):
        try:
            if self.config["browser"] == "Chrome":
                self._driver = webdriver.Chrome()
            elif self.config["browser"] == "Firefox":
                self._driver = webdriver.Firefox()
            else:
                print("browser not excite")
            self._driver.get(url)
            return self._driver

        except C.WebDriverException as e:
            print("ERROR : ", e)
