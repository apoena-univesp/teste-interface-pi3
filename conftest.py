import pytest
from playwright.sync_api import Playwright


@pytest.fixture(scope="session")
def set_up(playwright: Playwright) -> None:
    # Assess - Given
    browser = playwright.chromium.launch(headless=False)  # , slow_mo=500)
    context = browser.new_context()
    # # Open new page
    page = context.new_page()
    page.goto("http://127.0.0.1:5000/")
    page.set_default_timeout(3000)

    yield page
    page.close()
