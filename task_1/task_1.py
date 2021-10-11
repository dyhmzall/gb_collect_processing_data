"""
Необходимо собрать информацию о вакансиях на вводимую должность (используем input или через аргументы)
с сайтов Superjob и HH. Приложение должно анализировать несколько страниц сайта (также вводим через input или аргументы).
Получившийся список должен содержать в себе минимум:
Наименование вакансии.
Предлагаемую зарплату (отдельно минимальную и максимальную).
Ссылку на саму вакансию.
Сайт, откуда собрана вакансия.
По желанию можно добавить ещё параметры вакансии (например, работодателя и расположение).
Структура должна быть одинаковая для вакансий с обоих сайтов. Общий результат можно вывести с помощью dataFrame через pandas.
Можно выполнить по желанию один любой вариант или оба при желании и возможности.
"""

from bs4 import BeautifulSoup as bs
import requests

url = 'https://hh.ru/search/vacancy?area=&fromSearchLine=true&st=searchVacancy&text=php'
# https://bryansk.hh.ru/search/vacancy?area=&fromSearchLine=true&st=searchVacancy&text=php&page=1
# https://bryansk.hh.ru/search/vacancy?area=&fromSearchLine=true&st=searchVacancy&text=php&page=2

# добавим заголовок, чтобы обмануть hh
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15'
}

response = requests.get(url, headers=headers).text

soup = bs(response, 'html.parser')

items = soup.find_all(attrs={'data-qa' : 'vacancy-serp__vacancy-title'})

result = []

for item in items:
    result.append({
        'name':item.text
    })

print(result)
