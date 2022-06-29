from TvShows import DATABASE
from TvShows.config.mysqlconnection import connectToMySQL


class EditShow:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.network = data['network']
        self.release_date = data['release_date']
        self.desc = data['desc']


    @classmethod
    def edit_show(cls,data):
        query =""
        return connectToMySQL(DATABASE).query_db(query,data)

