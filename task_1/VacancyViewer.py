class VacancyViewer:

    @staticmethod
    def print(vacancies):
        for i, vacancy in enumerate(vacancies):
            print(i + 1, ') ', vacancy['title'], vacancy['salary_from'], '-', vacancy['salary_to'], vacancy['url'])
