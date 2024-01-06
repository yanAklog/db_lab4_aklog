--1.Кількість застосунків у кожній категорії

SELECT category_name, COUNT(*) as app_count
FROM App
GROUP BY category_name;


--2.Відсоток застосунків, що мають конкретний жанр (для всіх задіяних жанрів)

SELECT genre_type, COUNT(*) * 100.0 / (SELECT COUNT(*) FROM App_Genre) AS genre_percentage
FROM App_Genre
GROUP BY genre_type;


--3.Середній розмір застосунку для кожної категорії

SELECT category_name, AVG(app_size) as avg_app_size
FROM App
GROUP BY category_name;













select * from app

