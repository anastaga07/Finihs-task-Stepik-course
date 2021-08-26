from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add = self.browser.find_element(*ProductPageLocators.ADD_TO_BSK_BTN)
        add.click()

    def what_to_add(self):
        text = self.browser.find_element(*ProductPageLocators.WHAT_TO_ADD_NAME).text
        price = self.browser.find_element(*ProductPageLocators.WHAT_TO_ADD_PRICE).text
        return text, price

    def check_if_added_to_basket(self):
        text = self.browser.find_element(*ProductPageLocators.IS_IN_BASKET).text
        assert text == self.what_to_add()[0], 'Expected book not in basket'

    def check_correct_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE_ADDED_TO_BSK).text
        assert price == self.what_to_add()[1], 'Expected basket total is invalid'

    def should_not_be_success_message(self):
        assert self.element_is_not_present(*ProductPageLocators.IS_IN_BASKET), 'Element is present'

    def success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.IS_IN_BASKET), 'Element has not disappeared'