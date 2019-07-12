from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
	def should_be_empty_basket(self):
		assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_TEXT), (
			"Basket is not empty")

	def should_not_be_basket_items(self):
		assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), \
			"Item is presented in basket, but should not be"

