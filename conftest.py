import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.remote.webdriver import WebDriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                 help="Choose browser: chrome, edge or firefox")
    parser.addoption('--language', action='store', default="en",
                 help="Choose language")


class CustomBrowser:
    def __init__(self, driver, user_language):
        self.driver = driver
        self.user_language = user_language 
    def __getattr__(self, name):
        return getattr(self.driver, name)


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        chrome_options = Options()
        chrome_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=chrome_options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
    elif browser_name == "edge":
        print("\nstart edge browser for test..")
        edge_options = Options()
        edge_options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Edge(options=edge_options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    
    language_exceptions = {
        "en": "en-gb"
    }
    user_language = language_exceptions.get(user_language, user_language)
    
    browser = CustomBrowser(browser, user_language)
    
    yield browser
    
    time.sleep(5)
    print("\nquit browser..")
    browser.quit()