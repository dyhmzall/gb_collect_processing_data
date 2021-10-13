class VacancyViewer:

    @staticmethod
    def print(vacancies):

        if not vacancies:
            print('Пустой результат')
            return

        for i, vacancy in enumerate(vacancies):
            print(i + 1, ') ', vacancy['title'], vacancy['salary_from'], '-', vacancy['salary_to'], vacancy['url'])
