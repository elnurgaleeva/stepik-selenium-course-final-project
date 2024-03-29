from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
import pytest
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
								])
def test_guest_can_add_product_to_cart(browser, link):
	page = ProductPage(browser, link)
	page.open()
	page.add_to_basket()
	page.solve_quiz_and_get_code()
	page.should_be_message_basket_item()
	page.should_be_message_basket_price()

def test_guest_cant_see_success_message(browser):
	page = ProductPage(browser, link)
	page.open()
	page.should_not_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
	page = ProductPage(browser, link)
	page.open()
	page.go_to_login_page()
	login_page = LoginPage(browser, browser.current_url)
	login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
	page = ProductPage(browser, link)
	page.open()
	page.go_to_basket_page()
	basket_page = BasketPage(browser, browser.current_url)
	basket_page.should_be_empty_basket()
	basket_page.should_not_be_basket_items()

@pytest.mark.registered_user
class TestUserAddToCartFromProductPage():
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

	@pytest.fixture(scope="function", autouse=True)
	def setup(self, browser):
		register_link = "http://selenium1py.pythonanywhere.com/accounts/login/"
		register_page = LoginPage(browser, register_link)
		register_page.open()
		email = str(time.time()) + "@fakemail.org"
		password = "123test123"
		register_page.register_new_user(email, password)
		register_page.should_be_authorized_user()

	@pytest.mark.need_review
	def test_user_can_add_product_to_cart(self, browser):
		page = ProductPage(browser, link)
		page.open()
		page.add_to_basket()
		page.should_be_message_basket_item()
		page.should_be_message_basket_price()

	def test_user_cant_see_success_message(self, browser):
		page = ProductPage(browser, link)
		page.open()
		page.should_not_be_success_message()
