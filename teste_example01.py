import re
from playwright.sync_api import Page, Playwright, expect


def test_has_title(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://playwright.dev/")

    #Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")


    #Click the get started link.
    page.get_by_role("link", name="Get started").click()

    #Expects page to have a heading with the name of installation
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
