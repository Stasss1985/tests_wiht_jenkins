from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import time
import random
from faker import Faker
from dateutil.relativedelta import relativedelta

fake = Faker()
fake_ru = Faker("ru_RU")


class PersonLoc():
    PERSON_HREF = (By.CSS_SELECTOR, 'a[href="/person"]')
    SUCCESS_BUTTON = (By.CSS_SELECTOR,
                      '[class="p-button p-component p-button-icon-only p-speeddial-button p-button-rounded p-button-success"]')
    # локаторы для добавления нового клиента
    BTN_ADD_NEW_CLIENT = (By.CLASS_NAME, 'p-button.p-component.w-100')
    BIRTH_PLACE = (By.ID, 'birthPlace')
    MANY_INPUT = (
        By.CSS_SELECTOR, '[class="p-autocomplete-input p-inputtext p-component"]')  # через этот локатор находим ФИО
    RADIOBUTTON_MAN = (By.ID, 'gender-0')
    BIRTH_DATE = (By.CSS_SELECTOR, '#birthDate')
    CITIZENSHIP_FIELD = (By.ID, 'citizenship')
    CITIZENSHIP_RUSSIA = (By.CSS_SELECTOR, '[aria-label="РОССИЯ"]')
    DOCUMENT_TYPE_END_CONTACT_TYPE_FIELD = (
        By.CSS_SELECTOR, '[class="p-dropdown-label p-inputtext p-dropdown-label-empty"]')
    DOCUMENT_TYPE_PASSPORT = (By.CSS_SELECTOR, '[aria-label="Паспорт"]')
    DOCUMENT_NUMBER_FIELD = (By.ID, 'number')
    DOCUMENT_DATE_OF_ISSUE = (By.CSS_SELECTOR, '#date')
    DEPARTMENT_CODE_FIELD = (By.ID, 'departmentCode')
    BY_WHOM_ISSUED_DOCUMENT = (By.CSS_SELECTOR, '[aria-posinset="1"]')
    ADDRESS_OF_REGISTRATION = (By.CSS_SELECTOR,
                               '#app > div.content-page > div > div > div.card > div > form > div.mt-4 > div:nth-child(11) > div > div.p-autocomplete.p-component.p-inputwrapper > input')
    # ADDRESS_OF_REGISTRATION - '//*[@id="app"]/div[2]/div/div/div[2]/div/form/div[1]/div[7]/div/div[1]/input'
    MODAL_WINDOW = (By.CLASS_NAME, 'p-dialog-content')
    # CONTACT_TYPE = (By.XPATH, '/html/body/div[4]/div/div[2]/form/div[1]/div[10]/div[1]/div/div[1]/div/div/div/span')
    OPEN_MOBILE_NUMBER_CHOSE = (By.CSS_SELECTOR, '[aria-owns="pv_id_69_list"]')
    MOBILE_NUMBER_CHOSE = (By.CSS_SELECTOR, '[aria-posinset="1"]')
    INPUT_MOBILE_NUMBER = (By.CSS_SELECTOR, '[id="value"]')
    GRIN_BUTTON_SUCCESS = (
        By.CSS_SELECTOR,
        '.p-button.p-component.p-button-icon-only.p-speeddial-button.p-button-rounded.p-button-success')
    # локаторы для проверки что новый клиент есть в поиске
    BUTTON_OPEN_FILTER = (By.CSS_SELECTOR,
                          '[class="p-button p-component p-button-icon-only p-speeddial-button p-button-rounded p-speeddial-rotate"]')
    NAME_FIELD_IN_FILTER = (By.ID, 'name')
    CLOSE_FILTER_BTN = (By.CSS_SELECTOR, '[class="p-sidebar-close p-sidebar-icon p-link"]')
    XREF_FIO_NEW_CLIENT = (By.CSS_SELECTOR, ".w-25 a")
    # локаторы для удаления нового клиента
    BUTTON_OUTLINED = (By.CSS_SELECTOR,
                       '[class="p-button p-component p-button-icon-only p-speeddial-button p-button-rounded p-speeddial-rotate p-button-secondary p-button-outlined"]')
    DELETE_CLIENT_BTN = (By.CSS_SELECTOR, '[class="p-speeddial-action-icon pi pi-trash"]')
    BTN_YES = (By.CSS_SELECTOR, '[aria-label="Да"]')
    FIELD_CHECK_DELETE_CLIENT = (By.CSS_SELECTOR, '[class="p-datatable-emptymessage"]')


class PersonPage(BasePage):
    loc = PersonLoc

    def navigate_to_person_page(self):
        time.sleep(4)
        self.click(self.loc.PERSON_HREF)
        time.sleep(2)
        self.wait_clickable(self.loc.SUCCESS_BUTTON)
        self.click(self.loc.SUCCESS_BUTTON)

    def add_new_client_in_person_page(self):
        def __init__(self):
            self.fio = None

        self.click(self.loc.BTN_ADD_NEW_CLIENT)
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
        # ввод места рождения
        self.send_keys(self.loc.BIRTH_PLACE, fake_ru.address())
        # ввод гражданства
        citizenship_field = self.find(self.loc.CITIZENSHIP_FIELD)
        citizenship_field.click()
        time.sleep(2)
        self.wait_clickable(self.loc.CITIZENSHIP_RUSSIA)
        self.click(self.loc.CITIZENSHIP_RUSSIA)
        # ввод тип документа
        time.sleep(3)
        document_type_end_contact_type_fields = self.find_all(self.loc.DOCUMENT_TYPE_END_CONTACT_TYPE_FIELD)
        DOCUMENT_TYPE_FIELD = document_type_end_contact_type_fields[0]
        self.wait_clickable(DOCUMENT_TYPE_FIELD)
        DOCUMENT_TYPE_FIELD.click()
        self.wait_clickable(self.loc.DOCUMENT_TYPE_PASSPORT)
        self.click(self.loc.DOCUMENT_TYPE_PASSPORT)
        # ввод ФИО
        many_inputs_find = self.find_all(self.loc.MANY_INPUT)
        SURNAME_INPUT = many_inputs_find[1]
        NAME_INPUT = many_inputs_find[2]
        PATRONYMIC_INPUT = many_inputs_find[3]
        surname = fake_ru.last_name_male()
        SURNAME_INPUT.send_keys(surname)
        name = fake_ru.first_name_male()
        NAME_INPUT.send_keys(name)
        # Список возможных отчеств
        patronymics = ['Александрович', 'Сергеевич', 'Дмитриевич', 'Николаевич', 'Иванович', 'Викторович']
        patronymic = random.choice(patronymics)
        PATRONYMIC_INPUT.send_keys(patronymic)
        self.fio = f'{surname} {name} {patronymic}'
        print(self.fio)
        time.sleep(2)
        self.scroll_by(600)
        time.sleep(2)
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
        document_number_field = self.find(self.loc.DOCUMENT_NUMBER_FIELD)
        document_number_field.click()
        document_number_field.send_keys(generate_doc_number)
        # ввод "код подразделения"
        department_code_field = self.find(self.loc.DEPARTMENT_CODE_FIELD)
        department_code_field.click()
        code_num = random.choices(['6020-032', '6020-013', '6020-034', '6020-033', '6020-010'])
        department_code_field.send_keys(code_num)
        # ввод "Кем выдан" документ
        self.find(self.loc.BY_WHOM_ISSUED_DOCUMENT)
        # ввод "Адрес регистрации"
        self.scroll_to_down()
        time.sleep(2)
        address_of_registration = self.find(self.loc.ADDRESS_OF_REGISTRATION)
        address_of_registration.send_keys(fake_ru.address())
        # ввод контактов - телефон, мейл
        CONTACT_TYPE = document_type_end_contact_type_fields[1]
        CONTACT_TYPE.click()
        time.sleep(2)
        mobile_number_chose = self.find(self.loc.MOBILE_NUMBER_CHOSE)
        mobile_number_chose.click()

        def generate_phone_number():
            # Генерируем 10 цифр
            number = ''.join(random.choices('123456789', k=10))
            return number

        # ввод телефона
        input_mobile_number_find_all = self.find_all(self.loc.INPUT_MOBILE_NUMBER)
        input_mobile_number = input_mobile_number_find_all[0]
        input_mobile_number.click()
        input_mobile_number.send_keys(generate_phone_number())
        # прикрепляем фото
        files_add = self.find((By.CSS_SELECTOR, 'input[type="file"]'))
        # прикрепляемый файл должен быть в папке, где храним код
        files_add.send_keys('C:/Users/user/karman_test/pages/lead_page/Снимок экрана 2024-11-02 123632.png')
        time.sleep(3)
        # Клик по зеленой кнопки ОК
        grin_button_success = self.find(self.loc.GRIN_BUTTON_SUCCESS)
        grin_button_success.click()
        time.sleep(5)

    def check_add_new_client_in_person_page(self):
        self.click(self.loc.BUTTON_OPEN_FILTER)
        name_field_in_filter = self.find(self.loc.NAME_FIELD_IN_FILTER)
        name_field_in_filter.click()
        name_field_in_filter.send_keys(self.fio)
        close_filter_btn = self.find(self.loc.CLOSE_FILTER_BTN)
        close_filter_btn.click()
        time.sleep(3)
        self.wait_for_element_visibility(self.loc.XREF_FIO_NEW_CLIENT)
        xref_fio_new_clients = self.find_all(self.loc.XREF_FIO_NEW_CLIENT)
        xref_fio_new_client = xref_fio_new_clients[0]
        # Проверяем ФИО в фильтре с ФИО добавленного клиента
        filter_fio = xref_fio_new_client.text
        assert self.fio in filter_fio, (
            f'ФИО отличается: добавленное - "{self.fio}", '
            f'созданное - "{filter_fio}", '
            f'или ФИО не был добавлен'
        )
        button_outlined = self.find(self.loc.BUTTON_OUTLINED)
        button_outlined.click()
        delete_client_btn = self.find(self.loc.DELETE_CLIENT_BTN)
        time.sleep(3)
        delete_client_btn.click()
        btn_yes = self.find(self.loc.BTN_YES)
        btn_yes.click()
        time.sleep(5)
        actual_text = self.get_text(self.loc.FIELD_CHECK_DELETE_CLIENT)
        print(f"Фактический текст: {actual_text}")  # Для отладки
        self.compare_text(self.loc.FIELD_CHECK_DELETE_CLIENT, "Нет данных")
        time.sleep(7)
