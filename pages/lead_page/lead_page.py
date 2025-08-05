from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from pages.lead_page.contract_сreate_page import ContractCreateLoc
import random
from faker import Faker
from dateutil.relativedelta import relativedelta

fake = Faker()
fake_ru = Faker("ru_RU")


class LeadLoc():
    CHANGE_BUTTON = (By.CLASS_NAME, 'p-button.p-component.mt-2.p-button-warning')
    INPUT_FIELD = (By.CLASS_NAME, 'p-tree-filter-container')
    INPUT_FIELD_1_MAYA = (By.CSS_SELECTOR, '[aria-label="Краснодар-1-го Мая ЛОМБАРД (Карман)"]')
    INPUT_FIELD_KRASNIX_PARTISAN = (By.CSS_SELECTOR, '[aria-label="Краснодар-Красных Партизан ЛОМБАРД (Карман)"]')
    LEAD_HREF = (By.CSS_SELECTOR, 'a[href="/lead"]')
    LEAD_CREATE_BUTTON = (By.CSS_SELECTOR, 'a[href="/lead/create"]')
    COUNTERAGENT_INPUT = (By.ID, 'counteragentId')
    COUNTERAGENT_SEARCH = (By.CSS_SELECTOR, '[aria-controls="counteragentId_list"]')
    # COUNTERAGENT_SELECT = (By.CSS_SELECTOR, '[aria-label="Кривко С.Т."]')
    COUNTERAGENT_SELECT_0 = (By.ID, 'counteragentId_0')
    COUNTERAGENT_SELECT_1 = (By.ID, 'counteragentId_1')
    COUNTERAGENT_SELECT_2 = (By.ID, 'counteragentId_2')
    CHECK_BUTTON = (By.CSS_SELECTOR, '[aria-label="Проверить"]')
    PASSPORT_CHECKBOXES = (By.CLASS_NAME, 'p-checkbox-box')
    PASSPORT_CONFIRM = (By.CSS_SELECTOR, '[aria-label="Далее"]')
    SOURCE_ID_CHOSE = (By.ID, 'sourceId')
    SOURCE_ID_FIND = (By.CLASS_NAME, 'p-dropdown-item')
    # локаторы для кассы
    BTN_CASH_REGISTER = (By.CLASS_NAME, 'p-blockui-container.dropdown-toggle.arrow-none')
    BTN_ADD_CASH_IN_REGISTER = (By.CSS_SELECTOR, 'a[href="/kkm/depositing/transaction"]')
    SENT_AMOUNT_CASH = (By.CSS_SELECTOR, '#amount > input')
    CASH_ADOPTED_FROM = (By.ID, 'fundId')
    PERSON_CASH_ADOPTED_FROM = (By.CLASS_NAME, 'p-dropdown-filter.p-inputtext.p-component')
    CHOSE_PERSON_CASH_ADOPTED_FROM = (By.CSS_SELECTOR, '[aria-label="Кривов Алексей Олегович"]')
    REASON_ID_FIELD = (By.ID, 'reasonId')
    REASON_ID_CHOSE_ACTIVATE = (By.CLASS_NAME, 'p-dropdown-filter.p-inputtext.p-component')
    REASON_ID_CHOSE = (
        By.CSS_SELECTOR, '[aria-label="Внутреннее перемещение денежных средств (между подразделениями)"]')
    # локаторы для добавления нового клиента в лиде
    BTN_ADD_NEW_CLIENT = (By.CLASS_NAME, 'p-button.p-component.w-100')
    BIRTH_PLACE = (By.ID, 'birthPlace')
    SURNAME_INPUT = (By.XPATH, "/html/body/div[4]/div/div[2]/form/div[1]/div[1]/div[1]/div/div/div[1]/input")
    NAME_INPUT = (By.XPATH, "/html/body/div[4]/div/div[2]/form/div[1]/div[1]/div[2]/div/div/div[1]/input")
    PATRONYMIC_INPUT = (By.XPATH, "/html/body/div[4]/div/div[2]/form/div[1]/div[1]/div[3]/div/div/div[1]/input")
    RADIOBUTTON_MAN = (By.ID, 'gender-0')
    BIRTH_DATE = (By.CSS_SELECTOR, '#birthDate')
    CITIZENSHIP_FIELD = (By.ID, 'citizenship')
    CITIZENSHIP_RUSSIA = (By.CSS_SELECTOR, '[aria-label="РОССИЯ"]')
    DOCUMENT_TYPE_FIELD = (
        By.XPATH, "/html/body/div[4]/div/div[2]/form/div[1]/div[5]/div[1]/div/div[1]/div/div/div/span")
    DOCUMENT_TYPE_PASSPORT = (By.CSS_SELECTOR, '[aria-label="Паспорт"]')
    DOCUMENT_NUMBER_FIELD = (By.ID, 'number')
    DOCUMENT_DATE_OF_ISSUE = (By.CSS_SELECTOR, '#date')
    DEPARTMENT_CODE_FIELD = (By.ID, 'departmentCode')
    BY_WHOM_ISSUED_DOCUMENT = (By.CSS_SELECTOR, '[aria-posinset="1"]')
    ADDRESS_OF_REGISTRATION = (By.XPATH, '/html/body/div[4]/div/div[2]/form/div[1]/div[7]/div/div[1]/input')
    MODAL_WINDOW = (By.CLASS_NAME, 'p-dialog-content')
    CONTACT_TYPE = (By.XPATH, '/html/body/div[4]/div/div[2]/form/div[1]/div[10]/div[1]/div/div[1]/div/div/div/span')
    OPEN_MOBILE_NUMBER_CHOSE = (By.CSS_SELECTOR, '[aria-owns="pv_id_69_list"]')
    MOBILE_NUMBER_CHOSE = (By.CSS_SELECTOR, '[aria-posinset="1"]')
    INPUT_MOBILE_NUMBER = (By.XPATH, '/html/body/div[4]/div/div[2]/form/div[1]/div[10]/div[1]/div/div[2]/div/div/input')
    SAVE_BUTTON = (By.CSS_SELECTOR, '[aria-label="Сохранить"]')


class LeadPage(BasePage):
    loc = LeadLoc
    locc = ContractCreateLoc

    def change_office_1_maya(self):
        self.click(self.loc.CHANGE_BUTTON)
        self.click(self.loc.INPUT_FIELD)
        self.click(self.loc.INPUT_FIELD_1_MAYA)
        time.sleep(3)

    def change_office_krasnix_partisan(self):
        self.click(self.loc.CHANGE_BUTTON)
        self.click(self.loc.INPUT_FIELD)
        self.click(self.loc.INPUT_FIELD_KRASNIX_PARTISAN)
        time.sleep(3)

    # функция - добавить наличку в кассовый аппарат
    def add_cash_in_cash_register(self, summ):
        time.sleep(3)
        self.click(self.loc.BTN_CASH_REGISTER)
        self.click(self.loc.BTN_ADD_CASH_IN_REGISTER)
        self.send_keys(self.loc.SENT_AMOUNT_CASH, summ)
        # Активация поля Принято от
        cash_adopted_from = self.find(self.loc.CASH_ADOPTED_FROM)
        cash_adopted_from.click()
        # Ввод ФИО от кого принято
        person_cash_adopted_from = self.find(self.loc.PERSON_CASH_ADOPTED_FROM)
        person_cash_adopted_from.click()
        person_cash_adopted_from.send_keys('Кривов Алексей Олегович')
        self.click(self.loc.CHOSE_PERSON_CASH_ADOPTED_FROM)
        # Активация поля Основания для пополнения
        reason_id_field = self.find(self.loc.REASON_ID_FIELD)
        reason_id_field.click()
        # Выбор Внутреннее перемещение денежных средств (между подразделениями)
        reason_id_chose = self.find(self.loc.REASON_ID_CHOSE_ACTIVATE)
        reason_id_chose.click()
        reason_id_chose.send_keys('Внутреннее перемещение денежных средств (между подразделениями)')
        self.click(self.loc.REASON_ID_CHOSE)
        # Клик по зеленой кнопки, подтвердить
        success_button = self.find(self.locc.SUCCESS_BUTTON)
        success_button.click()
        time.sleep(2)
        # Сохранение текущего окна:
        self.wait_clickable(self.locc.PRINT_DOCUMENT_BUTTON)
        # Клик по кнопки печать документа
        time.sleep(3)
        btn_print_dok = self.wait_clickable(self.locc.PRINT_DOCUMENT_BUTTON)
        btn_print_dok.click()
        WebDriverWait(self.driver, 20).until(EC.number_of_windows_to_be(2))
        # Поиск всех окон
        windows = self.driver.window_handles
        # Переключение на последнее из тех, что открылось
        self.driver.switch_to.window(windows[-1])
        time.sleep(5)
        # Закрытие окна
        self.driver.close()
        # Переключение на 1 ое окно
        time.sleep(5)
        self.driver.switch_to.window(windows[0])
        # Клик распечатать чек
        self.click(self.locc.PRINT_CHECK_BUTTON)
        # # Еще раз после ожидания печать чека
        # self.click(self.locc.NEXT_BUTTON)
        # Клик финальная распечатка чека
        self.click(self.locc.PRINT_CHECK_FINAL_BUTTON)

    def navigate_to_lead_create(self):
        time.sleep(2)
        self.click(self.loc.LEAD_HREF)
        self.click(self.loc.LEAD_CREATE_BUTTON)
        self.wait_clickable(self.loc.BTN_ADD_NEW_CLIENT)

    def chose_old_client_to_lead(self):
        self.click(self.loc.COUNTERAGENT_INPUT)
        # Список клиентов
        clients = ['А', 'Б', 'В', 'Г', 'Д', 'Ж', 'З', 'И', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С']
        # Выбор случайного клиента
        random_client = random.choice(clients)
        # Отправка случайного имени в поле поиска
        self.send_keys(self.loc.COUNTERAGENT_SEARCH, random_client)
        # Выбор случайного локатора
        counteragent_locator = random.choice(
            [self.loc.COUNTERAGENT_SELECT_0, self.loc.COUNTERAGENT_SELECT_1, self.loc.COUNTERAGENT_SELECT_2])
        time.sleep(5)  # Рекомендуется заменить на WebDriverWait для лучшей практики
        # Найти элемент по локатору и кликнуть на него
        COUNTERAGENT_SELECT = self.driver.find_element(*counteragent_locator)  # Используем распаковку кортежа
        COUNTERAGENT_SELECT.click()
        self.wait_clickable(self.loc.CHECK_BUTTON)
        self.click(self.loc.CHECK_BUTTON)
        checkboxes = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.loc.PASSPORT_CHECKBOXES)
        )
        for checkbox in checkboxes[:5]:
            checkbox.click()
        print(f"Найдено чекбоксов: {len(checkboxes)}")
        self.click(self.loc.PASSPORT_CONFIRM)
        time.sleep(2)
        self.driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(2)
        source_chose = self.find(self.loc.SOURCE_ID_CHOSE)
        source_chose.click()
        # выбираем источник 2Gis
        source_find = self.driver.find_elements(*self.loc.SOURCE_ID_FIND)
        (source_find[0]).click()

    def add_new_client_to_lead(self):
        self.click(self.loc.BTN_ADD_NEW_CLIENT)
        # ввод места рождения
        self.send_keys(self.loc.BIRTH_PLACE, fake_ru.address())
        # выбор пола мужской
        self.click(self.loc.RADIOBUTTON_MAN)
        # Ожидание и клик по полю даты рождения
        birth_date_field = self.wait_clickable(self.loc.BIRTH_DATE)
        birth_date_field.click()
        # Генерируем дату рождения
        date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=65)
        # Преобразуем дату в нужный формат
        formatted_date_of_birth = date_of_birth.strftime('%d.%m.%Y')
        # Вводим дату рождения
        self.send_keys(self.loc.BIRTH_DATE, formatted_date_of_birth)
        # ввод гражданства
        citizenship_field = self.find(self.loc.CITIZENSHIP_FIELD)
        citizenship_field.click()
        time.sleep(2)
        self.wait_clickable(self.loc.CITIZENSHIP_RUSSIA)
        self.click(self.loc.CITIZENSHIP_RUSSIA)
        # ввод тип документа
        time.sleep(3)
        document_type_field = self.find(self.loc.DOCUMENT_TYPE_FIELD)
        document_type_field.click()
        self.wait_clickable(self.loc.DOCUMENT_TYPE_PASSPORT)
        self.click(self.loc.DOCUMENT_TYPE_PASSPORT)
        # ввод ФИО
        # Список возможных отчеств
        patronymics = ['Александрович', 'Сергеевич', 'Дмитриевич', 'Николаевич', 'Иванович', 'Викторович']
        patronymic = random.choice(patronymics)
        self.send_keys(self.loc.SURNAME_INPUT, fake_ru.last_name_male())
        self.send_keys(self.loc.NAME_INPUT, fake_ru.first_name_male())
        self.send_keys(self.loc.PATRONYMIC_INPUT, patronymic)
        # ввод даты выдачи документа
        # Добавляем 18 лет к дате рождения
        date_doc = date_of_birth + relativedelta(years=18)
        # Преобразуем новую дату в нужный формат
        formatted_date_doc = date_doc.strftime('%d.%m.%Y')
        document_date_of_issue = self.wait_clickable(self.loc.DOCUMENT_DATE_OF_ISSUE)
        document_date_of_issue.click()
        self.send_keys(self.loc.DOCUMENT_DATE_OF_ISSUE, formatted_date_doc)

        # ввод номер документа
        def generate_custom_number():
            # Генерируем оставшиеся 6 цифр
            number = ''.join(random.choices('0123456789', k=6))
            return number

        prefix = '6020'
        generate_doc_number = f'{prefix}{generate_custom_number()}'
        print(generate_doc_number)
        document_number_field = self.find(self.loc.DOCUMENT_NUMBER_FIELD)
        document_number_field.click()
        document_number_field.send_keys(generate_doc_number)
        # Прокрутка внутри всплывающего окна
        self.scroll_in_modal(self.loc.MODAL_WINDOW)
        time.sleep(2)
        # ввод "код подразделения"
        department_code_field = self.find(self.loc.DEPARTMENT_CODE_FIELD)
        department_code_field.click()
        code_num = random.choices(['6020-032', '6020-013', '6020-034', '6020-033', '6020-010'])
        department_code_field.send_keys(code_num)
        # ввод "Кем выдан" документ
        self.find(self.loc.BY_WHOM_ISSUED_DOCUMENT)
        # ввод "Адрес регистрации"
        time.sleep(2)
        address_of_registration = self.find(self.loc.ADDRESS_OF_REGISTRATION)
        address_of_registration.click()
        address_of_registration.send_keys(fake_ru.address())
        # ввод контактов - телефон, мейл
        self.scroll_in_modal(self.loc.MODAL_WINDOW)
        contact_type = self.find(self.loc.CONTACT_TYPE)
        contact_type.click()
        time.sleep(2)
        mobile_number_chose = self.find(self.loc.MOBILE_NUMBER_CHOSE)
        mobile_number_chose.click()

        def generate_phone_number():
            # Генерируем 10 цифр
            number = ''.join(random.choices('123456789', k=10))
            return number

        # ввод телефона
        input_mobile_number = self.find(self.loc.INPUT_MOBILE_NUMBER)
        input_mobile_number.click()
        input_mobile_number.send_keys(generate_phone_number())
        # прикрепляем фото
        files_add = self.find((By.CSS_SELECTOR, 'input[type="file"]'))
        # прикрепляемый файл должен быть в папке где храним код
        files_add.send_keys('C:/Users/user/karman_test/pages/lead_page/Снимок экрана 2024-11-02 123632.png')
        time.sleep(3)
        # Клик по кнопки "Сохранить"
        save_button = self.wait_for_element_visibility(self.loc.SAVE_BUTTON)
        # Теперь ждем, пока элемент станет кликабельным
        self.wait_clickable(save_button)
        # Кликаем по кнопки сохранить
        save_button.click()
        time.sleep(5)
        # Прокрутка до поля "Источник"
        self.driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(2)
        source_chose = self.find(self.loc.SOURCE_ID_CHOSE)
        source_chose.click()
        # выбираем источник 2Gis
        source_find = self.driver.find_elements(*self.loc.SOURCE_ID_FIND)
        (source_find[0]).click()
