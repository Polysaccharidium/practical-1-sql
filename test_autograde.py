import sqlite3

# --- Настройка базы данных ---
def setup_db():
    conn = sqlite3.connect(":memory:")  # временная база в памяти
    cur = conn.cursor()
    # создаем таблицу
    cur.execute("""
        CREATE TABLE students (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER
        );
    """)
    # вставляем начальные данные
    cur.execute("INSERT INTO students (id, name, age) VALUES (1, 'Alice', 20);")
    cur.execute("INSERT INTO students (id, name, age) VALUES (2, 'Bob', 21);")
    cur.execute("INSERT INTO students (id, name, age) VALUES (3, 'Charlie', 23);")
    return conn, cur

# --- Тест обновления студента ---
def test_update_student():
    conn, cur = setup_db()
    with open("starter.sql") as f:
        student_sql = f.read()
    cur.executescript(student_sql)
    cur.execute("SELECT name, age FROM students WHERE id = 1;")
    result = cur.fetchone()
    assert result == ("Alice_updated", 22), f"Ожидалось ('Alice_updated', 22), получено {result}"

# --- Тест удаления студента ---
def test_delete_student():
    conn, cur = setup_db()
    with open("starter.sql") as f:
        student_sql = f.read()
    cur.executescript(student_sql)
    cur.execute("SELECT * FROM students WHERE id = 2;")
    result = cur.fetchone()
    assert result is None, f"Студент с id=2 должен быть удален, найдено {result}"
