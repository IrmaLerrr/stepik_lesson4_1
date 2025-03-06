from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url == f'https://selenium1py.pythonanywhere.com/{self.browser.user_language}/accounts/login/', "Login url is incorrect"
        
    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        self.should_be_register_form()
        assert self.is_element_present(*LoginPageLocators.REGISTER_EMAIL), "Register email is not presented"
        input1 = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        input1.send_keys(email)
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASS1), "Register password1 is not presented"
        input2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASS1)
        input2.send_keys(password)
        assert self.is_element_present(*LoginPageLocators.REGISTER_PASS2), "Register password2 is not presented"
        input3 = self.browser.find_element(*LoginPageLocators.REGISTER_PASS2)
        input3.send_keys(password)
        assert self.is_element_present(*LoginPageLocators.REGISTER_BTN), "Register button is not presented"
        btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        btn.click()
