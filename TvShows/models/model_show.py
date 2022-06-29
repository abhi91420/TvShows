from TvShows import DATABASE
from TvShows.config.mysqlconnection import connectToMySQL


class Show:
    def __int__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.date = data['date']
        self.desc = data['desc']
        self.posted_by = data['posted_by']

    @classmethod
    def show_info(cls, data):
        query = ""
        return connectToMySQL(DATABASE).query_db(query, data)
