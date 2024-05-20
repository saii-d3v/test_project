from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_ELEMENT = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE_ELEMENT = (By.CSS_SELECTOR, ".product_main .price_color")
    ADDED_PRODUCT_NAME_MESSAGE_ELEMENT = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    ADDED_PRODUCT_PRICE_MESSAGE_ELEMENT = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
