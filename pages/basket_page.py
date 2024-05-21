from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_page(self):
        self.should_be_basket_url()

    
    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "Wrong URL"
    

    def should_not_be_item_list(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM_LIST), "Item list should not be presented"


    def should_be_basket_empty_message(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_EMPTY_ELEMENT), '"Basket empty" message is not presented'
