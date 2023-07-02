import psycopg2


class DBManager:
    """
    Класс для получения информации из баз данных
    """

    def __init__(self, database):

        self.database = database

    def get_companies_and_vacancies_count(self):
        """
        Выводик название компаний и кол-во их вакансий
        """
        with psycopg2.connect(host="localhost", database=self.database, user="postgres", password="Denis.melnik96") as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT employe_name, count(*) FROM public.employees '
                            'JOIN public.vacancys USING (employe_id) '
                            'group by employe_name')
                rows = cur.fetchall()
                print('Название компании, кол-во вакансий.')
                for row in rows:
                    print(row)
        conn.close()

    def get_all_vacancies(self):
        """
        Выводит список всех вакансий
        """
        with psycopg2.connect(host="localhost", database=self.database, user="postgres", password="Denis.melnik96") as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT employe_name, vacancy_name, salary, vacancy_url FROM vacancys '
                            'LEFT JOIN employees USING(employe_id)')
                rows = cur.fetchall()
                print('Компания, название должности, зарплата от, ссылка на вакансию.')
                for row in rows:
                    print(row)

        conn.close()

    def get_avg_salary(self):
        """
        Выводит среднее значение зарплаты
        """

        with psycopg2.connect(host="localhost", database=self.database, user="postgres", password="Denis.melnik96") as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT AVG(salary) FROM vacancys '
                            'WHERE salary <> 0')
                rows = cur.fetchall()
                print('Средняя заработная плата: ')
                print(rows)
        conn.close()

    def get_vacancies_with_higher_salary(self):
        """
        Выводит список вакансий с заплатой выше среднего значения
        """
        with psycopg2.connect(host="localhost", database=self.database, user="postgres", password="Denis.melnik96") as conn:
            with conn.cursor() as cur:
                cur.execute('SELECT AVG(salary) FROM vacancys '
                            'WHERE salary <> 0')
                rows = cur.fetchall()
                print('Средняя заработная плата: ')
                print(rows)
                cur.execute('SELECT vacancy_name, salary, vacancy_url FROM vacancys '
                            'WHERE salary > (select avg(salary) from vacancys)')
                rows = cur.fetchall()
                print('Название должности, зарплата от, ссылка на вакансию.')
                for row in rows:
                    print(row)
        conn.close()

    def get_vacancies_with_keyword(self):
        """
        Возвращает список вакансий, в назване которых имеется ключевое слово
        """
        user_word = input('Укажите одно ключевое слово для поиска: ')
        with psycopg2.connect(host="localhost", database=self.database, user="postgres", password="Denis.melnik96") as conn:
            with conn.cursor() as cur:
                cur.execute(f"SELECT vacancy_name, salary, vacancy_url FROM vacancys "
                            f"WHERE LOWER(vacancy_name) like ('%{user_word.lower()}%')")
                rows = cur.fetchall()
                print('Название должности, зарплата от, ссылка на вакансию.')
                for row in rows:
                    print(row)
        conn.close()
