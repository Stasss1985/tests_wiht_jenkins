from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import random
import time


class ShopLoc():
    # локаторы для фильтра для продажи товаров
    SHOP_HREF = (By.CSS_SELECTOR, 'a[href="/product/store"]')
    BUTTON_OPEN_FILTER = (
        By.CLASS_NAME, 'p-button.p-component.p-button-icon-only.p-speeddial-button.p-button-rounded.p-speeddial-rotate')
    CATEGORY_OFFICE_STATUS_FIELDS_OPEN = (By.CLASS_NAME, 'p-multiselect.p-component.p-inputwrapper')
    CATEGORY_FIELD_CHOSE = (By.CLASS_NAME, 'p-multiselect-filter.p-inputtext.p-component')
    CATEGORY_TECHNIQUE_CHOSE = (By.CSS_SELECTOR, '[aria-label="  Техника"]')
    FIELD_CLOSE = (By.CLASS_NAME, 'p-multiselect-close.p-link')
    # локаторы выбора офиса в фильтре
    OFFICE_FIELD_OPEN = (By.XPATH, '/html/body/div[2]/div/div[2]/div[7]/div/div/div[2]/div')
    OFFICE_FIELD_CHOSE = (By.CLASS_NAME, 'p-multiselect-filter.p-inputtext.p-component')
    OFFICE_CHOSE = (By.CSS_SELECTOR, '[aria-label="Краснодар-1-го Мая ЛОМБАРД (Карман)"]')
    # локаторы статуса в фильтре
    STATUS_FIELD_OPEN = (By.CSS_SELECTOR, '.p-sidebar-content > div:nth-child(10) > div > div')
    STATUS_FIELD_CHOSE = (By.CLASS_NAME, 'p-multiselect-filter.p-inputtext.p-component')
    STATUS_CHOSE = (By.CSS_SELECTOR, '[aria-label="На витрине"]')
    FILTER_CLOSE = (By.CLASS_NAME, 'p-sidebar-close.p-sidebar-icon.p-link')
    # локаторы для продажи в магазине
    BTN_OPEN_MENU_IN_LINE = (By.CLASS_NAME,
                             'p-button.p-component.p-button-icon-only.p-speeddial-button.p-button-rounded.p-speeddial-rotate.p-button-secondary.p-button-outlined')
    BTN_CHOSE_SALE_IN_MENU = (By.CLASS_NAME, 'p-speeddial-action-icon.pi.pi-money-bill')
    COUNTERAGENT_INPUT = (By.ID, 'counteragentId')
    COUNTERAGENT_SEARCH = (By.CSS_SELECTOR, '[aria-controls="counteragentId_list"]')
    COUNTERAGENT_SELECT_0 = (By.ID, 'counteragentId_0')
    COUNTERAGENT_SELECT_1 = (By.ID, 'counteragentId_1')
    COUNTERAGENT_SELECT_2 = (By.ID, 'counteragentId_2')
    SOURCE_ID_CHOSE = (By.ID, 'sourceId')
    SOURCE_ID_FIND = (By.CLASS_NAME, 'p-dropdown-item')
    # SUCCESS_BUTTON = (By.CSS_SELECTOR, '.p-button.p-component.p-button-icon-only.p-speeddial-button.p-button-rounded.p-button-success > button')
    SUCCESS_BUTTON = (By.XPATH, '//*[@id="app"]/div[2]/div/div/form/div[5]/span/button')
    XREF_GO_TO_PRODUCT_ID = (By.CSS_SELECTOR, ".container-fluid .w-100 a")
    PRODUCT_STATUS_IN_PRODUCT_ID = (By.CLASS_NAME, "product-badge.status-0")
    PRODUCT_CONDITION_IN_PRODUCT_ID = (By.CSS_SELECTOR, "li:nth-child(7) > div.w-100")


class ShopSalePage(BasePage):
    loc = ShopLoc

    def navigate_to_shop_page(self):
        time.sleep(2)
        self.click(self.loc.SHOP_HREF)

    def filter_for_sale_product_in_shop(self):
        self.click(self.loc.BUTTON_OPEN_FILTER)
        # Выбираем категорию - техника
        category_office_status_fields_open = self.find_all(self.loc.CATEGORY_OFFICE_STATUS_FIELDS_OPEN)
        CATEGORY_FIELD_OPEN = category_office_status_fields_open[0]
        OFFICE_FIELD_OPEN = category_office_status_fields_open[1]
        STATUS_FIELD_OPEN = category_office_status_fields_open[2]
        time.sleep(2)
        CATEGORY_FIELD_OPEN.click()
        self.send_keys(self.loc.CATEGORY_FIELD_CHOSE, 'техника')
        self.click(self.loc.CATEGORY_TECHNIQUE_CHOSE)
        self.click(self.loc.FIELD_CLOSE)
        # Выбираем офис 1 мая
        OFFICE_FIELD_OPEN.click()
        self.send_keys(self.loc.OFFICE_FIELD_CHOSE, '1')
        self.wait_clickable(self.loc.OFFICE_CHOSE)
        self.click(self.loc.OFFICE_CHOSE)
        self.click(self.loc.FIELD_CLOSE)
        time.sleep(2)
        self.scroll_by(200)
        time.sleep(2)
        # Выбираем статус - на витрине
        STATUS_FIELD_OPEN.click()
        self.send_keys(self.loc.STATUS_FIELD_CHOSE, 'На витрине')
        self.click(self.loc.STATUS_CHOSE)
        self.click(self.loc.FIELD_CLOSE)
        # Закрываем фильтр
        self.click(self.loc.FILTER_CLOSE)
        time.sleep(3)

    def sale_product_in_shop(self):
        self.scroll_to_top()
        time.sleep(2)
        all_btn_open_menu_in_line = self.find_all(self.loc.BTN_OPEN_MENU_IN_LINE)
        print(all_btn_open_menu_in_line)
        time.sleep(2)
        all_btn_open_menu_in_line[0].click()
        # time.sleep(3)
        self.wait_clickable(self.loc.BTN_CHOSE_SALE_IN_MENU)
        self.click(self.loc.BTN_CHOSE_SALE_IN_MENU)
        # Выбор клиента
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
        source_chose = self.find(self.loc.SOURCE_ID_CHOSE)
        source_chose.click()
        # выбираем источник 2Gis
        source_find = self.driver.find_elements(*self.loc.SOURCE_ID_FIND)
        (source_find[0]).click()
        time.sleep(3)
        btn_create_dogovor = self.wait_clickable(self.loc.SUCCESS_BUTTON)
        btn_create_dogovor.click()
        # self.find(self.loc.SUCCESS_BUTTON)
        # self.click(self.loc.SUCCESS_BUTTON)
        time.sleep(8)

    def xref_go_to_product_id(self):
        self.find(self.loc.XREF_GO_TO_PRODUCT_ID)
        self.click(self.loc.XREF_GO_TO_PRODUCT_ID)
        time.sleep(4)

    def compare_product_status_out_of_stock(self):
        actual_text = self.get_text(self.loc.PRODUCT_STATUS_IN_PRODUCT_ID)
        print(f"Фактический текст: {actual_text}")  # Для отладки
        self.compare_text(self.loc.PRODUCT_STATUS_IN_PRODUCT_ID, "НЕТ В НАЛИЧИИ")

    def compare_product_condition_sold(self):
        actual_text = self.get_text(self.loc.PRODUCT_CONDITION_IN_PRODUCT_ID)
        print(f"Фактический текст: {actual_text}")  # Для отладки
        self.compare_text(self.loc.PRODUCT_CONDITION_IN_PRODUCT_ID, "Продан")
