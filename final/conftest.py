import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: ru (default) or en-gb")
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": language})
    if language == "ru" or language == "en-gb":
        print(f"\nstart chrome browser for test in {language} locale")
    else:
        raise pytest.UsageError("--language should be ru or en-gb")
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()