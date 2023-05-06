from vacancies.get_vac import GetVacHH, GetVacSJ
from vacancies.json_saver import Saver

def user_interaction():
    """Функция для взаимодействия с пользователем"""

    print("Привет, это парсер по поиску вакансий с двух платформ HH,SJ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: "))
    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()

    """Создаем экземпляры класса Vacancy hh sj"""
    hh = GetVacHH()
    sj = GetVacSJ()

    """Получение вакансий"""
    items = hh.get_request(filter_words, top_n)
    items_sj = sj.get_request(filter_words, top_n)

    """Соханение вакансий в json"""
    hj = Saver()

    """Добавление вакансий"""
    hj.add_vacancy(items)
    hj.add_vacancy(items_sj)

    """Поиск по имени"""
    name = str(input("По какому имени хотите совершить поиск? "))
    while len(hj.find_by_name(name)) == 0:
        name = str(input("Совпадений не найдено, введите другое слово: "))
    for el in hj.find_by_name(name):
        print(el)

    """Сортировка вакансий по минимально допустимой зарплате"""
    salary_min = int(input("Укажите минимально допустимый порог зарплаты: "))
    for i in hj.get_vacancies_by_salary(salary_min):
        print(i)

    """Удаление вакансий по имени"""
    delite_name = str(input("С каким именем вы хотите удалить вакансии?"))
    print("Список удаленных вакансий:\n")
    for i in hj.get_delete_vacancy(delite_name):
        print(i)

if __name__ == "__main__":
    user_interaction()