from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ContractCreateLoc():
    # Селекторы для выбора тарифа
    MENU_ITEM_BTN_OPEN = (By.CSS_SELECTOR,
                          '[class="p-button p-component p-button-icon-only p-speeddial-button p-button-rounded p-speeddial-rotate p-button-secondary"]')
    MENU_ITEM_BTN_CHOSE = (By.CSS_SELECTOR, '.p-speeddial-action-icon.pi.pi-user-plus')
    CONTRACT_TARIFF_ID_FIND = (By.ID, 'contractHasTariffId')
    CONTRACT_TARIFF_ID_CHOSE_1 = (By.CSS_SELECTOR, '[aria-posinset="1"]')
    CONTRACT_TARIFF_ID_CHOSE_2 = (By.CSS_SELECTOR, '[aria-posinset="2"]')
    CONTRACT_BUTTON = (By.CSS_SELECTOR, '[aria-label="Отправить"]')
    # Селекторы для контракта
    CREATE_OPERATION_BUTTON = (By.CSS_SELECTOR, '[aria-label="Создать операцию"]')
    CREATE_CONTRACT_BUTTON = (By.ID, 'btnCreateOperationInit_0')
    TEXT_SUMM = (By.CSS_SELECTOR, '[role = "spinbutton"]')
    SUCCESS_BUTTON = (By.CSS_SELECTOR,
                      '[class="p-button p-component p-button-icon-only p-speeddial-button p-button-rounded p-button-success"]')
    PRINT_DOCUMENT_BUTTON = (
        By.CSS_SELECTOR, '[class="p-button p-component p-button-icon-only p-speeddial-button p-button-rounded"]')
    PRINT_CHECK_BUTTON = (By.CSS_SELECTOR,
                          '[class="p-button p-component p-button-icon-only p-speeddial-button p-button-rounded p-button-warning"]')
    NEXT_BUTTON = (By.CSS_SELECTOR, '[aria-label="Далее"]')
    PRINT_CHECK_FINAL_BUTTON = (By.CSS_SELECTOR, '[aria-label="Напечатать чек"]')
    STATUS_PRINT_DOC_CHECK = (By.CSS_SELECTOR, "div.content-page li:nth-child(3) div.w-100 div")
    XREF_GO_TO_CONTRACT = (By.CSS_SELECTOR, ".container-fluid .w-100 a")


class ContractCreatePage(BasePage):
    loc = ContractCreateLoc

    def contract_tariff_chose_1(self):
        # Раскрываем круглые кнопки в нижнем правом углу
        menu_btn_ope = self.wait_clickable(self.loc.MENU_ITEM_BTN_OPEN)
        menu_btn_ope.click()
        # Выбираем "Создать лид и сделку" круглая кнопка в нижнем правом углу
        menu_item_btn_chose = self.wait_clickable(self.loc.MENU_ITEM_BTN_CHOSE)
        time.sleep(5)
        menu_item_btn_chose.click()
        # Открываем тарифы
        contract_tariff_id_find = self.find(self.loc.CONTRACT_TARIFF_ID_FIND)
        contract_tariff_id_find.click()
        # Выбираем первый тариф [0] "1"
        contract_tariff_id_chose_1 = self.wait_clickable(self.loc.CONTRACT_TARIFF_ID_CHOSE_1)
        contract_tariff_id_chose_1.click()
        # Находим и кликаем по кнопке отправить
        contract_button = self.find(self.loc.CONTRACT_BUTTON)
        contract_button.click()
        time.sleep(5)

    def contract_tariff_chose_2(self):
        # Раскрываем круглые кнопки в нижнем правом углу
        menu_btn_ope = self.wait_clickable(self.loc.MENU_ITEM_BTN_OPEN)
        menu_btn_ope.click()
        # Выбираем "Создать лид и сделку" круглая кнопка в нижнем правом углу
        time.sleep(2)
        menu_item_btn_chose = self.wait_clickable(self.loc.MENU_ITEM_BTN_CHOSE)
        menu_item_btn_chose.click()
        # Открываем тарифы
        contract_tariff_id_find = self.find(self.loc.CONTRACT_TARIFF_ID_FIND)
        contract_tariff_id_find.click()
        # Выбираем первый тариф [1] "2"
        contract_tariff_id_chose_2 = self.wait_clickable(self.loc.CONTRACT_TARIFF_ID_CHOSE_2)
        contract_tariff_id_chose_2.click()
        # Находим и кликаем по кнопке отправить
        contract_button = self.find(self.loc.CONTRACT_BUTTON)
        contract_button.click()
        time.sleep(5)

    def create_operation_create_contract(self):
        self.driver.execute_script("window.scrollBy(0, 1100);")
        # кликаем по кнопке "Создать операцию"
        time.sleep(5)
        btn_create_operation_click = self.wait_clickable(self.loc.CREATE_OPERATION_BUTTON)
        btn_create_operation_click.click()

        # выбираем "Создать договор потребительского займа"
        btn_create_operation = self.wait_clickable(self.loc.CREATE_CONTRACT_BUTTON)
        btn_create_operation.click()

        # подтверждаем "Договор купли продажи" с выбранным видом оплаты "Наличка"
        time.sleep(4)
        self.get_text(self.loc.TEXT_SUMM)
        btn_create_dogovor = self.wait_clickable(self.loc.SUCCESS_BUTTON)
        btn_create_dogovor.click()
        time.sleep(2)

    def print_document(self):
        original_window = self.driver.current_window_handle  # Сохраняем текущее окно

        # Клик по кнопке печати документа с явным ожиданием
        btn_print_dok = self.wait_clickable(self.loc.PRINT_DOCUMENT_BUTTON)
        btn_print_dok.click()

        # Ожидание появления нового окна (>= 2 окон)
        WebDriverWait(self.driver, 40).until(lambda d: len(d.window_handles) >= 2)

        # Находим новое окно
        new_window = [window for window in self.driver.window_handles if window != original_window][0]

        # Переключаемся на новое окно
        self.driver.switch_to.window(new_window)

        try:
            # Ожидание загрузки содержимого в новом окне
            WebDriverWait(self.driver, 40).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        finally:
            # Закрываем новое окно и возвращаемся в исходное
            self.driver.close()
            self.driver.switch_to.window(original_window)

    def print_check(self):
        # Клик распечатать чек
        self.click(self.loc.PRINT_CHECK_BUTTON)
        # Подтверждение суммы
        price = self.get_text((By.CSS_SELECTOR, '[class="text-success"]'))
        self.send_keys((By.CSS_SELECTOR, '[class="p-inputtext p-component p-inputnumber-input"]'), price)
        self.click(self.loc.NEXT_BUTTON)
        # Клик финальная распечатка чека
        self.click(self.loc.PRINT_CHECK_FINAL_BUTTON)
        # time.sleep(4)

        # Проверка статуса создания сделки "Завершено"

    def compare_text_status(self):
        # time.sleep(6)
        self.wait_for_element_to_disappear(self.loc.STATUS_PRINT_DOC_CHECK)
        time.sleep(2)
        actual_text = self.get_text(self.loc.STATUS_PRINT_DOC_CHECK)
        print(f"Фактический текст: {actual_text}")  # Для отладки
        self.compare_text(self.loc.STATUS_PRINT_DOC_CHECK, "Завершено")
        time.sleep(2)
        self.take_screenshot()

    def xref_go_to_contract(self):
        self.find(self.loc.XREF_GO_TO_CONTRACT)
        self.click(self.loc.XREF_GO_TO_CONTRACT)
        time.sleep(4)
