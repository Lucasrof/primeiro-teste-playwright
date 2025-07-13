import re
import time
from playwright.sync_api import Playwright, sync_playwright, expect


def teste_example03(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://demo.playwright.dev/todomvc/#/")
    page.get_by_role("heading", name="todos").click()
    page.get_by_role("heading", name="todos").click()
    page.get_by_role("textbox", name="What needs to be done?").click()
    page.get_by_role("textbox", name="What needs to be done?").fill("Tarefa 1")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("textbox", name="What needs to be done?").fill("Tarefa 2")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_role("textbox", name="What needs to be done?").fill("Tarefa 3")
    page.get_by_role("textbox", name="What needs to be done?").press("Enter")
    page.get_by_text("Tarefa 1").click()
    page.get_by_role("button", name="Delete").click()
    page.get_by_text("Tarefa 2").click()
    page.get_by_role("button", name="Delete").click()
    page.get_by_role("checkbox", name="Toggle Todo").check()
    page.get_by_role("button", name="Clear completed").click()
    context.tracing.stop(path= "trace.zip")
    context.close()
    browser.close()

with sync_playwright() as playwright:
    teste_example03(playwright)