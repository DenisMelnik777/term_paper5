from utils import get_hh
from DBManager import DBManager


def main():

    # Создаем список id компаний с НН
    employees_id = [3529, 1776381, 3672566, 4300631, 863273, 4392713, 9261916, 936465, 9352347, 2515455]

    # Запускаем цикл для заполнения БД
    for i in employees_id:
        get_hh(i)

    # Создаем экземпляр класса для связи с БД 'Vacancys'
    bd_element = DBManager('Vacancys')

    # Получаем список компаний и количество вакансий
    bd_element.get_companies_and_vacancies_count()

    # Получаем список всех вакансий
    bd_element.get_all_vacancies()

    # Получаем среднюю зарплату
    bd_element.get_avg_salary()

    # Получаем список вакансий, где зарплата выше средней
    bd_element.get_vacancies_with_higher_salary()

    # Получаем список вакансий, где присутствует ключевое слово
    bd_element.get_vacancies_with_keyword()


if __name__ == '__main__':
    main()
