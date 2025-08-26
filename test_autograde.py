import sqlite3

# Подключаемся к временной базе
conn = sqlite3.connect(":memory:")
cur = conn.cursor()

# Создаем таблицу и вставляем начальные данные
cur.execute("CREATE TABLE students (id INTEGER PRIMARY KEY, name TEXT, age INTEGER);")
cur.execute("INSERT INTO students (id, name, age) VALUES (1, 'Alice', 20);")
cur.execute("INSERT INTO students (id, name, age) VALUES (2, 'Bob', 21);")
cur.execute("INSERT INTO students (id, name, age) VALUES (3, 'Charlie', 23);")

# Загружаем SQL студента
with open("starter.sql") as f:
    student_sql = f.read()

# Выполняем SQL студента
try:
    cur.executescript(student_sql)
except Exception as e:
    print("Ошибка в SQL:", e)
    exit(1)

# Проверка обновления
cur.execute("SELECT name, age FROM students WHERE id = 1;")
result = cur.fetchone()
assert result == ("Alice_updated", 22), f"Ожидалось ('Alice_updated', 22), получено {result}"

# Проверка удаления
cur.execute("SELECT * FROM students WHERE id = 2;")
result = cur.fetchone()
assert result is None, f"Студент с id=2 должен быть удален, найдено {result}"

print("Все проверки пройдены!")