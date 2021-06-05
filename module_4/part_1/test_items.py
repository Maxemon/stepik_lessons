from selenium.webdriver.support import expected_conditions as exp
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button(browser):
    browser.get(link)
    assert exp.presence_of_element_located((By.CLASS_NAME, "btn-add-to-basket")), "No ""Add to basket"" button"
    button_text = browser.find_element_by_class_name("btn-add-to-basket").text
    assert button_text == "Добавить в корзину", "Text in button is incorrect"
