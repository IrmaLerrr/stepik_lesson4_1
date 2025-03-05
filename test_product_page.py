from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators
import pytest

@pytest.mark.skip(reason="Тест устарел")
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_good_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_that_good_in_basket()
    page.cost_is_equal_to_price_of_good()

@pytest.mark.skip(reason="Тест устарел")
@pytest.mark.parametrize('link', ["https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_good_to_basket()
    assert page.is_not_element_present(*ProductPageLocators.ALERT_MESSAGE), "Sucsess message is presented"

@pytest.mark.skip(reason="Тест устарел")
@pytest.mark.parametrize('link', ["https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"])
def test_guest_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    assert page.is_not_element_present(*ProductPageLocators.ALERT_MESSAGE), "Sucsess message is presented"

@pytest.mark.skip(reason="Тест устарел")
@pytest.mark.parametrize('link', ["https://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"])
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_good_to_basket()
    assert page.is_disappeared(*ProductPageLocators.ALERT_MESSAGE), "Sucsess message is not disappeared"

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

