"""
Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев
для конкретного пользователя, сохранить JSON-вывод в файле *.json.
"""

import json
import requests

USER = 'dyhmzall'
ENDPOINT = f'/users/{USER}/repos'
URL = 'https://api.github.com'
FILENAME = 'task_1.json'

response = requests.get(f'{URL}{ENDPOINT}')
repositories = json.loads(response.text)

# выведем только названия репозиториев
for repository in repositories:
    print(repository['name'])

# сохраним всю доступную информацию о репозиториях
with open(FILENAME, 'w', encoding='utf-8') as f:
    json.dump(repositories, f)
