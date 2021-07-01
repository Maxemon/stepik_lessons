import pytest

from final.pages.locators import LoginPageLocators
from final.pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
existing_username = "test5@test.te"
existing_username_password = "123456789Max"


@pytest.mark.personal_tests
class TestUserRegistration:
    def test_registration_of_new_user(self, browser):
        # Arrange
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_page()
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
        page.should_be_login_page()

        # Act
        page.register_new_user(existing_username, existing_username_password)

        # Assert
        page.should_be_email_warning_message()
        page.should_be_warning_message()
        page.should_be_filled_field(*LoginPageLocators.REGISTRATION_EMAIL, existing_username)
        page.should_be_empty_field(*LoginPageLocators.REGISTRATION_PASSWORD)
        page.should_be_empty_field(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM)


@pytest.mark.personal_tests
class TestUserLogin:
    def test_correct_user_login(self, browser):
        # Arrange
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_page()

        # Act
        page.login_user(existing_username, existing_username_password)

        # Assert
        page.should_be_success_login_message()
        page.should_be_authorized_user()
