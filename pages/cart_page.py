from pages.base_page import Page
from selenium.webdriver.common.by import By

class CartPage(Page):

    ITEM_IN_CART = (By.XPATH, "//div[contains(text(),'SkinnyPop')]")
    CART_ICON = (By.CSS_SELECTOR, "a[data-test='@web/CartLink']")
    # Add to cart
    ADD_TO_CART = (By.CSS_SELECTOR, "button[id*='addToCartButtonOr']")
    # Shipping option selected
    SHIPPING_BUTTON = (By.CSS_SELECTOR, "button[data-test='fulfillment-cell-shipping']")
    # Shipping option selected
    ADD_TO_CART_SMALL_WINDOW = (By.CSS_SELECTOR, "button[data-test='shippingButton']")
    # View cart button
    VIEW_CART_CHECK_OUT = (By.CSS_SELECTOR, "a[class*='ButtonSecondary-sc-125aivg-0 hCWYcY bxLMor']")
    def add_to_cart(self):

        # Add item to cart
        self.driver.find_element(*self.ADD_TO_CART).click()
        # Shipping option selected
        self.driver.find_element(*self.SHIPPING_BUTTON).click()
        # Click View Cart button
        self.driver.find_element(*self.VIEW_CART_CHECK_OUT).click()

    def verify_cart(self):
        # actual_text = self.find_element(*self.ITEM_IN_CART).text
        # expected_text = 'SkinnyPop'
        # assert expected_text == actual_text, f'Expect {expected_text} snack is NOT in cart'
        # print("Test case has passed")
        self.verify_partial_text("SkinnyPop",*self.ITEM_IN_CART)


