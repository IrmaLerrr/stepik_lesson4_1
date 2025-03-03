from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_good_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "Add to basket button is not presented"
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        button.click()
    
    def should_be_message_that_good_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.ALERT_MESSAGE), "Alert Message is not presented"
        alert = self.browser.find_elements(*ProductPageLocators.ALERT_MESSAGE)
        print(alert[0].text)
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        expected = f"{name.text} has been added to your basket."
        actual = alert[0].text
        assert actual == expected, f"Alert Message is incorrect. Expected is {expected} Actual is {actual}"
    
    def cost_is_equal_to_price_of_good(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL), "Alert Message is not presented"
        bucket = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
        print(bucket.text)
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        expected = f"Basket total: {price.text}\nView basket"
        actual = bucket.text
        assert actual == expected, f"Alert Message is incorrect. Expected is {expected} Actual is {actual}"

