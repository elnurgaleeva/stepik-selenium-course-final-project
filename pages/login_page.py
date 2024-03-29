from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
	def should_be_login_page(self):
		self.should_be_login_url()
		self.should_be_login_form()
		self.should_be_register_form()

	def should_be_login_url(self):
		login_url = self.browser.current_url
		assert "/login" in login_url

	def should_be_login_form(self):
		assert self.is_element_present (*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

	def should_be_register_form(self):
		assert self.is_element_present (*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

	def register_new_user(self, email, password):
		email_input = self.browser.find_element(*LoginPageLocators.EMAIL)
		password_input = self.browser.find_element(*LoginPageLocators.PASSWORD)
		confirm_password_input = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)

		email_input.send_keys(email)
		password_input.send_keys(password)
		confirm_password_input.send_keys(password)

		confirm_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
		confirm_button.click()