import sqlite3

DATABASE_NAME = "library.db"


def create_table():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            author TEXT NOT NULL,
            publication_year INTEGER NOT NULL,
            genre TEXT NOT NULL,
            number_of_pages INTEGER NOT NULL,
            number_of_copies INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
    print(f"Таблица 'books' успешно создана '{DATABASE_NAME}'.")

def insert_books():
    books_data = [
        (1, 'Война и мир', 'Лев Толстой', 1869, 'Роман-эпопея', 1300, 5),
        (2, 'Преступление и наказание', 'Федор Достоевский', 1866, 'Философский роман', 600, 3),
        (3, 'Мастер и Маргарита', 'Михаил Булгаков', 1966, 'Фантастический роман', 480, 8),
        (4, 'Отцы и дети', 'Иван Тургенев', 1862, 'Роман', 350, 4),
        (5, 'Евгений Онегин', 'Александр Пушкин', 1833, 'Роман в стихах', 250, 6),
        (6, 'Мертвые души', 'Николай Гоголь', 1842, 'Поэма в прозе', 300, 2),
        (7, 'Герой нашего времени', 'Михаил Лермонтов', 1840, 'Роман', 200, 7),
        (8, 'Архипелаг ГУЛАГ', 'Александр Солженицын', 1973, 'Документальный роман', 1500, 1),
        (9, '1984', 'Джордж Оруэлл', 1949, 'Антиутопия', 320, 10),
        (10, 'Гарри Поттер и философский камень', 'Джоан Роулинг', 1997, 'Фэнтези', 400, 15),
        (11, 'Властелин колец: Братство кольца', 'Дж. Р. Р. Толкин', 1954, 'Фэнтези', 500, 12)
    ]

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT OR IGNORE INTO books VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', books_data)

    conn.commit()
    conn.close()
    print(f"Книги добавлены в таблицу 'books'.")


def get_all_books():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()

    conn.close()
    return rows


def view_books():
    rows = get_all_books()
    print("\n--- Список книг в базе данных ---")
    if rows:
        for row in rows:
            print(row)
    else:
        print("База данных пуста.")
    print("--------------------------------\n")


def update_book_name(book_id, new_name):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("UPDATE books SET name = ? WHERE id = ?", (new_name, book_id))

    conn.commit()
    conn.close()
    if cursor.rowcount > 0:
        print(f"Название книги с ID {book_id} успешно обновлено на '{new_name}'.")
    else:
        print(f"Книга с ID {book_id} не найдена.")


def delete_book(book_id):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))

    conn.commit()
    conn.close()
    if cursor.rowcount > 0:
        print(f"Книга с ID {book_id} успешно удалена.")
    else:
        print(f"Книга с ID {book_id} не найдена.")


if __name__ == "__main__":
    create_table()
    insert_books()

    print("Вызов view_books() после вставки:")
    view_books()

    book_id_to_update = 1
    new_title = 'Война и мир (исправленное название)'
    update_book_name(book_id_to_update, new_title)

    print(f"\nВызов view_books() после обновления книги с ID {book_id_to_update}:")
    view_books()

    book_id_to_delete = 2
    delete_book(book_id_to_delete)

    print(f"\nВызов view_books() после удаления книги с ID {book_id_to_delete}:")
    view_books()
# proverka