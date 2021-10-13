from hh_vacancy_storage_mongo import HHVacancyStorageMongo
from vacancy_viewer import VacancyViewer

search_text = 'php'  # input('Введите должность: ')
min_salary = 100000  # int(input('Введите минимальную зарплату: '))

storage = HHVacancyStorageMongo()

vacancies = storage.find(search_text, min_salary)

VacancyViewer.print(vacancies)
