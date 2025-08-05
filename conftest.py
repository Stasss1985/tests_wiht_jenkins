import pytest
import winsound
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.login_page.admin_login import AdminLogin
from pages.lead_page.lead_page import LeadPage
from pages.lead_page.product_page import ProductPage
from pages.lead_page.contract_сreate_page import ContractCreatePage
from pages.contract_page.do_operation_with_contract_page import DoOperationContractPage
import allure
from webdriver_manager.chrome import ChromeDriverManager
from pages.shop_page.shop_sale_page import ShopSalePage
from pages.person_page.person_page import PersonPage


@pytest.fixture(scope="session", autouse=True)
def play_sound_after_tests():
    yield
    winsound.PlaySound("SystemHand", winsound.SND_ALIAS)
    # winsound.Beep(1000, 500)


@pytest.fixture(scope="function")
def driver(request):
    # Создаем объект опций для Chrome
    chrome_options = Options()

    # Проверяем, есть ли параметр командной строки для запуска в headless режиме
    if request.config.getoption("--headless"):
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        # Устанавливаем размер окна и масштаб
        chrome_options.add_argument("--window-size=2560,1600")
        chrome_options.add_argument("--force-device-scale-factor=1")

    service = Service(ChromeDriverManager().install())
    chrome_driver = webdriver.Chrome(service=service, options=chrome_options)

    # Явная установка размера окна
    if request.config.getoption("--headless"):
        chrome_driver.set_window_size(2560, 1600)

        # Дополнительная настройка через DevTools Protocol
        chrome_driver.execute_cdp_cmd("Emulation.setDeviceMetricsOverride", {
            "width": 2560,
            "height": 1600,
            "deviceScaleFactor": 1,
            "mobile": False
        })

    try:
        yield chrome_driver
    finally:
        chrome_driver.quit()


# Добавляем опцию командной строки для headless режима
def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="Run tests in headless mode")


@pytest.fixture(scope="function")
def login_page(driver):
    return AdminLogin(driver)


@pytest.fixture()
def lead_page(driver):
    return LeadPage(driver)


@pytest.fixture()
def product_page(driver):
    return ProductPage(driver)


@pytest.fixture()
def contract_create_page(driver):
    return ContractCreatePage(driver)


@pytest.fixture()
def do_operation_with_contract_page(driver):
    return DoOperationContractPage(driver)


@pytest.fixture()
def shop_sale_page(driver):
    return ShopSalePage(driver)


@pytest.fixture()
def person_page(driver):
    return PersonPage(driver)


@pytest.fixture(scope="function")
def open_crm_as_admin(login_page):
    login_page.open_page()
    with allure.step('enter correct login and password'):
        login_page.fill_login_form_good('krivko.su@codeagency.ru', 'DLNKsfd3214$%23')
    with allure.step('Check correct url'):
        login_page.check_expected_url('https://erp-test.karman24.ru/')
    login_page.take_screenshot()
