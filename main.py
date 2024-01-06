import psycopg2

username = 'aklog_yan'
password = 'aBc'
database = 'db_lab3'
host = 'localhost'
port = '5432'

# Запит 1: Кількість додатків у кожній категорії
query_1 = '''
    SELECT category_name, COUNT(*) as app_count
    FROM App
    GROUP BY category_name;
'''

# Запит 2: Відсоткове співвідношення жанрів
query_2 = '''
    SELECT genre_type, COUNT(*) * 100.0 / (SELECT COUNT(*) FROM App_Genre) AS genre_percentage
    FROM App_Genre
    GROUP BY genre_type;
'''

# Запит 3: Середній розмір програми для кожної категорії
query_3 = '''
    SELECT category_name, AVG(app_size) as avg_app_size
    FROM App
    GROUP BY category_name;
'''

def execute_and_print_query(connection, query, query_description):
    with connection.cursor() as cursor:
        cursor.execute(query)
        print(f"\n{query_description}\n")
        for row in cursor.fetchall():
            print(row)

if __name__ == "__main__":
    try:
        connection = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
        execute_and_print_query(connection, query_1, "Результати запиту 1: Кількість додатків у кожній категорії")
        execute_and_print_query(connection, query_2, "Результати запиту 2: Відсоткове співвідношення жанрів")
        execute_and_print_query(connection, query_3, "Результати запиту 3: Середній розмір додатку для кожної категорії")
    except Exception as e:
        print(f"Помилка: {e}")
    finally:
        if connection:
            connection.close()