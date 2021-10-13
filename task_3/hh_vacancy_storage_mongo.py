from pymongo import MongoClient


class HHVacancyStorageMongo:
    HOST = 'localhost'
    PORT = 27017
    DB = 'vacancy'
    COLLECTION = 'vacancy'

    def __init__(self):
        self.client = MongoClient(self.HOST, self.PORT)
        self.db = self.client[self.DB]
        self.collection = self.db[self.COLLECTION]

    def save(self, vacancies):

        for vacancy in vacancies:
            if self.collection.find_one({'url': vacancy['url']}) is None:
                self.collection.insert_one(vacancy)

    def find(self, search_text, min_salary):
        return self.collection.find({
            'search_text': search_text,
            'salary_from': {'$gt': min_salary}
        })
