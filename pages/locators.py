from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".page_inner a.btn.btn-default")
    
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    
class BasketPageLocators():
    GOOD_CARD = (By.CSS_SELECTOR, ".basket_summary")
    BASKET_INNER = (By.CSS_SELECTOR, "#content_inner")

class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ALERT_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".basket-mini")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")

