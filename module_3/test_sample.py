from selenium import webdriver
import time

registration_page_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"

email_register_input = '[name="registration-email"]'
password_register_input = '#id_registration-password1'
repeat_password_register_input = '#id_registration-password2'
submit_registration_button = '[name="registration_submit"]'


def test_registration_new_user_with_valid_credentials():
    try:
        # Data
        valid_email = "test21131@gmail.com"
        valid_password = "Newpassword19283746"
        success_registration_link = "http://selenium1py.pythonanywhere.com/ru/"

        # Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(registration_page_link)

        # Act
        search_email_register_input = browser.find_element_by_css_selector(email_register_input)
        search_email_register_input.clear()
        search_email_register_input.send_keys(valid_email)

        search_password_register_input = browser.find_element_by_css_selector(password_register_input)
        search_password_register_input.clear()
        search_password_register_input.send_keys(valid_password)

        search_repeat_password_register_input = browser.find_element_by_css_selector(repeat_password_register_input)
        search_repeat_password_register_input.clear()
        search_repeat_password_register_input.send_keys(valid_password)

        browser.find_element_by_css_selector(submit_registration_button).click()

        # Assert
        after_register_link = browser.current_url
        assert success_registration_link == after_register_link, \
            "Registration failed. Success registration links did not match"

    finally:
        time.sleep(4)
        browser.quit()


test_registration_new_user_with_valid_credentials()

# 1) Ставлю на то, что с блоком Act беда, ведь в нем ни разу ни 1-3 строчки, но-подругому тут никак.
# Хоть на еще более атомарные тесты дели, которые будут проверять такие мелочи,
# что для каждого инпут поля текст введен и отображается корретно и это и есть тест

# 2) Переменные, что были использованы как общие (до теста) порой созвучны с теми, что внутри теста
# с отличием в том, что переменные внутри теста содержат глагол, который выполянется над существительным переменной до теста.
# надеюсь это не ошибка

# 3) Возможно assert нужно было основывать на появившемся уведомлении об успешной регистрации, но моя логика
# заключается в том, что если бы регистрация не была бы успешной, редирект на главную страницу сайта не произошел бы.
# А знать, что менее надежно и более вероятно - измененный текст уведомления или иной редирект/замена пути ссылки, я пока не знаю
