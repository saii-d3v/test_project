from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_product_info(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_ELEMENT), "Product name is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_ELEMENT), "Product price is not presented"

        self.product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_ELEMENT).text
        self.product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ELEMENT).text

        # print(self.product_name)
        # print(self.product_price)

    def add_product_to_basket(self):
        btn_add_to_basket = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        btn_add_to_basket.click()

    def should_be_added_product_info(self):
        assert self.is_element_present(*ProductPageLocators.ADDED_PRODUCT_NAME_MESSAGE_ELEMENT), "Added product name is not presented"
        assert self.is_element_present(*ProductPageLocators.ADDED_PRODUCT_PRICE_MESSAGE_ELEMENT), "Added product price is not presented"

        self.added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME_MESSAGE_ELEMENT).text
        self.added_product_price = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE_MESSAGE_ELEMENT).text

        # print(self.added_product_name)
        # print(self.added_product_price)

    def should_be_btn_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BTN_ADD_TO_BASKET ), '"Add to basket" button is not presented'

    def should_add_correct_product(self):
        assert self.product_name == self.added_product_name, "Wrong product name"
        assert self.product_price == self.added_product_price, "Wrong product price"
