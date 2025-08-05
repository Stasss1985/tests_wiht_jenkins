import pytest


@pytest.mark.smoke
def test_add_new_person_in_person_page(open_crm_as_admin, lead_page, person_page):
    # Смена офиса
    lead_page.change_office_1_maya()
    lead_page.take_screenshot()
    # Переход на страницу "Клиенты" person
    person_page.navigate_to_person_page()
    person_page.take_screenshot()
    # Добавление нового клиента
    person_page.add_new_client_in_person_page()
    person_page.take_screenshot()
    # Проверка что новый клиент появился в клиентах
    person_page.check_add_new_client_in_person_page()
    person_page.take_screenshot()
