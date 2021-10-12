from bs4 import BeautifulSoup
import requests
import re


class HHParser:
    SOURCE = 'hh.ru'
    BASE_URL = 'https://hh.ru/search/vacancy?area=&fromSearchLine=true&st=searchVacancy'
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15'
    }

    def __init__(self, search_text, page_count):
        self.search_text = search_text
        self.page_count = page_count

    def create_url(self, page_number):
        return f'{self.BASE_URL}&text={self.search_text}&page={page_number}'

    def run(self):
        for page_number in range(0, self.page_count):

            response = self.get_response(page_number)

            soup = BeautifulSoup(response, 'html.parser')
            vacancies = soup.find_all(attrs={'data-qa': 'vacancy-serp__vacancy-title'})

            vacancies_params = []

            for vacancy in vacancies:
                vacancies_params.append(
                    self.get_vacancy_params(vacancy)
                )

            return vacancies_params

    def get_response(self, page_number):
        return requests.get(
            self.create_url(page_number),
            headers=self.HEADERS
        ).text

    def get_vacancy_params(self, vacancy):
        salary_from = ''
        salary_to = ''

        if vacancy.parent.parent.parent.parent.next_sibling is not None:

            if vacancy.parent.parent.parent.parent.next_sibling.contents[0].contents[0] == 'до ':
                salary_to = vacancy.parent.parent.parent.parent.next_sibling.contents[0].contents[2]
                salary_to = re.sub('[^\d|\–]', '', salary_to)
            elif vacancy.parent.parent.parent.parent.next_sibling.contents[0].contents[0] == 'от ':
                salary_from = vacancy.parent.parent.parent.parent.next_sibling.contents[0].contents[2]
                salary_from = re.sub('[^\d|\–]', '', salary_from)
            else:
                salary = vacancy.parent.parent.parent.parent.next_sibling.contents[0].contents[0].string
                salary = re.sub('[^\d|\–]', '', salary)
                salary_array = salary.split('–')
                if len(salary_array) == 2:
                    salary_from = salary_array[0]
                    salary_to = salary_array[1]

        return {
            'title': vacancy.text,
            'url': vacancy['href'],
            'salary_from': salary_from,
            'salary_to': salary_to,
            'source': self.SOURCE
        }
