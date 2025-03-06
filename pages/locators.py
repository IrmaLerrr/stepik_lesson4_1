from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, ".page_inner a.btn.btn-default")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class LoginPageLocators():
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASS1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASS2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BTN = (By.NAME, "registration_submit")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASS = (By.CSS_SELECTOR, "#id_login-password")
    LOGIN_BTN = (By.NAME, 'login_submit')
    
class BasketPageLocators():
    GOOD_CARD = (By.CSS_SELECTOR, ".basket_summary")
    BASKET_INNER = (By.CSS_SELECTOR, "#content_inner")

class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    ALERT_MESSAGE = (By.CSS_SELECTOR, ".alert-success .alertinner")
    BASKET_TOTAL = (By.CSS_SELECTOR, ".basket-mini")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")

