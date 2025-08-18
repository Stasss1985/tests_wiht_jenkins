import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException, \
    StaleElementReferenceException
import logging
import allure
import os
from pathlib import Path
import datetime
from selenium.webdriver.common.by import By

# Для добавления в инициализацию driver: WebDriver - чтобы были подсказки
# и Pycharm понимал лучше.
logging.basicConfig(
    filename='tests.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
# Отключаем логи WDM (добавьте эти строки)
logging.getLogger('WDM').setLevel(logging.CRITICAL)  # Показывать только критические ошибки
logging.getLogger('WDM').propagate = False  # Запретить передачу логов родительским логгерам


class BasePage:
    base_url = 'https://www.google.com'
    page_url = None

    def __init__(self, driver: WebDriver):
        self.driver = driver
        driver.maximize_window()
        self.wait = WebDriverWait(driver, 30)  # Добавляем ожидание

    def open_page(self):
        if self.page_url:
            self.driver.get(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Page cannot be opened for this URL')

    def find(self, locator: tuple):
        try:
            return self.wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            logging.error(f"Element with locator {locator} not found.")
            self.take_screenshot(description=f"find_error_{locator}")
            return None

    def find_all(self, locator: tuple):
        try:
            return self.driver.find_elements(*locator)
        except Exception as e:
            logging.error(f"Ошибка при поиске элементов по локатору {locator}: {e}")
            self.take_screenshot(description=f"find_all_error_{locator}")
            raise AssertionError(f"Не удалось найти элементы по локатору {locator}")

    def send_keys(self, locator: tuple, text: str):
        try:
            self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)
        except TimeoutException:
            logging.error(f"Element with locator {locator} not visible.")
            self.take_screenshot(description=f"send_keys_error_{locator}")

    def click(self, locator: tuple, timeout=20, retry_delay=1, max_retries=3, scroll_if_needed=True):
        retries = 0
        while retries < max_retries:
            try:
                element = self.wait.until(EC.element_to_be_clickable(locator))
                if scroll_if_needed:
                    self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
                time.sleep(retry_delay)
                element.click()
                return
            except TimeoutException:
                logging.error(f"Элемент {locator} не стал кликабельным за {timeout} секунд.")
                self.take_screenshot(description=f"wait_click_timeout_{locator}")
                raise TimeoutException(f"Элемент {locator} не стал кликабельным")
            except ElementClickInterceptedException:
                retries += 1
                if retries < max_retries:
                    logging.info(f"Попытка повторного клика по элементу {locator} (попытка {retries + 1})")
                    time.sleep(retry_delay)
                else:
                    logging.error(f"Не удалось нажать на элемент {locator}, элемент перехвачен")
                    self.take_screenshot(description=f"wait_click_intercepted_{locator}")
                    raise ElementClickInterceptedException(f"Не удалось нажать на элемент {locator}")
            except StaleElementReferenceException:
                retries += 1
                if retries < max_retries:
                    logging.info(f"Элемент {locator} устарел, повторный поиск и клик (попытка {retries + 1})")
                    time.sleep(retry_delay)
                else:
                    logging.error(f"Элемент {locator} устарял и не найден после {max_retries} попыток")
                    self.take_screenshot(description=f"wait_click_stale_{locator}")
                    raise StaleElementReferenceException(f"Элемент {locator} устарел")
            except Exception as e:
                logging.error(f"Неизвестная ошибка при клике по элементу {locator}: {e}")
                self.take_screenshot(description=f"wait_click_error_{locator}")
                raise Exception(f"Неизвестная ошибка при клике по элементу {locator}")

    def get_text(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).text
        except TimeoutException:
            logging.error(f"Элемент {locator} не найден или не стал видимым за отведенное время")
            # Можно дополнительно бросить исключение или вернуть None/пустую строку
            raise  # Повторно вызываем исключение, чтобы тест упал

    def scroll_to_element(self, locator):
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        except TimeoutException:
            logging.error(f"Элемент {locator} не найден или не стал видимым за отведенное время")
            raise  # Повторно вызываем исключение

    def scroll_by(self, pixels: int):
        """Прокрутка страницы на заданное количество пикселей."""
        try:
            self.driver.execute_script(f"window.scrollBy(0, {pixels});")
        except Exception as e:
            logging.error(f"Ошибка при прокрутке на {pixels} пикселей: {e}")
            self.take_screenshot(description=f"scroll_by_error_{pixels}")
            raise AssertionError(f"Не удалось прокрутить страницу на {pixels} пикселей")

    def scroll_to_top(self):
        """Прокрутка страницы вверх до самого верха."""
        try:
            self.driver.execute_script("window.scrollTo(0, 0);")
        except Exception as e:
            logging.error(f"Ошибка при прокрутке страницы вверх: {e}")
            self.take_screenshot(description="scroll_to_top_error")
            raise AssertionError("Не удалось прокрутить страницу вверх")

    def scroll_to_down(self, scroll_pause_time=2):
        """Прокрутка страницы вниз до самого низа."""
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Прокрутка вниз
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Ждем, чтобы страница загрузилась
            time.sleep(scroll_pause_time)

            # Получаем новую высоту страницы после прокрутки
            new_height = self.driver.execute_script("return document.body.scrollHeight")

            # Если высота не изменилась, значит достигли низа страницы
            if new_height == last_height:
                break
            last_height = new_height

    def scroll_in_modal(self, modal_locator: tuple):
        """Прокрутка внутри всплывающего окна."""
        try:
            modal_window = self.wait.until(EC.visibility_of_element_located(modal_locator))
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal_window)
        except TimeoutException as e:
            logging.error(f"Модальное окно {modal_locator} не найдено или не стало видимым: {e}")
            self.take_screenshot(description=f"modal_not_found_{modal_locator}")
            raise AssertionError(f"Не удалось найти модальное окно {modal_locator}")
        except Exception as e:
            logging.error(f"Ошибка при прокрутке внутри модального окна {modal_locator}: {e}")
            self.take_screenshot(description=f"scroll_in_modal_error_{modal_locator}")
            raise AssertionError(f"Не удалось прокрутить внутри модального окна {modal_locator}")

    def scroll_in_modal_by(self, modal_locator: tuple, pixels: int):
        """Прокрутка внутри всплывающего окна на заданное количество пикселей."""
        try:
            modal_window = self.wait.until(EC.visibility_of_element_located(modal_locator))
            self.driver.execute_script(f"arguments[0].scrollTop += {pixels};", modal_window)
        except TimeoutException as e:
            logging.error(f"Модальное окно {modal_locator} не найдено или не стало видимым: {e}")
            self.take_screenshot(description=f"modal_not_found_{modal_locator}")
            raise AssertionError(f"Не удалось найти модальное окно {modal_locator}")
        except Exception as e:
            logging.error(f"Ошибка при прокрутке внутри модального окна {modal_locator} на {pixels} пикселей: {e}")
            self.take_screenshot(description=f"scroll_in_modal_error_{modal_locator}")
            raise AssertionError(f"Не удалось прокрутить внутри модального окна {modal_locator}")

    def check_expected_url(self, expected_url):
        """
        Проверяет, что текущий URL соответствует ожидаемому.
        :param expected_url: Ожидаемый URL.
        """
        current_url = self.driver.current_url
        assert current_url == expected_url, \
            f"Текущий URL не соответствует ожидаемому. Ожидалось: '{expected_url}', Фактически: '{current_url}'"

    def take_screenshot(self, description: str = "screenshot") -> None:
        try:
            # Создаем директорию с кроссплатформенными путями
            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(parents=True, exist_ok=True)
        
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{description}_{timestamp}.png"
            screenshot_path = str(screenshot_dir / filename)
        
            # Делаем скриншот один раз
            screenshot_bytes = self.driver.get_screenshot_as_png()
        
            # Сохраняем на диск
            with open(screenshot_path, "wb") as f:
                f.write(screenshot_bytes)
        
            # Прикрепляем в Allure
            allure.attach(
                screenshot_bytes,
                name=filename,
                attachment_type=allure.attachment_type.PNG
            )
        
        except Exception as e:
            logging.exception("Failed to take screenshot")  # Логируем стек трассировки

    def wait_for_element_visibility(self, locator: tuple, timeout: int = 30):
        """Ожидает появления элемента на странице."""
        try:
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            logging.error(f"Element with locator {locator} not visible after {timeout} seconds.")
            return None

    def wait_clickable(self, locator: tuple, timeout: int = 30):
        """Ожидает, пока элемент не станет кликабельным."""
        try:
            return self.wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            logging.error(f"Element with locator {locator} not clickable after {timeout} seconds.")
            return None

    def wait_for_elements(self, locator: tuple, timeout: int = 30):
        """Ожидает появления всех элементов на странице."""
        try:
            return self.wait.until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            logging.error(f"Elements with locator {locator} not visible after {timeout} seconds.")
            return []

    def wait_for_element_to_disappear(self, locator: tuple, timeout: int = 30):
        """Ожидает исчезновения элемента со страницы."""
        try:
            return self.wait.until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            logging.error(f"Element with locator {locator} still visible after {timeout} seconds.")
            return False

    @allure.step("Сравнение текста элемента с ожидаемым текстом")
    def compare_text(self, locator, expected_text):
        try:
            # Ожидание появления элемента и получение его текста
            actual_text = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator)).text

            assert actual_text == expected_text, f"Текст не совпадает. Ожидаемый: {expected_text}, Фактический: {actual_text}"
        except TimeoutException as e:
            logging.error(f"Элемент {locator} не найден или не стал видимым за 30 секунд: {e}")
            self.take_screenshot(description=f"compare_text_timeout_{locator}")
            raise AssertionError(f"Элемент {locator} не найден или не стал видимым")
        except AssertionError as e:
            logging.error(f"Текст не совпадает. Ожидаемый: {expected_text}, Фактический: {actual_text}: {e}")
            self.take_screenshot(description=f"compare_text_mismatch_{locator}")
            raise
        except Exception as e:
            logging.error(f"Ошибка при сравнении текста элемента {locator}: {e}")
            self.take_screenshot(description=f"compare_text_error_{locator}")
            raise AssertionError(f"Ошибка при сравнении текста элемента {locator}")
        finally:
            allure.attach(f"Ожидаемый текст: {expected_text}\nФактический текст: {actual_text}",
                          name="Сравнение текста",
                          attachment_type=allure.attachment_type.TEXT)
