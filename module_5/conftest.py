import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-GB', help="Choose your language: 'ru', 'en-GB', 'es', 'fr'")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")

    if language in ['ru', 'en-GB', 'es', 'fr']:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        print('\nStart...')
        browser.implicitly_wait(10)
        browser.user_language = language
    else:
        raise pytest.UsageError("Browser language should be 'ru', 'en-GB', 'es' or 'fr'")
    yield browser
    print("\nquit browser..")
    browser.quit()
