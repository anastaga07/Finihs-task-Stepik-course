from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty_basket(self):
        """Проверка на пустую корзину"""
        self.guest_cant_see_product_in_basket()
        self.guest_can_see_empty_basket()
    

    def guest_cant_see_product_in_basket(self):
        """Проверка: не должно быть товаров в корзине"""
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET), \
            "Product in basket is presented, but should not be"

    def guest_can_see_empty_basket(self):
        """Проверка: есть сообщение корзина пуста"""
        text_message_in_basket = self.browser.find_element(*BasketPageLocators.MESSAGE_IN_BASKET).text
        assert 'Your basket is empty' in text_message_in_basket, \
            'The basket not exist the message that basket is empty'