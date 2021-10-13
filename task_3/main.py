"""
1. Развернуть у себя на компьютере/виртуальной машине/хостинге MongoDB и реализовать функцию, записывающую собранные вакансии в созданную БД.
2. Написать функцию, которая производит поиск и выводит на экран вакансии с заработной платой больше введённой суммы.
3. Написать функцию, которая будет добавлять в вашу базу данных только новые вакансии с сайта.
"""

from hh_parser import HHParser
from hh_vacancy_storage_mongo import HHVacancyStorageMongo
from vacancy_viewer import VacancyViewer

search_text = 'php'  # input('Введите должность: ')
page_count = 1  # int(input('Введите количество просматриваемых страниц: '))

parser = HHParser(search_text, page_count)

# спарсим вакансии
vacancies = parser.run()

# сохраним вакансии
storage = HHVacancyStorageMongo()
storage.save(vacancies)

# выведем список вакансий
VacancyViewer.print(vacancies)
