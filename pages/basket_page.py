from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def basket_has_no_goods(self):
        assert self.element_is_not_present(*BasketPageLocators.ITEMS_TO_BUY_NOW), 'Basket not empty'

    def has_empty_basket_text(self):
        text = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text
        assert text == 'Your basket is empty. Continue shopping', 'Page does not have text about empty basket'