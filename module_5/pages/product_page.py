from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        basket_btn.click()

    def check_add_to_basket_notification(self, expected_product_name, expected_notification_template):
        expected_notification_text = expected_notification_template.format(expected_product_name)
        actual_notification_text = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_NOTIFICATION).text
        print("Actual product name is " + actual_notification_text,
              "Expected product name is " + expected_notification_text)
        assert actual_notification_text == expected_notification_text

    def check_product_and_basket_price(self, expected_product_price):
        actual_product_price = self.browser.find_element(By.CSS_SELECTOR, ".alertinner>p>strong").text
        print("Actual product price is " + actual_product_price, "Expected product price is " + expected_product_price)
        assert actual_product_price == expected_product_price
