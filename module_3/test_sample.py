from selenium import webdriver

registration_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

email_register_input_loc = '[name="registration-email"]'
password_register_input_loc = '#id_registration-password1'
repeat_password_register_input_loc = '#id_registration-password2'
submit_registration_button_loc = '[name="registration_submit"]'


def test_registration_new_user_with_valid_credentials():
    try:
        # Data
        valid_email = "test261521@gmail.com"
        valid_password = "Newpassword19283746"
        success_registration_link = "http://selenium1py.pythonanywhere.com/ru/"
        success_registration_notification_loc = ".alertinner.wicon"
        success_registration_notification_text = "Спасибо за регистрацию!"

        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(registration_page_link)

        # Act
        email_input = browser.find_element_by_css_selector(email_register_input_loc)
        email_input.clear()
        email_input.send_keys(valid_email)

        password_input = browser.find_element_by_css_selector(password_register_input_loc)
        password_input.clear()
        password_input.send_keys(valid_password)

        repeat_password_input = browser.find_element_by_css_selector(repeat_password_register_input_loc)
        repeat_password_input.clear()
        repeat_password_input.send_keys(valid_password)

        browser.find_element_by_css_selector(submit_registration_button_loc).click()

        # Assert
        after_register_link = browser.current_url
        assert success_registration_link == after_register_link, \
            "Registration failed. Success registration links did not match"

        check_notification = browser.find_element_by_css_selector(success_registration_notification_loc).text
        assert check_notification == success_registration_notification_text, \
            "success notification doesn't match or missing"

    finally:
        browser.quit()


test_registration_new_user_with_valid_credentials()
