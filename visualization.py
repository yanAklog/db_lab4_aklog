import psycopg2
import matplotlib.pyplot as plt

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

def execute_and_visualize_query(connection, query, visualization_type):
    with connection.cursor() as cursor:
        cursor.execute(query)
        data = cursor.fetchall()

        if visualization_type == "bar":
            labels, values = zip(*data)
            plt.bar(labels, values)
            plt.xlabel('Категорії' if "App" in query else 'Типи жанрів' if "App_Genre" in query else 'Категорії')
            plt.ylabel('Кількість застосунків' if "App" in query else 'Відсоткове співвідношення' if "App_Genre" in query else 'Середній розмір застосунку (МБ)')
            plt.title('Кількість додатків у кожній категорії')
            plt.show()

        elif visualization_type == "pie":
            labels, percentages = zip(*data)
            plt.pie(percentages, labels=labels, autopct='%1.1f%%')
            plt.title('Відсоткове співвідношення жанрів (задіяних)')
            plt.show()

        elif visualization_type == "plot":
            labels, avg_sizes = zip(*data)
            plt.plot(labels, avg_sizes, marker='o')
            plt.xlabel('Категорії')
            plt.ylabel('Середній розмір застосунку (МБ)')
            plt.title('Середній розмір програми для кожної категорії')
            plt.show()

if __name__ == "__main__":
    try:
        connection = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
        execute_and_visualize_query(connection, query_1, "bar")
        execute_and_visualize_query(connection, query_2, "pie")
        execute_and_visualize_query(connection, query_3, "plot")
    except Exception as e:
        print(f"Помилка: {e}")
    finally:
        if connection:
            connection.close()
