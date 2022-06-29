from TvShows import DATABASE
from TvShows.config.mysqlconnection import connectToMySQL


class AddShow:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.network = data['network']
        self.release_date = data['release_date']
        self.desc = data['desc']

    @classmethod
    def add_show(cls, data):
        query = ""
        return connectToMySQL(DATABASE).query_db(query, data)
