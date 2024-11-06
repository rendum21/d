# pip install mysql.connector-python
import mysql.connector


connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='student'
)


cursor = connection.cursor()


def create_table():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        age INT
    )
    """
    cursor.execute(create_table_query)
    connection.commit()


def add_record(name, age):
    query = "INSERT INTO users (name, age) VALUES (%s, %s)"
    cursor.execute(query, (name, age))
    connection.commit()


def delete_record(user_id):
    query = "DELETE FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    connection.commit()


def update_record(user_id, new_name, new_age):
    query = "UPDATE users SET name = %s, age = %s WHERE id = %s"
    cursor.execute(query, (new_name, new_age, user_id))
    connection.commit()


def fetch_all_records():
    query = "SELECT * FROM users"
    cursor.execute(query)
    return cursor.fetchall()


create_table()


add_record("John", 25)
update_record(1, "Johnny", 26)
delete_record(2)
records = fetch_all_records()
for record in records:
    print(record)

cursor.close()
connection.close()
