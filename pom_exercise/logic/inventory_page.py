from selenium.webdriver.common.by import By


class InventoryPage(BasePageApp):
    ADD_TO_CART_BUTTON = '//button[@id="add-to-cart-sauce-labs-backpack"]'
    ITEM_TITTLE_BUTTON = '//div[contains(text(),"Sauce Labs Backpack")]'
    ITEM_IMAGE_BUTTON = '//img[@alt="Sauce Labs Backpack"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._add_to_cart_button = self._driver.find_element(By.XPATH, self.ADD_TO_CART_BUTTON)
        self.item_tittle_button = self._driver.find_element(By.XPATH, self.ITEM_TITTLE_BUTTON)
        self.item_image_button = self._driver.find_element(By.XPATH , self.ITEM_IMAGE_BUTTON)

    def add_to_cart_button_click(self):
        self._add_to_cart_button.click()

    def item




