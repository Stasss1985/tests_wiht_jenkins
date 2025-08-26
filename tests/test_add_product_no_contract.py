import allure
import time
import pytest
from selenium.webdriver.common.by import By


@pytest.mark.smoke
@pytest.mark.first_test
def test_add_gold_no_contract(login_page):
    login_page.open_page()
    # Смена офиса
    # lead_page.change_office_1_maya()
    # lead_page.take_screenshot()
    # Переход к созданию лида
    # lead_page.navigate_to_lead_create()
    # lead_page.take_screenshot()


# time.sleep(4)
# Добавление продукта
# product_page.scroll_by(500)
# time.sleep(2)
# product_page.add_product_gold()
# product_page.take_screenshot()
# Сравнение названия добавленного товара
# product_page.compare_name_product()
# product_page.take_screenshot()

@pytest.mark.regress
@pytest.mark.second_test
def test_add_gold_qr_no_contract(open_crm_as_admin, lead_page, product_page):
    # Смена офиса
    lead_page.change_office_1_maya()
    lead_page.take_screenshot()
    # Переход к созданию лида
    lead_page.navigate_to_lead_create()
    lead_page.take_screenshot()
    time.sleep(4)
    # Добавление продукта
    product_page.scroll_by(500)
    time.sleep(2)
    product_page.add_product_gold_QR()
    product_page.take_screenshot()
    # Сравнение названия добавленного товара
    product_page.compare_name_product()
    product_page.take_screenshot()


@pytest.mark.regress
def test_add_silver_no_contract(open_crm_as_admin, lead_page, product_page):
    # Смена офиса
    lead_page.change_office_1_maya()
    lead_page.take_screenshot()
    # Переход к созданию лида
    lead_page.navigate_to_lead_create()
    lead_page.take_screenshot()
    time.sleep(4)
    # Добавление продукта
    product_page.scroll_by(500)
    time.sleep(2)
    product_page.add_product_silver()
    product_page.take_screenshot()
    # Сравнение названия добавленного товара
    product_page.compare_name_product()
    product_page.take_screenshot()


@pytest.mark.extended
def test_add_laptop_no_contract(open_crm_as_admin, lead_page, product_page):
    # Смена офиса
    lead_page.change_office_1_maya()
    lead_page.take_screenshot()
    # Переход к созданию лида
    lead_page.navigate_to_lead_create()
    lead_page.take_screenshot()
    # time.sleep(4)
    # Добавление продукта
    product_page.scroll_by(500)
    time.sleep(2)
    product_page.add_product_laptop()
    product_page.take_screenshot()
    # Сравнение названия добавленного товара
    product_page.compare_name_product()
    product_page.take_screenshot()


@pytest.mark.regress
def test_add_car_no_contract(open_crm_as_admin, lead_page, product_page):
    # Смена офиса
    lead_page.change_office_krasnix_partisan()
    lead_page.take_screenshot()
    # Переход к созданию лида
    lead_page.navigate_to_lead_create()
    lead_page.take_screenshot()
    time.sleep(4)
    # Добавление товара
    product_page.scroll_by(500)
    time.sleep(2)
    product_page.add_product_car()
    product_page.take_screenshot()
    # Сравнение названия добавленного товара
    product_page.compare_name_product()
    product_page.take_screenshot()
