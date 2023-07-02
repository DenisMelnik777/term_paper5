-- Создаем таблицу с вакансиями
CREATE TABLE vacancys
(
vacancy_id int primary key,
employe_id int,
vacancy_name varchar(500),
vacancy_url varchar(500),
salary int,
snippet text
);
-- Создаем таблице с компаниями
CREATE TABLE employees
(
    employe_id   int primary key,
    employe_name varchar(100),
    employe_url  varchar(500)
);

-- Указываем зависимость внешнего ключа
ALTER TABLE vacancys ADD CONSTRAINT fk_employees_vacancys FOREIGN KEY (employe_id) REFERENCES employees(employe_id) ON DELETE CASCADE
