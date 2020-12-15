from .pages.product_page import ProductPage


class TestProductPage:
    @pytest.mark.parametrize('link', "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear")

    def test_guest_can_add_product_to_basket(self, browser, link):
        product_name = "The shellcoder's handbook"
        template = "{} has been added to your basket."
        expected_product_price = "£9.99"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.check_add_to_basket_notification(product_name, template)
        page.check_product_and_basket_price(expected_product_price)
