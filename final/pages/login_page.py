from final.pages.base_page import BasePage
from final.pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def login_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "No email field on login form"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "No password field on login form"
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "No login button on login form"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "No email field on registration form"
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_PASSWORD), "No password field on registration form"
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM), "No password confirm field on registration form"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BUTTON), "No reg button on registration form"

    def should_be_success_login_message(self):
        assert self.is_element_present(*LoginPageLocators.SUCCESS_LOGIN_MESSAGE), "No success message about login"

    def should_be_email_warning_message(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_EMAIL_WARNING_MESSAGE), "No registration email warning message"

    def should_be_warning_message(self):
        assert self.is_element_present(
            *LoginPageLocators.REGISTRATION_WARNING_MESSAGE), "No registration warning message"
