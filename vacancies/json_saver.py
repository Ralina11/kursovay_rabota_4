import json
from typing import Optional
from vacancies.vacancies import Vacancy, VacancyEncoder
from os.path import exists

"""Класс для работы с данными о вакансиях"""
class Saver:

    def __save_json(self, data, filename="vac.json"):
        """Добавляет вакансии в файл 'vac.json'"""
        with open(filename, 'w') as file:
            text = json.dumps(data, cls=VacancyEncoder, ensure_ascii=False)
            file.write(text)

    def __read_json(self, filename="vac.json") -> list[Vacancy]:
        """Считывает вакансии с файл 'vac.json' """
        with open(filename, 'r') as file:
            data: list[dict] = json.loads(file.read())
            result_list = []
            for item in data:
                result_list.append(self.__serialize(item))
            return result_list

    def __serialize(self, item: dict) -> Vacancy:
        """Задает нужные нам поля для создания экземпляра класса"""
        return Vacancy(
            name=item['name'],
            url=item['url'],
            employer_name=item['employer_name'],
            town=item['town'],
            salary_from=item['salary_from'],
            salary_to=item['salary_to'],
            salary_currency=item['salary_currency']
        )

    def add_vacancy(self, data: list[dict]) -> None:
        """Добавляет вакансии в файл 'vac.json'"""
        if exists("vac.json"):
            old_data = self.__read_json()
        else:
            old_data = []
        new_data = []
        for item in data:
            new_data.append(self.__serialize(item))
        self.__save_json(new_data + old_data)

    def find_by_name(self, name: str, filename="vac.json") -> Optional[list[Vacancy]]:
        """Находит в файле 'vac.json' вакансии по имени"""
        data = self.__read_json(filename=filename)
        result_list = []
        for item in data:
            if name.lower() in item.name.lower():
                result_list.append(item)
        return result_list


    def get_vacancies_by_salary(self, sallary_min: int, filename="vac.json") -> list[Vacancy]:
        """Находит в файле 'vac.json' вакансии по зарплате """
        data = self.__read_json(filename=filename)
        result_list = []
        for item in data:
            if item.salary_from >= sallary_min:
                result_list.append(item)
        return result_list if result_list else None

    def get_delete_vacancy(self, word_name: str, filename="vac.json") -> list[Vacancy]:
        """Удаляет в файле 'vac.json' вакансии по имени"""
        data = self.__read_json(filename=filename)
        deleted_list = []
        for item in data:
            if word_name.lower() in item.name.lower():
                deleted_list.append(item)
                data.remove(item)
        return deleted_list



