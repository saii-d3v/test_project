import time

from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, url)
    page.open()
    time.sleep(2)
    page.go_to_login_page()
