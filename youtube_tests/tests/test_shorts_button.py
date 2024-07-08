import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from logic.home_page import HomePage


class TestShortsButton(unittest.TestCase):
    def setup(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])
        self.home_page = HomePage(self.driver)

    def test_short_button(self):
        self.home_page.click_on_shorts_button()
        self.driver.implicitly_wait(10)
        self.assertEqual(self.driver.current_url, self.config["url"] + "/shorts")


if __name__ == "__main__":
    unittest.main()
