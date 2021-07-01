from final.pages.base_page import BasePage
from final.pages.locators import CataloguePageLocators


class CataloguePage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*CataloguePageLocators.ADD_TO_BASKET_BUTTON).click()

    def go_to_category(self, locator):
        self.browser.find_element(locator).click()

    def check_message_about_adding(self):
        assert self.browser.find_element(*CataloguePageLocators.PRODUCT_NAME).text == self.browser.find_element(
            *CataloguePageLocators.ADD_TO_BASKET_MESSAGE).text, "Message about adding is incorrect"

    def should_be_category_url(self, locator):
        expected_category_link = {
            "*CataloguePageLocators.LINK_TO_CLOTHING": "clothing_1",
            "*CataloguePageLocators.LINK_TO_BOOKS": "books_2",
            "*CataloguePageLocators.LINK_TO_FICTION": "fiction_3",
            "*CataloguePageLocators.LINK_TO_COMPUTERS_IN_LIT": "computers-in-literature_4",
            "*CataloguePageLocators.LINK_TO_NON_FICTION": "non-fiction_5",
            "*CataloguePageLocators.LINK_TO_ESSENTIAL_PROG": "essential-programming_6",
            "*CataloguePageLocators.LINK_TO_HACKING": "hacking_7"
        }
        assert expected_category_link[locator] in self.browser.current_url

    def should_be_category_tree(self):
        assert self.is_element_present(*CataloguePageLocators.CATEGORY_TREE), "No category tree"

    def should_be_product(self):
        assert self.is_element_present(*CataloguePageLocators.PRODUCT_NAME), "No product name"
        assert self.is_element_present(*CataloguePageLocators.PRODUCT_STATUS), "No product status"
        assert self.is_element_present(*CataloguePageLocators.PRODUCT_PRICE), "No product price"
        assert self.is_element_present(*CataloguePageLocators.PRODUCT_RATING), "No product rating"
        assert self.is_element_present(*CataloguePageLocators.ADD_TO_BASKET_BUTTON), "No Add to basket button"

    def should_be_products_qty(self):
        assert self.is_element_present(*CataloguePageLocators.PRODUCTS_QTY), "No products qty"

    def should_be_selected_category(self):
        assert self.is_element_present(*CataloguePageLocators.SELECTED_CATEGORY), "No selected category header"
