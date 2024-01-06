
-- Вставлення нових даних

INSERT INTO Category (category_name) VALUES
('Entertainment'),
('Productivity'),
('Social'),
('Education'),
('Games'),
('Lifestyle');

INSERT INTO Genre (genre_type) VALUES
('Action'),
('Puzzle'),
('Adventure'),
('Simulation'),
('Strategy'),
('Music');

INSERT INTO App (app_name, app_size, app_price, app_content_rating, category_name) VALUES
('App1', 50, 2.99, 'Everyone', 'Entertainment'),
('App2', 30, 1.99, 'Everyone', 'Productivity'),
('App3', 80, 4.99, 'Teen', 'Social'),
('App4', 40, 3.49, 'Everyone 10+', 'Education'),
('App5', 60, 2.49, 'Adult', 'Games'),
('App6', 45, 3.99, 'Mature 21+', 'Lifestyle'),
('App7', 70, 5.99, 'Adult', 'Games'),
('App8', 35, 2.79, 'Everyone', 'Productivity'),
('App9', 55, 4.49, 'Teen', 'Social'),
('App10', 65, 3.99, 'Mature 17+', 'Games');

INSERT INTO App_Genre (app_name, genre_type) VALUES
('App1', 'Action'),
('App2', 'Puzzle'),
('App3', 'Adventure'),
('App4', 'Simulation'),
('App5', 'Strategy'),
('App6', 'Music'),
('App7', 'Action'),
('App8', 'Puzzle'),
('App9', 'Adventure'),
('App10', 'Strategy');








