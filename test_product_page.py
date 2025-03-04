from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_good_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_that_good_in_basket()
    page.cost_is_equal_to_price_of_good()
