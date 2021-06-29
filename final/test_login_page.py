import pytest

from pages.login_page import LoginPage
from pages.locators import LoginPageLocators

link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
existing_username = "test5@test.te"
existing_username_password = "123456789Max"


class TestLoginPage:
    def test_registration_of_new_user(self, browser):
        # Arrange
        page = LoginPage(browser, link)
        page.open()
        email, password = page.new_user()

        # Act
        page.register_new_user(email, password)

        # Assert
        page.should_be_authorized_user()
        page.should_be_success_login_message()

    def test_registration_of_existing_user(self, browser):
        # Arrange
        page = LoginPage(browser, link)
        page.open()

        # Act
        page.register_new_user(existing_username, existing_username_password)

        # Assert
        page.should_be_email_warning_message()
        page.should_be_warning_message()
        page.should_be_filled_field(*LoginPageLocators.REGISTRATION_EMAIL, existing_username)
        page.should_be_empty_field(*LoginPageLocators.REGISTRATION_PASSWORD)
        page.should_be_empty_field(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM)
