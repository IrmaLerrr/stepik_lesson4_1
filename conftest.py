import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                 help="Choose browser: chrome, edge or firefox")
    parser.addoption('--language', action='store', default="en",
                 help="Choose language")


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
    
    yield browser
    
    time.sleep(15)
    print("\nquit browser..")
    browser.quit()