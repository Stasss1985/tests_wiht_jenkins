import logging
import pytest


# @pytest.mark.repeat(3) запустит тест 3 раза
@pytest.mark.smoke('smoke test')
def test_01_sale_in_shop_product(open_crm_as_admin, lead_page, shop_sale_page, contract_create_page):
    logging.info('Старт проверки "Продажа техники из магазина за наличку"')
    lead_page.change_office_1_maya()
    lead_page.take_screenshot("change_office")

    logging.info('Переход в магазин')
    shop_sale_page.navigate_to_shop_page()
    shop_sale_page.take_screenshot("navigated_to_shop")

    logging.info('Открытие фильтра справа и сортировка для продажи товаров (не ЮИ)')
    shop_sale_page.filter_for_sale_product_in_shop()
    shop_sale_page.take_screenshot("filter_for_sale_product_in_shop")

    logging.info('Продажа товара из магазина (не ЮИ)')
    shop_sale_page.sale_product_in_shop()
    shop_sale_page.take_screenshot("sale_product_in_shop")

    logging.info('Печать документа')
    contract_create_page.print_document()
    contract_create_page.take_screenshot("document_printed")

    logging.info('Печать чека создания "догов потребит займа"')
    contract_create_page.print_check()
    contract_create_page.take_screenshot("check_printed")

    logging.info('Проверка статуса продажи товара (печати чека)')
    contract_create_page.compare_text_status()
    contract_create_page.take_screenshot("status_checked")

    logging.info('Переход в карточку товара из печати чека')
    shop_sale_page.xref_go_to_product_id()
    shop_sale_page.take_screenshot("product_card_accessed")

    logging.info('Проверка статуса "Нет в наличии" в карточке товара')
    shop_sale_page.compare_product_status_out_of_stock()
    shop_sale_page.take_screenshot("product_out_of_stock_checked")

    logging.info('Проверка состояния "Продан" в карточке товара')
    shop_sale_page.compare_product_condition_sold()
    shop_sale_page.take_screenshot("product_sold_checked")

    logging.info('Продажа техники из магазина за наличку завершена успешно')
