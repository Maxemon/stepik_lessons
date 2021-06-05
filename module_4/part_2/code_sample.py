import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as exp
from selenium.webdriver.common.by import By

# Main Data
login_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
page_after_login = "http://selenium1py.pythonanywhere.com/ru/"


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(login_page_link)
    yield browser
    print("\nquit browser..")
    browser.quit()


def test_reg_new_user(browser):
    # Test Data
    email = "test5@test.te"
    password = "123456789Max"
    control_password = "123456789Max"
    reg_text = "Спасибо за регистрацию!"

    # Act
    browser.find_element_by_name("registration-email").send_keys(email)
    browser.find_element_by_name("registration-password1").send_keys(password)
    browser.find_element_by_name("registration-password2").send_keys(control_password)
    browser.find_element_by_name("registration_submit").click()

    # Assert
    assert exp.presence_of_element_located((By.CLASS_NAME, "alert-success")), f"No success message"
    success_message = browser.find_element_by_class_name("alertinner").text
    assert success_message == reg_text, f"No success message after login. {success_message}"
    assert exp.presence_of_element_located((By.CLASS_NAME, "icon-user")), f"No link to account"
    current_url = browser.current_url
    assert current_url == page_after_login, f"Expected url = {page_after_login}, Current url = {current_url}"
