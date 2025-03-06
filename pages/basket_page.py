from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import BasketPageLocators

basket_messages = {
    "en-br":"Your basket is empty. Continue shopping",
    "ru":"Ваша корзина пуста. Продолжить покупки"
}

class BasketPage(BasePage):
    def should_be_basket_url(self):
        assert self.browser.current_url == f'https://selenium1py.pythonanywhere.com/{self.browser.user_language}/basket/', "Basket url is incorrect"

    def should_be_no_good(self):
        assert self.is_not_element_present(*BasketPageLocators.GOOD_CARD), "Good card is presented"
        
    def should_be_message_that_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_INNER), "Basket is not presented"
        element = self.browser.find_element(*BasketPageLocators.BASKET_INNER)
        print(element.text)
        expected = basket_messages.get(self.browser.user_language, 'Your basket is empty. Continue shopping')
        actual = element.text
        assert actual == expected, f"Alert Message is incorrect. Expected is {expected} Actual is {actual}"

