from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_BTN = (By.CSS_SELECTOR, ".header .btn-group a.btn-default")



# class MainPageLocators:
    


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BTN = (By.CSS_SELECTOR, "button.btn-primary[name='registration_submit']")



class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME_ELEMENT = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE_ELEMENT = (By.CSS_SELECTOR, ".product_main .price_color")
    ADDED_PRODUCT_NAME_MESSAGE_ELEMENT = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    ADDED_PRODUCT_PRICE_MESSAGE_ELEMENT = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    SUCCESS_MEESSAGE = (By.CSS_SELECTOR, ".alert-success")


class BasketPageLocators:
    BASKET_ITEM_LIST = (By.CSS_SELECTOR, "#basket_formset")
    MESSAGE_BASKET_EMPTY_ELEMENT = (By.CSS_SELECTOR, "#content_inner p")