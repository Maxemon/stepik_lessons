import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en-GB",
                     help="Choose language: ru (default), en-GB, es, fr")


@pytest.fixture(scope="function")
def browser(language):
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": language})

    if language == "ru" or language == "en-GB" or language == "es" or language == "fr":
        print(f"\nstart chrome browser for test in {language} locale")
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be ru, en-GB, es, fr")

    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="session")
def language(request):
    return request.config.getoption("language")
