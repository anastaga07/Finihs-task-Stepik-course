from .base_page import BasePage
from .locators import ProductPageLocator
from selenium.common.exceptions import NoAlertPresentException 
import math

class ProductPage(BasePage): 
  def add_poduct_to_basket(self):
        add_to_cart = self.browser.find_element(*ProductPageLocator.PRODUCT_ADD_BUTTON)
        add_to_cart.click()

  def solve_quiz_and_get_code(self):
    alert = self.browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    try:
          alert = self.browser.switch_to.alert
          alert_text = alert.text
          print(f"Your code: {alert_text}")
          alert.accept()
    except NoAlertPresentException:
      print("No second alert presented")        

  def message_items_should_be_add_to_basket(self):
    """Проверка: название товара в сообщении совпадает с добавленным товаром"""
    title_of_item = self.browser.find_element(*ProductPageLocator.TITLE_OF_THE_ITEM).text
    message_after_add = self.browser.find_element(*ProductPageLocator.MESSAGE_AFTER_ADD_ITEM).text
    assert title_of_item == message_after_add, 'book title does not match message'

  def cost_should_be_eql_price(self):
    """Проверка: стоимость корзины равна цене товара"""
    price_item = self.browser.find_element(*ProductPageLocator.PRICE_ITEM).text
    basket_total = self.browser.find_element(*ProductPageLocator.BASKET_TOTAL).text
    assert price_item == basket_total, 'price of items does not eql basket total'
 
  def should_not_be_success_message(self):
        """Проверка, что элемент не появился на странице"""
        assert self.is_not_element_present(*ProductPageLocator.SUCCESS_MESSAGE), \
            'Success message is presented, but should not be'

  