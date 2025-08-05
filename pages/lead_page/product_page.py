from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import random
import time
import os


class ProductLoc():
    ADD_PRODUCT_BUTTON = (By.CSS_SELECTOR, 'button[aria-label="Добавить товар"]')
    MAIN_CATEGORY = (By.ID, 'mainInstanceCategoryId')  # активация категории товара
    INSTANCE_NAME = (By.ID, 'instanceName')
    # локаторы в основном для товар-ЗОЛОТО
    MAIN_CATEGORY_ID_CHOSE = (By.CSS_SELECTOR, '[aria-posinset="2"]')  # Локатор Основные изделия в ЮИ
    CATEGORY = (By.ID, 'instanceCategoryId')
    METAL_TYPE = (By.CSS_SELECTOR, "#instanceV\.6")
    METAL_SAMPLE = (By.CSS_SELECTOR, "#instanceV\.7")
    METAL_WEIGHT = (By.CSS_SELECTOR, "#instanceV\.14 > input")
    INSERT_WEIGHT = (By.CSS_SELECTOR, "#instanceV\.13 > input")
    JEWELRY_MARKED = (By.ID, 'typeJewelryId')  # typeJewelryId
    # локаторы общие
    SELL_PRICE = (By.CSS_SELECTOR, "#sellPrice > input")
    COST = (By.CSS_SELECTOR, "#cost > input")
    SAVE_BUTTON = (By.CSS_SELECTOR, '[aria-label="Сохранить"]')
    CREATED_NAME_PRODUCT_TEXT = (By.CSS_SELECTOR, '.d-flex.align-items-center.justify-content-between > a')
    # локаторы для ноутбука
    PRODUCT_CATEGORY_LAPTOP = (By.CSS_SELECTOR, '[aria-posinset="6"]')
    CATEGORY_LAPTOP = (By.CSS_SELECTOR, '[aria-label="Ноутбуки"]')
    # локаторы для автомобиля
    PRODUCT_CATEGORY_CAR = (By.CSS_SELECTOR, '[aria-label="Автомобили"]')
    MARCA_CAR_FIELD = (By.ID, 'instanceV.730')
    MARCA_CAR_CHOOSE = (By.CSS_SELECTOR, '[aria-label="Acura"]')
    MODEL_CAR_FIELD = (By.ID, 'instanceV.735')
    MODEL_CAR_CHOOSE = (By.CSS_SELECTOR, '[aria-label="MDX"]')
    PROBEG_CAR_FIELD = (By.CSS_SELECTOR, '#instanceV\.9644 > input')
    YEAR_CAR_FIELD = (By.CSS_SELECTOR, '#instanceV\.740 > input')
    COLOUR_CAR_FIELD = (By.ID, 'instanceV.745')
    COLOUR_CAR_CHOOSE = (By.CSS_SELECTOR, '[aria-label="Белый"]')
    GOS_NUMBER_CAR = (By.ID, 'instanceV.750')
    VIN_NUMBER_CAR = (By.ID, 'instanceV.755')
    NUMBER_ENGINE = (By.ID, 'instanceV.760')
    WORKING_VOLUME_ENGINE = (By.CSS_SELECTOR, '#instanceV\.756 > input')
    SERIES_NUMBER_PTS = (By.ID, 'instanceV.780')
    PTS_ISSUED_BY_WHOM = (By.ID, 'instanceV.785')
    DATE_OF_ISSUE_PTS = (By.ID, 'instanceV.790')
    SERIES_NUMBER_STS = (By.ID, 'instanceV.795')
    STS_ISSUED_BY_WHOM = (By.ID, 'instanceV.800')
    DATE_OF_ISSUE_STS = (By.ID, 'instanceV.805')


class ProductPage(BasePage):
    loc = ProductLoc

    def add_product_gold(self):
        # добавляем товар золото
        self.click(self.loc.ADD_PRODUCT_BUTTON)
        self.product_name = random.choice(["Кольцо", "Цепь", "Кулон", "Серьга", "Браслет", "Ожерелье", "Подвеска"])
        # Отправка выбранного названия в элемент
        self.send_keys(self.loc.INSTANCE_NAME, self.product_name)
        time.sleep(2)
        maincategoryId_find = self.find(self.loc.MAIN_CATEGORY)  # активация категории товара
        maincategoryId_find.click()

        # Выбор Основные изделия в ЮИ
        self.wait_for_element_visibility(self.loc.MAIN_CATEGORY_ID_CHOSE)
        maincategoryId_chose = self.wait_clickable(self.loc.MAIN_CATEGORY_ID_CHOSE)
        maincategoryId_chose.click()

        time.sleep(2)
        # Активация подкатегории - ЮИ
        categoryId_find = self.find(self.loc.CATEGORY)
        categoryId_find.click()

        # Выбор (random.choice) подкатегории - ЮИ
        categoryId_chose9 = self.wait_clickable((By.CSS_SELECTOR, '[aria-posinset="9"]'))
        categoryId_chose8 = self.wait_clickable((By.CSS_SELECTOR, '[aria-posinset="8"]'))
        categoryId_chose7 = self.wait_clickable((By.CSS_SELECTOR, '[aria-posinset="7"]'))
        categoryId_chose6 = self.wait_clickable((By.CSS_SELECTOR, '[aria-posinset="6"]'))
        categoryId_chose = (categoryId_chose9, categoryId_chose8,
                            categoryId_chose7, categoryId_chose6)
        self.click(random.choice(categoryId_chose))

        # Свойства
        time.sleep(2)
        type_metal_find = self.find(self.loc.METAL_TYPE)
        time.sleep(2)
        type_metal_find.click()
        type_metal_chose = self.find((By.CSS_SELECTOR, '[aria-label="Золото"]'))
        type_metal_chose.click()

        # Вводим пробу металла
        proba_metal_find = self.find(self.loc.METAL_SAMPLE)
        self.driver.execute_script(
            "return arguments[0].scrollIntoView(true);", proba_metal_find)
        proba_metal_find.click()
        proba_metal_chose = self.wait_clickable((By.CSS_SELECTOR, '[aria-label="585"]'))
        proba_metal_chose.click()

        # Вводим вес металла
        weight_metal_find = self.find((By.CSS_SELECTOR, "#instanceV\.14"))
        self.driver.execute_script(
            "return arguments[0].scrollIntoView(true);", weight_metal_find)

        weight_metal_add = self.wait_for_element_visibility(self.loc.METAL_WEIGHT)

        # Выбор случайного веса
        random_weight = random.choice([5, 7, 9, 10, 12, 15])
        weight_metal_add.send_keys(random_weight)

        # Получаем введенное значение и преобразуем в целое число (?????)
        weight_metal_add_int = int(weight_metal_add.get_attribute('value'))

        # Вводим вес вставок
        weight_vstavka_add = self.wait_for_element_visibility(self.loc.INSERT_WEIGHT)
        # Вычисляем вес вставок и вводим его
        weight_vstavka_add.send_keys(int(weight_metal_add_int / 3))

        # Находим Тип (по QR или/ без QR x Лом)
        JewelryMarked_find = self.find(self.loc.JEWELRY_MARKED)
        JewelryMarked_find.click()
        time.sleep(2)

        # Выбираем Тип - aria-label="На витрину (без QR) и ЛОМ (с/без QR)"
        isJewelryMarked_chose = self.wait_for_element_visibility(
            (By.CSS_SELECTOR, '[aria-label="На витрину (без QR) и ЛОМ (с/без QR)"]'))
        isJewelryMarked_chose.click()

        # Вводим Цена на витрине
        sellPrice_add = self.wait_for_element_visibility(self.loc.SELL_PRICE)
        # Выбор случайной цены
        random_sellPrice = random.choice([300, 1000, 2500, 5000, 7321])
        sellPrice_add.send_keys(random_sellPrice)

        # Получаем введенное значение и преобразуем в целое число
        random_sellPrice_int = int(sellPrice_add.get_attribute('aria-valuenow'))

        # Вводим Себестоимость
        cost_add = self.wait_for_element_visibility(self.loc.COST)
        # Вычисляем Себестоимость и вводим ее
        #  (себестоимость я выбрал -20% от цены на Витрине)
        cost_add.send_keys(int(random_sellPrice_int * 0.8))

        # Прокрутка вниз до кнопки "Сохранить"
        scroll_down = self.wait_for_element_visibility(self.loc.SAVE_BUTTON)
        self.driver.execute_script(
            "return arguments[0].scrollIntoView(true);", scroll_down)

        # прикрепляем фото
        files_add = self.find((By.CSS_SELECTOR, 'input[type="file"]'))
        # прикрепляемый файл (через os мы вытаскиваем путь текущей директории и склеиваем джойном.
        photo_path = os.path.dirname(__file__)
        file_path = os.path.join(photo_path, 'Снимок экрана 2024-11-02 123632.png')
        files_add.send_keys(file_path)
        time.sleep(3)

        # Прокрутка вниз до кнопки "Сохранить"
        scroll_down2 = self.wait_for_element_visibility(self.loc.SAVE_BUTTON)

        # Прокрутка вниз страницы
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_down2)

        # Теперь ждем, пока элемент станет кликабельным
        self.wait_clickable(scroll_down2)
        # Кликаем по кнопки сохранить
        scroll_down2.click()

    def add_product_gold_QR(self):
        # добавляем товар золото
        self.click(self.loc.ADD_PRODUCT_BUTTON)
        self.product_name = random.choice(["Кольцо", "Цепь", "Кулон", "Серьга", "Браслет", "Ожерелье", "Подвеска"])
        # Отправка выбранного названия в элемент
        self.send_keys(self.loc.INSTANCE_NAME, self.product_name)
        time.sleep(2)
        maincategoryId_find = self.find(self.loc.MAIN_CATEGORY)  # активация категории товара
        maincategoryId_find.click()

        # Выбор Основные изделия в ЮИ
        self.wait_for_element_visibility(self.loc.MAIN_CATEGORY_ID_CHOSE)
        maincategoryId_chose = self.wait_clickable(self.loc.MAIN_CATEGORY_ID_CHOSE)
        maincategoryId_chose.click()

        time.sleep(2)
        # Активация подкатегории - ЮИ
        categoryId_find = self.find(self.loc.CATEGORY)
        categoryId_find.click()

        # Выбор (random.choice) подкатегории - ЮИ
        categoryId_chose9 = self.wait_clickable((By.CSS_SELECTOR, '[aria-posinset="9"]'))
        categoryId_chose8 = self.wait_clickable((By.CSS_SELECTOR, '[aria-posinset="8"]'))
        categoryId_chose7 = self.wait_clickable((By.CSS_SELECTOR, '[aria-posinset="7"]'))
        categoryId_chose6 = self.wait_clickable((By.CSS_SELECTOR, '[aria-posinset="6"]'))
        categoryId_chose = (categoryId_chose9, categoryId_chose8,
                            categoryId_chose7, categoryId_chose6)
        self.click(random.choice(categoryId_chose))

        # Свойства
        time.sleep(2)
        type_metal_find = self.find(self.loc.METAL_TYPE)
        type_metal_find.click()
        type_metal_chose = self.find((By.CSS_SELECTOR, '[aria-label="Золото"]'))
        type_metal_chose.click()

        # Вводим пробу металла
        proba_metal_find = self.find(self.loc.METAL_SAMPLE)
        self.driver.execute_script(
            "return arguments[0].scrollIntoView(true);", proba_metal_find)
        proba_metal_find.click()
        proba_metal_chose = self.wait_clickable((By.CSS_SELECTOR, '[aria-label="585"]'))
        proba_metal_chose.click()

        # Вводим вес металла
        weight_metal_find = self.find((By.CSS_SELECTOR, "#instanceV\.14"))
        self.driver.execute_script(
            "return arguments[0].scrollIntoView(true);", weight_metal_find)

        weight_metal_add = self.wait_for_element_visibility(self.loc.METAL_WEIGHT)

        # Выбор случайного веса
        random_weight = random.choice([5, 7, 9, 10, 12, 15])
        weight_metal_add.send_keys(random_weight)

        # Получаем введенное значение и преобразуем в целое число (?????)
        weight_metal_add_int = int(weight_metal_add.get_attribute('value'))

        # Вводим вес вставок
        weight_vstavka_add = self.wait_for_element_visibility(self.loc.INSERT_WEIGHT)
        # Вычисляем вес вставок и вводим его
        weight_vstavka_add.send_keys(int(weight_metal_add_int / 3))

        # Находим Тип (по QR или/ без QR x Лом)
        JewelryMarked_find = self.find(self.loc.JEWELRY_MARKED)
        JewelryMarked_find.click()
        time.sleep(2)

        # Выбираем Тип - aria-label="На витрину (только с QR)"
        isJewelryMarked_chose = self.wait_for_element_visibility(
            (By.CSS_SELECTOR, '[aria-label="На витрину (только с QR)"]'))
        isJewelryMarked_chose.click()

        # Вводим Цена на витрине
        sellPrice_add = self.wait_for_element_visibility(self.loc.SELL_PRICE)
        # Выбор случайной цены
        random_sellPrice = random.choice([300, 1000, 2500, 5000, 7321])
        sellPrice_add.send_keys(random_sellPrice)

        # Получаем введенное значение и преобразуем в целое число
        random_sellPrice_int = int(sellPrice_add.get_attribute('aria-valuenow'))

        # Вводим Себестоимость
        cost_add = self.wait_for_element_visibility(self.loc.COST)
        # Вычисляем Себестоимость и вводим ее
        #  (себестоимость я выбрал -20% от цены на Витрине)
        cost_add.send_keys(int(random_sellPrice_int * 0.8))

        # Прокрутка вниз до кнопки "Сохранить"
        scroll_down = self.wait_for_element_visibility(self.loc.SAVE_BUTTON)
        self.driver.execute_script(
            "return arguments[0].scrollIntoView(true);", scroll_down)

        # прикрепляем фото
        files_add = self.find((By.CSS_SELECTOR, 'input[type="file"]'))
        # прикрепляемый файл (через os мы вытаскиваем путь текущей директории и склеиваем джойном.
        photo_path = os.path.dirname(__file__)
        file_path = os.path.join(photo_path, 'Снимок экрана 2024-11-02 123632.png')
        files_add.send_keys(file_path)
        time.sleep(3)

        # Прокрутка вниз до кнопки "Сохранить"
        scroll_down2 = self.wait_for_element_visibility(self.loc.SAVE_BUTTON)

        # Прокрутка вниз страницы
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_down2)

        # Теперь ждем, пока элемент станет кликабельным
        self.wait_clickable(scroll_down2)
        # Кликаем по кнопки сохранить
        scroll_down2.click()

    def add_product_silver(self):
        # добавляем товар серебро
        self.click(self.loc.ADD_PRODUCT_BUTTON)
        self.product_name = random.choice(["Кольцо", "Цепь", "Кулон", "Серьга", "Браслет", "Ожерелье", "Подвеска"])
        # Отправка выбранного названия в элемент
        self.send_keys(self.loc.INSTANCE_NAME, self.product_name)
        time.sleep(2)
        maincategoryId_find = self.find(self.loc.MAIN_CATEGORY)  # активация категории товара
        maincategoryId_find.click()

        # Выбор Основные изделия в ЮИ
        self.wait_for_element_visibility(self.loc.MAIN_CATEGORY_ID_CHOSE)
        maincategoryId_chose = self.wait_clickable(self.loc.MAIN_CATEGORY_ID_CHOSE)
        maincategoryId_chose.click()

        time.sleep(2)
        # Активация подкатегории - ЮИ
        categoryId_find = self.find(self.loc.CATEGORY)
        categoryId_find.click()

        # Выбор (random.choice) подкатегории - ЮИ
        categoryId_chose9 = self.wait_clickable((By.CSS_SELECTOR, '[aria-posinset="9"]'))
        categoryId_chose8 = self.wait_clickable((By.CSS_SELECTOR, '[aria-posinset="8"]'))
        categoryId_chose7 = self.wait_clickable((By.CSS_SELECTOR, '[aria-posinset="7"]'))
        categoryId_chose6 = self.wait_clickable((By.CSS_SELECTOR, '[aria-posinset="6"]'))
        categoryId_chose = (categoryId_chose9, categoryId_chose8,
                            categoryId_chose7, categoryId_chose6)
        self.click(random.choice(categoryId_chose))

        # Свойства
        time.sleep(2)
        # self.wait_clickable(self.loc.METAL_TYPE)
        type_metal_find = self.find(self.loc.METAL_TYPE)
        type_metal_find.click()
        type_metal_chose = self.find((By.CSS_SELECTOR, '[aria-label="Серебро"]'))
        type_metal_chose.click()

        # Вводим пробу металла
        proba_metal_find = self.find(self.loc.METAL_SAMPLE)
        self.driver.execute_script(
            "return arguments[0].scrollIntoView(true);", proba_metal_find)
        proba_metal_find.click()
        proba_metal_chose = self.wait_clickable((By.CSS_SELECTOR, '[aria-label="925"]'))
        proba_metal_chose.click()

        # Вводим вес металла
        weight_metal_find = self.find((By.CSS_SELECTOR, "#instanceV\.14"))
        self.driver.execute_script(
            "return arguments[0].scrollIntoView(true);", weight_metal_find)

        weight_metal_add = self.wait_for_element_visibility(self.loc.METAL_WEIGHT)

        # Выбор случайного веса
        random_weight = random.choice([5, 7, 9, 10, 12, 15])
        weight_metal_add.send_keys(random_weight)

        # Получаем введенное значение и преобразуем в целое число (?????)
        weight_metal_add_int = int(weight_metal_add.get_attribute('value'))

        # Вводим вес вставок
        weight_vstavka_add = self.wait_for_element_visibility(self.loc.INSERT_WEIGHT)
        # Вычисляем вес вставок и вводим его
        weight_vstavka_add.send_keys(int(weight_metal_add_int / 3))

        # Вводим Цена на витрине
        sellPrice_add = self.wait_for_element_visibility(self.loc.SELL_PRICE)
        # Выбор случайной цены
        random_sellPrice = random.choice([300, 1000, 2500, 5000, 7321])
        sellPrice_add.send_keys(random_sellPrice)

        # Получаем введенное значение и преобразуем в целое число
        random_sellPrice_int = int(sellPrice_add.get_attribute('aria-valuenow'))

        # Вводим Себестоимость
        cost_add = self.wait_for_element_visibility(self.loc.COST)
        # Вычисляем Себестоимость и вводим ее
        #  (себестоимость я выбрал -20% от цены на Витрине)
        cost_add.send_keys(int(random_sellPrice_int * 0.8))

        # Прокрутка вниз до кнопки "Сохранить"
        scroll_down = self.wait_for_element_visibility(self.loc.SAVE_BUTTON)
        self.driver.execute_script(
            "return arguments[0].scrollIntoView(true);", scroll_down)

        # прикрепляем фото
        files_add = self.find((By.CSS_SELECTOR, 'input[type="file"]'))
        # прикрепляемый файл (через os мы вытаскиваем путь текущей директории и склеиваем джойном.
        photo_path = os.path.dirname(__file__)
        file_path = os.path.join(photo_path, 'Снимок экрана 2024-11-02 123632.png')
        files_add.send_keys(file_path)
        time.sleep(3)

        # Прокрутка вниз до кнопки "Сохранить"
        scroll_down2 = self.wait_for_element_visibility(self.loc.SAVE_BUTTON)

        # Прокрутка вниз страницы
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_down2)

        # Теперь ждем, пока элемент станет кликабельным
        self.wait_clickable(scroll_down2)
        # Кликаем по кнопки сохранить
        scroll_down2.click()

    def add_product_laptop(self):
        # добавляем товар ноутбук
        self.wait_clickable(self.loc.ADD_PRODUCT_BUTTON)
        self.click(self.loc.ADD_PRODUCT_BUTTON)
        # Выбор случайного названия товара
        self.product_name = random.choice(["Телефон Samsung S10", "Ноутбук Ninkear N16 Pro"])
        # Отправка выбранного названия в элемент
        self.send_keys(self.loc.INSTANCE_NAME, self.product_name)
        time.sleep(2)
        maincategoryId_find = self.find(self.loc.MAIN_CATEGORY)  # активация категории товара
        maincategoryId_find.click()
        time.sleep(2)
        # Выбор категории "Компютеры и ноутбуки"
        self.wait_for_element_visibility(self.loc.PRODUCT_CATEGORY_LAPTOP)
        product_category_laptop_chose = self.wait_clickable(self.loc.PRODUCT_CATEGORY_LAPTOP)
        product_category_laptop_chose.click()
        time.sleep(3)
        # Активация подкатегории
        categoryId_find = self.find(self.loc.CATEGORY)
        categoryId_find.click()
        # Активация подкатегории - "Ноутбуки"
        category_laptop_find = self.find(self.loc.CATEGORY_LAPTOP)
        category_laptop_find.click()
        # Вводим Цена на витрине
        sellPrice_add = self.wait_for_element_visibility(self.loc.SELL_PRICE)
        # Выбор случайной цены
        random_sellPrice = random.choice([300, 1000, 2500, 5000, 7321])
        sellPrice_add.send_keys(random_sellPrice)
        # Получаем введенное значение и преобразуем в целое число
        random_sellPrice_int = int(sellPrice_add.get_attribute('aria-valuenow'))
        # Вводим Себестоимость
        cost_add = self.wait_for_element_visibility(self.loc.COST)
        # Вычисляем Себестоимость и вводим ее
        #  (себестоимость я выбрал -20% от цены на Витрине)
        cost_add.send_keys(int(random_sellPrice_int * 0.8))
        # Прокрутка вниз до кнопки "Сохранить"
        scroll_down = self.wait_for_element_visibility(self.loc.SAVE_BUTTON)
        self.driver.execute_script(
            "return arguments[0].scrollIntoView(true);", scroll_down)
        # прикрепляем фото
        files_add = self.find((By.CSS_SELECTOR, 'input[type="file"]'))
        # прикрепляемый файл (через os мы вытаскиваем путь текущей директории и склеиваем джойном.
        photo_path = os.path.dirname(__file__)
        file_path = os.path.join(photo_path, 'Снимок экрана 2024-11-02 123632.png')
        files_add.send_keys(file_path)
        time.sleep(3)
        # Прокрутка вниз до кнопки "Сохранить"
        scroll_down2 = self.wait_for_element_visibility(self.loc.SAVE_BUTTON)
        # Прокрутка вниз страницы
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_down2)
        # Теперь ждем, пока элемент станет кликабельным
        self.wait_clickable(scroll_down2)
        # Кликаем по кнопки сохранить
        scroll_down2.click()

    def add_product_car(self):
        # добавляем товар автомобиль
        self.click(self.loc.ADD_PRODUCT_BUTTON)
        self.product_name = random.choice(["Acura MDX", "Acura Macura"])
        # Отправка выбранного названия в элемент
        self.send_keys(self.loc.INSTANCE_NAME, self.product_name)
        time.sleep(2)
        maincategoryId_find = self.find(self.loc.MAIN_CATEGORY)  # активация категории товара
        maincategoryId_find.click()
        time.sleep(2)
        # Выбор категории "Автомобили"
        self.wait_for_element_visibility(self.loc.PRODUCT_CATEGORY_CAR)
        product_category_laptop_car = self.wait_clickable(self.loc.PRODUCT_CATEGORY_CAR)
        product_category_laptop_car.click()
        time.sleep(3)
        # Свойства автомобиля
        # Активация поля Марка
        marca_car_field_find = self.find(self.loc.MARCA_CAR_FIELD)
        marca_car_field_find.click()
        # Выбор марки автомобиля Acura
        marca_car_choose = self.find(self.loc.MARCA_CAR_CHOOSE)
        marca_car_choose.click()
        # Активация поля Модель
        model_car_field_find = self.find(self.loc.MODEL_CAR_FIELD)
        model_car_field_find.click()
        # Выбор модели автомобиля MDX
        model_car_choose = self.find(self.loc.MODEL_CAR_CHOOSE)
        model_car_choose.click()
        # Ввод пробега
        self.send_keys(self.loc.PROBEG_CAR_FIELD, '15000')
        # Ввод года автомобиля
        self.send_keys(self.loc.YEAR_CAR_FIELD, '2023')
        # Активация поля Цвет
        colour_car_field = self.find(self.loc.COLOUR_CAR_FIELD)
        colour_car_field.click()
        # Выбор цвета автомобиля "Белый"
        colour_car_choose = self.find(self.loc.COLOUR_CAR_CHOOSE)
        colour_car_choose.click()
        # Ввод ГОС номера машины
        self.send_keys(self.loc.GOS_NUMBER_CAR, 'АВ654Х123')
        # Ввод VIN номера машины
        self.send_keys(self.loc.VIN_NUMBER_CAR, 'VINjldk1564воал')
        # Ввод номера двигателя
        self.send_keys(self.loc.NUMBER_ENGINE, 'б/н')
        # Ввод Рабочий объем двигателя, куб. см.
        self.send_keys(self.loc.WORKING_VOLUME_ENGINE, '2400')
        # Ввод Серия, номер ПТС
        self.send_keys(self.loc.SERIES_NUMBER_PTS, '77 УН879999')
        # Ввод ПТС выдан - кем.
        self.send_keys(self.loc.PTS_ISSUED_BY_WHOM, 'ГИБДД Отд №3 МРЭО ГИБДД УМВД по Калужской области')
        # Дата выдачи ПТС
        self.send_keys(self.loc.DATE_OF_ISSUE_PTS, '21.02.2024')
        # Серия, номер СТС
        self.send_keys(self.loc.SERIES_NUMBER_STS, '35 ХН 503585')
        # СТС выдан - кем.
        self.send_keys(self.loc.STS_ISSUED_BY_WHOM, 'МРЭО ГИБДД УМВД по Калужской области')
        # Дата выдачи СТС
        self.send_keys(self.loc.DATE_OF_ISSUE_STS, '22.03.2024')
        # Вводим Цена на витрине
        sellPrice_add = self.wait_for_element_visibility(self.loc.SELL_PRICE)
        # Выбор случайной цены
        random_sellPrice = random.choice([300, 1000, 2500, 5000])
        sellPrice_add.send_keys(random_sellPrice)
        # Получаем введенное значение и преобразуем в целое число
        random_sellPrice_int = int(sellPrice_add.get_attribute('aria-valuenow'))
        # Вводим Себестоимость
        cost_add = self.wait_for_element_visibility(self.loc.COST)
        # Вычисляем Себестоимость и вводим ее
        #  (себестоимость я выбрал -20% от цены на Витрине)
        cost_add.send_keys(int(random_sellPrice_int * 0.8))
        # Прокрутка вниз до кнопки "Сохранить"
        scroll_down = self.wait_for_element_visibility(self.loc.SAVE_BUTTON)
        self.driver.execute_script(
            "return arguments[0].scrollIntoView(true);", scroll_down)
        # прикрепляем фото
        files_add = self.find((By.CSS_SELECTOR, 'input[type="file"]'))
        # прикрепляемый файл (через os мы вытаскиваем путь текущей директории и склеиваем джойном.
        photo_path = os.path.dirname(__file__)
        file_path = os.path.join(photo_path, 'Снимок экрана 2024-11-02 123632.png')
        files_add.send_keys(file_path)
        time.sleep(3)
        # Прокрутка вниз до кнопки "Сохранить"
        scroll_down2 = self.wait_for_element_visibility(self.loc.SAVE_BUTTON)
        # Прокрутка вниз страницы
        self.driver.execute_script("arguments[0].scrollIntoView(true);", scroll_down2)
        # Теперь ждем, пока элемент станет кликабельным
        self.wait_clickable(scroll_down2)
        # Кликаем по кнопки сохранить
        scroll_down2.click()

    def compare_name_product(self):
        # Проверяем название добавляемого товара с тем названием который создан
        created_name_product = self.get_text(self.loc.CREATED_NAME_PRODUCT_TEXT)
        assert self.product_name in created_name_product, (
            f'Название товара отличается: добавленное - "{self.product_name}", '
            f'созданное - "{created_name_product}", '
            f'или товар не был добавлен'
        )
