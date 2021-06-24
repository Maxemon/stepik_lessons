import pytest

from .pages.base_page import BasePage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


class TestProductPage:
    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Act
        page.add_product_to_basket()

        # Assert
        page.should_not_be_success_message()

    @pytest.mark.xfail
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Act
        page.add_product_to_basket()

        # Assert
        page.success_message_should_disappeared()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        # Arrange
        page = ProductPage(browser, link)

        # Act
        page.open()

        # Assert
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Act
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)

        # Assert
        login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        # Arrange
        page = ProductPage(browser, link)
        page.open()

        # Act
        page.go_to_basket()
        basket_page = BasketPage(browser, browser.current_url)

        # Assert
        basket_page.should_be_empty()
        basket_page.should_be_empty_message()


@pytest.mark.add_to_basket_from_PP
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, login_link)
        page.open()
        base = BasePage(browser, link)
        email, password = base.new_user()
        page.register_new_user(email, password)
        base.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        # Arrange
        page = ProductPage(browser, link)

        # Act
        page.open()

        # Assert
        page.should_not_be_success_message()

    @pytest.mark.parametrize('promo_offer',
                             ["newYear2019", "offer0", "offer1", "offer2", "offer3", "offer4", "offer5", "offer6",
                              pytest.param("offer7", marks=pytest.mark.xfail), "offer8",
                              "offer9"])
    def test_user_can_add_product_to_basket(self, browser, promo_offer):
        # Arrange
        test_link = link + "/?promo=" + promo_offer
        page = ProductPage(browser, test_link)
        page.open()

        # Act
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()

        # Assert
        page.check_message_about_adding()
        page.check_message_about_basket_sum()
