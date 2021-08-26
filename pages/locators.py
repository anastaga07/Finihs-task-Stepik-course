from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#id_login-username')
    REGISTER_FORM = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_FORM_1 = (By.CSS_SELECTOR, '#id_registration-password1')
    PASSWORD_FORM_2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    ADD_TO_BSK_BTN = (By.CSS_SELECTOR, '#add_to_basket_form button')
    PRICE_ADDED_TO_BSK = (By.CSS_SELECTOR, '#messages div:nth-child(3) .alertinner strong')
    IS_IN_BASKET = (By.CSS_SELECTOR, '#messages div:nth-child(1) strong')
    WHAT_TO_ADD_NAME = (By.CSS_SELECTOR, '.product_main h1')
    WHAT_TO_ADD_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    GO_BASKET_PAGE_BTN = (By.CSS_SELECTOR, '.page_inner div:nth-child(2) span a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    ITEMS_TO_BUY_NOW = (By.CSS_SELECTOR, '#content_inner div div h2')
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, '#content_inner p')