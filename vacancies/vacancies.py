from json import JSONEncoder

class Vacancy:
    """Класс вакансий"""
    def __init__(self, name, salary_from, salary_to, url, employer_name, town, salary_currency):
        self.name = name
        self.url = url
        self.employer_name = employer_name
        self.town = town
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.salary_currency = salary_currency

    def __str__(self):
        short_information = f"название компании: {self.employer_name}\n"\
                            f"Url:{self.url}\n"\
                            f"город: {self.town}\n"\
                            f"должность: {self.name}\n"\
                            f"зарплата: От {self.salary_from} до {self.salary_to}, {self.salary_currency}"
        return short_information

    def __le__(self, other):
        """Определяет поведение оператора сравнения «меньше или равно»"""
        return (self.salary_from + self.salary_to) / 2 <= (other.salary_from + other.salary_to) / 2

    def __ge__(self, other):
        """Определяет поведение оператора сравнения «больше или равно»"""
        return (self.salary_from + self.salary_to) / 2 >= (other.salary_from + other.salary_to) / 2


class VacancyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__






