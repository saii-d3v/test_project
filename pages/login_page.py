from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Wrong URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    
    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_field.send_keys(email)

        password1_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        password1_field.send_keys(password)

        password2_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        password2_field.send_keys(password)

        register_btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        register_btn.click()
