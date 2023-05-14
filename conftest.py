import time
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest
from pages.login_page import LoginPage
from pages.product_page import ProductPage


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language: ru, en-gb, es, fr")


@pytest.fixture(scope="function")
def browser(request):
    # В переменную user_language передается параметр из командной строки
    user_language = request.config.getoption("language")
    # Инициализируются опции браузера
    options = Options()
    # В опции вебдрайвера передаем параметр из командной строки
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    yield browser
    browser.quit()


# @pytest.fixture(scope="function")
# def setup(browser):
#     link = "http://selenium1py.pythonanywhere.com/accounts/login/"
#     page = LoginPage(browser, link)
#     page.open()
#     email = str(time.time()) + "@fakemail.org"
#     password = "test_password"
#     page.register_new_user(email, password)
#     page.should_be_authorized_user()


# @pytest.fixture(scope="function")
# def product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page = ProductPage(browser, link)
#     page.open()
#     return page