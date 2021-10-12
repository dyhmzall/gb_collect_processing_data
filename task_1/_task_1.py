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

import json
from bs4 import BeautifulSoup as bs
import requests

SOURCE = 'hh.ru'

text = input('Введите должность: ')
count = int(input('Введите количество просматриваемых страниц: '))

base_url = f'https://hh.ru/search/vacancy?area=&fromSearchLine=true&st=searchVacancy&text={text}'

# добавим заголовок, чтобы обмануть hh
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15'
}

result = []

for i in range(0, count):
    url = f'{base_url}&page={i}'
    response = requests.get(url, headers=headers).text

    soup = bs(response, 'html.parser')
    items = soup.find_all(attrs={'data-qa': 'vacancy-serp__vacancy-title'})

    for item in items:

        if item.parent.parent.parent.parent.next_sibling is not None:
            salary = item.parent.parent.parent.parent.next_sibling.contents[0].contents[0].string
        else:
            salary = 'После собеседования'

        result.append({
            'title': item.text,
            'url': item['href'],
            'salary': salary,
            'source': SOURCE
        })

# сохраним для дальнейшего анализа
with open(f'hh.ru.{text}.json', 'w', encoding='utf-8') as f:
    json.dump(result, f)

# вывод
for i, item in enumerate(result):
    print(i + 1, ') ', item['title'], item['salary'], item['url'])

# для примера получены вакансии по запросу "php" и "python"
