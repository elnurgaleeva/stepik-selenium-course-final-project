from selenium.webdriver.common.by import By

class BasePageLocators(object):
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
	LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
	BASKET_BUTTON = (By.LINK_TEXT, "View basket")
	USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators(object):
	pass
	
class LoginPageLocators(object):
	LOGIN_FORM = (By.ID, "login_form")
	REGISTER_FORM = (By.ID, "register_form")
	EMAIL = (By.ID, "id_registration-email")
	PASSWORD = (By.ID, "id_registration-password1")
	CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
	REGISTER_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators(object):
	ADD_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
	MESSAGE_BASKET_ITEM = (By.CSS_SELECTOR, "div.alertinner ")
	MESSAGE_BASKET_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
	ITEM_NAME = (By.CSS_SELECTOR, "div.product_main h1")
	ITEM_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")

class BasketPageLocators(object):
	BASKET_EMPTY_TEXT = (By.ID, "content_inner")
	BASKET_ITEM = (By.CLASS_NAME, "basket-items")
