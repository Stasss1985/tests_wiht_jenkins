import sqlite3
import pytest
from pathlib import Path


@pytest.fixture
def db_connection():
    """Фикстура для подключения к тестовой БД SQLite"""
    # Лучше использовать относительный путь или переменные окружения
    db_path = Path(
        "C:/Users/user/AppData/Roaming/DBeaverData/workspace6/.metadata/sample-database-sqlite-1/Chinook.db")  # Path Или ваш абсолютный путь

    # Проверка существования файла БД (опционально)
    if not db_path.exists():
        pytest.skip(f"Файл базы данных {db_path} не найден")

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # Для доступа к полям по имени
    yield conn  # Возвращаем соединение тесту

    # Пост-обработка (закрытие соединения)
    conn.close()


@pytest.fixture
def db_cursor(db_connection):
    """Фикстура для курсора (наследует соединение из db_connection)"""
    cursor = db_connection.cursor()
    yield cursor
    cursor.close()


def test_get_table_album(db_connection, db_cursor):
    # Пример запроса: выборка таблицы Album
    db_cursor.execute("SELECT * FROM Album")
    rows = db_cursor.fetchall()
    for row in rows:
        print(dict(row))  # Преобразуйте Row в словарь


def test_get_table_album_WHERE_AlbumId_3(db_connection, db_cursor):
    # Пример запроса: выборка таблицы Album
    db_cursor.execute('SELECT * FROM Album WHERE AlbumId = 3')
    row = db_cursor.fetchone()
    # Проверка, что запись найдена
    assert row is not None, "Запись с AlbumId=3 не найдена"
    # Проверка ожидаемых значений
    assert row[0] == 3  # Проверка AlbumId по индексу
    assert row[1] == "Restless and Wild"  # Проверка Title по индексу
    # Альтернативный вариант сравнения по имени столбца
    assert row['AlbumId'] == 3  # Проверка AlbumId по имени
    assert row['Title'] == "Restless and Wild"  # Проверка Title по имени
    print(dict(row))  # Для отладки (чтобы увидеть, используйте pytest -s)


def test_get_all_title(db_connection, db_cursor):
    # Пример запроса: выборка таблицы Album
    db_cursor.execute("SELECT * FROM Album")
    rows = db_cursor.fetchall()
    for Album in rows:
        print(Album['Title'])  # показывает все значения в колонке Title


def test_get_last_5_in_table_album(db_connection, db_cursor):
    # Пример запроса: выборка таблицы Album
    db_cursor.execute("SELECT * FROM Album ORDER BY AlbumId DESC limit 5")
    tables = db_cursor.fetchall()
    print("Таблицы в базе:", tables)


def test_get_last_5_in_table_album_new2(db_connection, db_cursor):
    # Пример запроса с разбивкой по строкам ''' (так лучше видно, как в SQL)
    select_query = '''
    SELECT *
    FROM Album 
    ORDER BY AlbumId 
    DESC 
    limit 5'''
    db_cursor.execute(select_query)
    rows = db_cursor.fetchall()
    for row in rows:
        print(dict(row))  # Преобразуйте Row в словарь


def test_insert_into_in_table_album(db_connection, db_cursor):
    try:
        # 1. Вставка данных
        db_cursor.execute("INSERT INTO Album (Title, ArtistId) VALUES (?, ?)",
                          ('Русский РОК', 276))
        db_connection.commit()  # Фиксируем изменения
        print(f"Данные успешно добавлены")

    except sqlite3.Error as e:
        print(f"Ошибка при работе с SQLite: {e}")
        db_connection.rollback()  # Откатываем изменения при ошибке


def test_insert_into_many_in_table_album(db_connection, db_cursor):  # Вставка сразу нескольких данных executemany
    try:
        # 1. Вставка сразу нескольких данных executemany
        db_cursor.executemany("INSERT INTO Album (Title, ArtistId) VALUES (?, ?)",
                              [
                                  ('Русский РОК', 276),
                                  ('Итальянский джаз', 277)
                              ])
        db_connection.commit()  # Фиксируем изменения
        print(f"Данные успешно добавлены")

    except sqlite3.Error as e:
        print(f"Ошибка при работе с SQLite: {e}")
        db_connection.rollback()  # Откатываем изменения при ошибке


def test_delete_in_table_album(db_connection, db_cursor):
    try:
        db_cursor.execute("DELETE FROM Album WHERE Title = ?", ('Русский РОК',))
        db_connection.commit()
        print(f"Удалено записей: {db_cursor.rowcount}")
    except sqlite3.Error as e:
        print(f"Ошибка при удалении: {e}")
        db_connection.rollback()


# Пример SQL иньекций в MySQL и PostgreSQL %s
# query = "SELECT * FROM students WHERE name = %s and second_name = %s"
# cursor.execute(query, (input('name'), input('second_name')))
# print(cursor.fetchall())

def test_insert_into_and_get_lastrowid_album_id(db_connection, db_cursor):
    try:
        # 1. Вставка данных
        db_cursor.execute("INSERT INTO Album (Title, ArtistId) VALUES (?, ?)",
                          ('Русский РОК', 276))
        album_id = db_cursor.lastrowid
        db_cursor.execute(f'SELECT * from Album where AlbumId = {album_id}')
        print(dict(db_cursor.fetchone()))  # можно получать последние данные в запросе по ID (до .commit())
        db_connection.commit()  # Фиксируем изменения
        print(f"Данные успешно добавлены")

    except sqlite3.Error as e:
        print(f"Ошибка при работе с SQLite: {e}")
        db_connection.rollback()  # Откатываем изменения при ошибке
