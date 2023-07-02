import json
import requests
import psycopg2


def get_hh(employees_id):
    """
    Функция заполняет БД по id компании, и берет последние 10 вакансий которые были опубликованы компанией
    :param employees_id: id компании с НН
    """

    # Задаем параметры для api запроса
    params = {
        'employer_id': employees_id,
        'area': 1,
        'page': 0,
        'per_page': 10
    }

    # api запрос для получения информации о компании
    req_1 = requests.get(f'https://api.hh.ru/employers/{employees_id}')
    data_1 = req_1.content.decode()
    req_1.close()
    employer_info = json.loads(data_1)

    # api запрос для получения информации о вакансиях компании
    req_2 = requests.get('https://api.hh.ru/vacancies', params)
    data_2 = req_2.content.decode()
    req_2.close()
    vacancy_list = json.loads(data_2)

    # Подключаемся к БД
    with psycopg2.connect(host="localhost", database="Vacancys", user="postgres", password="Denis.melnik96") as conn:
        with conn.cursor() as cur:

            # Заполняем БД информацией о компании
            cur.execute('INSERT INTO employees VALUES (%s, %s, %s)',
                        (employees_id, # id компании
                         employer_info['name'], # Название компании
                         employer_info['alternate_url'])) # Ссылка на НН

            # Запускаем цикл для получения информации о вакансиях
            for vacancy in vacancy_list['items']:

                # Получаем зарплату
                try:
                    salary = vacancy['salary']['from']
                except TypeError:
                    salary = 0
                # Заполняем БД информацией о вакансиях
                cur.execute('INSERT INTO vacancys VALUES (%s, %s, %s, %s, %s, %s)',
                            (vacancy['id'], # id вакансии
                             employees_id, # id компании
                             vacancy['name'], # Название вакансии
                             vacancy['alternate_url'], # Ссылка на НН
                             salary, # Зарплата
                             f"{vacancy['snippet']['requirement']}\n" # Описание вакансии
                             f"{vacancy['snippet']['responsibility']}"))

    conn.close()
