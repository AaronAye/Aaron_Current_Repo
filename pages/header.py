from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Header(Page):
    # Search input
    SEARCH_INPUT = (By.ID, 'search')
    # Search button
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[data-test='@web/Search/SearchButton']")

    # Click on cart icon
    # CART_ICON = (By.CSS_SELECTOR, "a[data-test='@web/CartLink']")
    # # Add to cart
    # ADD_TO_CART = (By.CSS_SELECTOR, "button[id*='addToCartButtonOr']")
    # # Shipping option selected
    # SHIPPING_BUTTON = (By.CSS_SELECTOR, "button[data-test='fulfillment-cell-shipping']")
    # # Shipping option selected
    # ADD_TO_CART_SMALL_WINDOW = (By.CSS_SELECTOR, "button[data-test='shippingButton']")
    # # View cart button
    # VIEW_CART_CHECK_OUT = (By.CSS_SELECTOR, "a[class*='ButtonSecondary-sc-125aivg-0 hCWYcY bxLMor']")

    def search_products(self, search_text):
        # Type "Snacks" in search bar
        self.input_text(search_text, *self.SEARCH_INPUT)
        # Click search button
        self.click(*self.SEARCH_BUTTON)

    # def add_to_cart(self):
    #
    #     # Add item to cart
    #     self.driver.find_element(*self.driver.ADD_TO_CART).click()
    #     # Shipping option selected
    #     self.driver.find_element(*self.driver.SHIPPING_BUTTON).click()
    #     # Click View Cart button
    #     self.driver.find_element(*self.driver.VIEW_CART_CHECK_OUT).click()
