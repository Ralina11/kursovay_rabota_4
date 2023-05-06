import requests
from abc import ABC, abstractmethod

class ParentApiClass(ABC):
    """Родительский класс, для классов, которые работают с API"""

    @abstractmethod
    def get_request(self, key_word, per_page):
        pass


class GetVacHH(ParentApiClass):
    """Получаем все вокансии из hh"""

    def __init__(self):
        self.list_vacancies = []

    @property
    def get_list_vacancies(self) -> list:
        return self.list_vacancies

    def get_request(self, key_word, per_page):
        url = "https://api.hh.ru/vacancies"
        params = {
            "text": key_word,
            "page": 1,
            "per_page": per_page,
        }
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                for vac in response.json()['items']:
                    try:
                        salary_from = vac["salary"]["from"]
                        if salary_from is None:
                            salary_from = 0
                    except (KeyError, TypeError):
                        salary_from = 0
                    try:
                        salary_to = vac["salary"]["to"]
                        if salary_to is None:
                            salary_to = 0
                    except (KeyError, TypeError):
                        salary_to = 0
                    try:
                        salary_currency = vac["salary"]["currency"]
                        if salary_currency is None:
                            salary_currency = 0
                    except (KeyError, TypeError):
                        salary_currency = 0
                    self.list_vacancies.append(
                        {
                            "name": vac["name"],
                            "url": vac["url"],
                            "employer_name": vac["employer"]["name"],
                            "town": vac["area"]["name"],
                            "salary_from": salary_from,
                            "salary_to": salary_to,
                            "salary_currency": salary_currency
                        })

            return self.list_vacancies
        except requests.ConnectionError as e:
            print(e)
            print("Ошибка при запросе. Ошибка соединения")
        return []


class GetVacSJ(ParentApiClass):
    """Класс для взаимодейстивя с SuperJobAPI, получаем все вакансии superJob"""

    def __init__(self):
        self.list_vacancies = []

    @property
    def get_list_vacancies(self) -> list:
        return self.list_vacancies

    def get_request(self, key_word, per_page):
        url = 'https://api.superjob.ru/2.0/vacancies/'
        auth_data = {
            'X-Api-App-Id': "v3.r.137524789.65f29a249836c544af3c91674aa96e400e45a09b.e556119a4bea4e843f1b174da7b38d0a9689d757"}
        params = {
            "keyword": key_word,
            "page": 1,
            "count": per_page,
        }
        try:
            response = requests.get(url, headers=auth_data, params=params)
            if response.status_code == 200:
                for vac in response.json()['objects']:
                    try:
                        salary_from = vac["salary_from"]
                    except (KeyError, TypeError):
                        salary_from = 0
                    try:
                        salary_to = vac["salary_to"]
                    except (KeyError, TypeError):
                        salary_to = 0
                    self.list_vacancies.append(
                                            {
                                                "name": vac["profession"],
                                                "url": vac["link"],
                                                "employer_name": vac["firm_name"],
                                                "town": vac["town"]["title"],
                                                "salary_from": salary_from,
                                                "salary_to": salary_to,
                                                "salary_currency": vac["currency"]
                                                })
            return self.list_vacancies
        except requests.ConnectionError as e:
            print(e)
            print("Ошибка при запросе. Ошибка соединения")
        return []
