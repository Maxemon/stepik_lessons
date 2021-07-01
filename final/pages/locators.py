from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "[name='login_submit']")

    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
    REGISTRATION_EMAIL_WARNING_MESSAGE = (By.CSS_SELECTOR, ".error-block")
    REGISTRATION_WARNING_MESSAGE = (By.CSS_SELECTOR, ".alert-danger")

    SUCCESS_LOGIN_MESSAGE = (By.CSS_SELECTOR, ".alert-success")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, ".alertinner > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > p.price_color")
    PRODUCT_PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alertinner > p > strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    SMTH_IN_BASKET = (By.CSS_SELECTOR, ".basket_summary")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner > p")


class CataloguePageLocators:
    CATEGORY_TREE = (By.CSS_SELECTOR, ".side_categories")

    SELECTED_CATEGORY = (By.CSS_SELECTOR, ".page-header h1")

    PRODUCTS_QTY = (By.CSS_SELECTOR, ".form-horizontal")

    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_pod h3")
    PRODUCT_STATUS = (By.CSS_SELECTOR, ".product_price .availability")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_price .price_color")
    PRODUCT_RATING = (By.CSS_SELECTOR, ".star-rating")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".product_price button")

    ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, ".alertinner > strong")

    LINK_TO_CLOTHING = (By.CSS_SELECTOR, "[href='/ru/catalogue/category/clothing_1/']")
    LINK_TO_BOOKS = (By.CSS_SELECTOR, "[href='/ru/catalogue/category/books_2/']")
    LINK_TO_FICTION = (By.CSS_SELECTOR, "[href='/ru/catalogue/category/books/fiction_3/']")
    LINK_TO_COMPUTERS_IN_LIT = (
        By.CSS_SELECTOR, "[href='/ru/catalogue/category/books/fiction/computers-in-literature_4/']")
    LINK_TO_NON_FICTION = (By.CSS_SELECTOR, ".nav-list > [href='/ru/catalogue/category/books/non-fiction_5/']")
    LINK_TO_ESSENTIAL_PROG = (
        By.CSS_SELECTOR, "[href='/ru/catalogue/category/books/non-fiction/essential-programming_6/']")
    LINK_TO_HACKING = (By.CSS_SELECTOR, "[href='/ru/catalogue/category/books/non-fiction/hacking_7/']")
