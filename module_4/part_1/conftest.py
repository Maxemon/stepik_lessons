import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru",
                     help="Choose language: ru (default) or en-gb")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": language})
    if language == "ru" or language == "en-gb":
        print(f"\nstart chrome browser for test in {language} locale")
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be ru or en-gb")
    yield browser
    print("\nquit browser..")
    browser.quit()
