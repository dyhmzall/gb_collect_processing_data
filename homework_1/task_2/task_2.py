"""
Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл.

Для выполнения задания, используем API платежной системы:
https://www.programmableweb.com/api/alternative-payments
ссылка на само API:
https://alternativepayments.com/developers/API/?shell#creating-a-transaction
"""

import json
import base64
import requests

URL = 'https://api.alternativepayments.com/api/payments'
TEST_API_KEY = 'sk_test_VeQdhVu1P5KmHi3HKas0MjMWv1mv1SaIS1QXFE9S'
FILENAME = 'task_2.json'

# согласно документации - api key это логин, а пароль отсутствует
auth = base64.b64encode(bytes(f'{TEST_API_KEY}:', 'utf-8')).decode('utf-8')
headers = {'Authorization': f'Basic {auth}', 'Content-Type': 'application/json'}
print(headers)

data = {
    'holder': 'John Doe',
    'paymentOption': 'sepa',
    'iban': 'AT85XXXXX0817'
}
response = requests.post(URL, headers=headers, json=data)
print(response.text)

# сохраним всю доступную информацию о репозиториях
with open(FILENAME, 'w', encoding='utf-8') as f:
    json.dump(response.json(), f)

# в файле содержится ошибка о том, что IBAN не корректны, но этот ответ мы считаем успешным,
# так как базовую авторизацию мы прошли и наш запрос даже был взят на анализ
