def test_language_add_btn(browser):
    # Data
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    language_button = {
        'ru': 'Добавить в корзину',
        'en-gb': 'Add to basket',
        'es': 'Añadir al carrito',
        'fr': 'Ajouter au panier'
    }
    add_to_cart_button_loc = '.btn-add-to-basket'
    site_language = browser.user_language
    button_text = language_button[site_language]

    # Arrange
    browser.get(link)

    # Act
    find_add_btn = browser.find_element_by_css_selector(add_to_cart_button_loc)

    # Assert
    assert button_text in find_add_btn.text, 'Button text does not match'
