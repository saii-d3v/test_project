import time

from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, url)
    page.open()
    # time.sleep(2)
    page.go_to_login_page()

def test_guest_should_see_login_link(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, url)
    page.open()
    # time.sleep(2)
    page.should_be_login_link()
