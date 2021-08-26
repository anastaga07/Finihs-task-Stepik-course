from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators ():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    PRODUCT_ADD_BUTTON= (By.CSS_SELECTOR, "button.btn-add-to-basket")   
    MESSAGE_AFTER_ADD_ITEM = (By.CSS_SELECTOR, '.alert-success:first-child .alertinner strong')
    TITLE_OF_THE_ITEM = (By.CSS_SELECTOR, 'h1')
    PRICE_ITEM = (By.CSS_SELECTOR, '.product_main .price_color')
    BASKET_TOTAL = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alertinner')

class BasePageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a")

class BasketPageLocators():
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#content_inner h2")
    MESSAGE_IN_BASKET = (By.CSS_SELECTOR, '#content_inner')

