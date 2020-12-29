from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    SUCCESS_MESSAGE_NOTIFICATION = (By.CSS_SELECTOR, ".alert:nth-child(1) .alertinner")
