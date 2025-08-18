from selenium.webdriver.support.wait import WebDriverWait
from utils import project_ec
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AdminLoc():
    EMAIL_FILD = (By.ID, 'email')
    PASSWORD_FILD = (By.ID, 'password')
    BUTTON = (By.CLASS_NAME, 'btn.btn-primary')
    ERROR_ALERT = (By.XPATH, '//*[@id="app"]/div/div/div/div/div/div/div/div[2]/form/div[2]/small')
    CHANGE_BUTTON = (By.CLASS_NAME, 'p-button.p-component.mt-2.p-button-warning')


class AdminLogin(BasePage):
    loc = AdminLoc
    page_url = None

    def fill_login_form_good(self, login, password):
        self.wait_clickable(self.loc.BUTTON)
        # Находим элементы
        email_field = self.find(self.loc.EMAIL_FILD)
        password_field = self.find(self.loc.PASSWORD_FILD)
        # Заполняем форму
        email_field.send_keys(login)
        password_field.send_keys(password)
        self.click(self.loc.BUTTON)
        self.wait_clickable(self.loc.CHANGE_BUTTON)

    def fill_login_form(self, login, password):
        self.wait_clickable(self.loc.BUTTON)
        # Находим элементы
        email_field = self.find(self.loc.EMAIL_FILD)
        password_field = self.find(self.loc.PASSWORD_FILD)
        # Заполняем форму
        email_field.send_keys(login)
        password_field.send_keys(password)
        self.click(self.loc.BUTTON)

    def check_error_alert_is(self, expected_error):
        WebDriverWait(self.driver, 5).until(project_ec.text_is_not_empty_in_element(self.loc.ERROR_ALERT))
        error_alert = self.find(self.loc.ERROR_ALERT)
        error_alert_text = error_alert.text
        assert error_alert_text == expected_error, f"Ожидалось сообщение об ошибке '{expected_error}', но получено '{error_alert_text}'"
