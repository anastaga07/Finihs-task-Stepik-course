from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, 'url is invalid, does not contain "login"'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'no login form on the page'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'no registration form on the page'

    def register_new_user(self):
        email =  str(time.time()) + '@email.org'
        password = '123456@_abc'
        email_form = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        password_form_1 = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM_1)
        password_form_2 = self.browser.find_element(*LoginPageLocators.PASSWORD_FORM_2)
        email_form.send_keys(email)
        password_form_1.send_keys(password)
        password_form_2.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()