import pytest

from final.pages.catalogue_page import CataloguePage
from final.pages.locators import CataloguePageLocators

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/"


@pytest.mark.personal_tests
class TestCataloguePage:
    def test_page_view(self, browser):
        # Arrange
        page = CataloguePage(browser, link)

        # Act
        page.open()

        # Assert
        page.should_be_category_tree()
        page.should_be_selected_category()
        page.should_be_products_qty()
        page.should_be_product()

    def test_add_product_to_basket(self, browser):
        # Arrange
        page = CataloguePage(browser, link)
        page.open()

        # Act
        page.add_product_to_basket()

        # Assert
        page.check_message_about_adding()

    # Не придумал как пощёлкать дерево категорий. Все функции есть, а как передать им локаторы чёт не дошло.
    @pytest.mark.personal_tests
    @pytest.mark.skip
    @pytest.mark.parametrize('locator',
                             [*CataloguePageLocators.LINK_TO_CLOTHING,
                              *CataloguePageLocators.LINK_TO_BOOKS,
                              *CataloguePageLocators.LINK_TO_FICTION,
                              *CataloguePageLocators.LINK_TO_COMPUTERS_IN_LIT,
                              *CataloguePageLocators.LINK_TO_NON_FICTION,
                              *CataloguePageLocators.LINK_TO_ESSENTIAL_PROG,
                              *CataloguePageLocators.LINK_TO_HACKING])
    def test_catalogue_tree(self, browser, locator):
        # Arrange
        page = CataloguePage(browser, link)
        page.open()

        # Act
        page.go_to_category(locator)

        # Assert
        page.should_be_category_url(locator)
        page.should_be_category_tree()
        page.should_be_selected_category()
        page.should_be_products_qty()
        page.should_be_product()
