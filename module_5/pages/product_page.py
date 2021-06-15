from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def check_message_about_adding(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_MESSAGE).text, "Message about adding is incorrect"

    def check_message_about_basket_sum(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text, "Product price in basket is incorrect"
