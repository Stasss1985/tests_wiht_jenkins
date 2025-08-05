from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.lead_page.contract_сreate_page import ContractCreateLoc
import time


class ContractLoc():
    BTN_CREATE_OPERATIONS = (By.CSS_SELECTOR, '[aria-controls = "btnCreateOperation"]')
    BTN_CREATE_OPERATION_BUY_BACK = (By.CSS_SELECTOR, '[aria-label="Выкуп"]')
    BTN_PAYMENT_METHOD = (By.ID, 'paymentMethod')
    BTN_PAYMENT_METHOD_CACHE = (By.CSS_SELECTOR, '[aria-label="Наличные"]')


class DoOperationContractPage(BasePage):
    loc = ContractLoc
    locc = ContractCreateLoc

    def contract_create_operation_buy_back(self):
        # Прокрутка до кнопки создать операцию
        time.sleep(2)
        # self.scroll_to_element(self.loc.BTN_CREATE_OPERATIONS)
        self.driver.execute_script("window.scrollBy(0, 1100);")
        time.sleep(3)
        # Поиск и клик по кнопки "Создать операцию"
        self.find(self.loc.BTN_CREATE_OPERATIONS)
        self.click(self.loc.BTN_CREATE_OPERATIONS)
        # Выбор "Выкуп"
        self.find(self.loc.BTN_CREATE_OPERATION_BUY_BACK)
        self.click(self.loc.BTN_CREATE_OPERATION_BUY_BACK)
        # Открытие окна способ оплаты
        time.sleep(4)
        btn_payment_method = self.find(self.loc.BTN_PAYMENT_METHOD)
        btn_payment_method.click()
        time.sleep(2)
        # Выбор тип оплаты "Наличные"
        self.find(self.loc.BTN_PAYMENT_METHOD_CACHE)
        self.click(self.loc.BTN_PAYMENT_METHOD_CACHE)
        # Клик на зеленую кнопочку (подтердить)
        self.find(self.locc.SUCCESS_BUTTON)
        self.click(self.locc.SUCCESS_BUTTON)
        # Клик распечатать чек
