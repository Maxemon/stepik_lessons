from selenium.webdriver.support import expected_conditions as exp
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
button = By.CLASS_NAME, "btn-add-to-basket"
expected_button_text = {
    "ru": "Добавить в корзину",
    "en-GB": "Add to basket",
    "es": "Añadir al carrito",
    "fr": "Ajouter au panier"
}


def test_add_to_basket_button(browser, language):
    # Arrange
    browser.get(link)

    # Assert
    assert exp.presence_of_element_located(button), f"No '{expected_button_text[language]}' button"
    button_text = browser.find_element(button).text
    assert button_text == expected_button_text[language], "Text in button is incorrect"
