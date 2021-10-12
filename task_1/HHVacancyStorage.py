import json
from HHParser import HHParser


class HHVacancyStorage:

    @staticmethod
    def save(search_text, vacancies):
        with open(f'{HHParser.SOURCE}.{search_text}.json', 'w', encoding='utf-8') as f:
            json.dump(vacancies, f)
