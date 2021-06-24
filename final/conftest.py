import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: ru (default), en-GB, es or fr")
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(language, browser_name):
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": language})
    if language == "ru" or language == "en-GB" or language == "es" or language == "fr":
        if browser_name == "chrome":
            print(f"\nstart chrome browser for test in {language} locale")
            browser = webdriver.Chrome(options=options)
        elif browser_name == "firefox":
            print(f"\nstart firefox browser for test in {language} locale")
            fp = webdriver.FirefoxProfile()
            fp.set_preference("intl.accept_languages", language)
            browser = webdriver.Firefox(firefox_profile=fp)
        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")
    else:
        raise pytest.UsageError("--language should be ru or en-gb")
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="session")
def language(request):
    return request.config.getoption("language")


@pytest.fixture(scope="session")
def browser_name(request):
    return request.config.getoption("browser")
