from TvShows.config.mysqlconnection import connectToMySQL
from TvShows import app
from TvShows import DATABASE
from flask import flash
from TvShows.models.model_index import Index


class Dashboard:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date = data['date']
        self.under_thirty = data['under_thirty']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.index_id = data['index_id']
        self.indexes = []

    @classmethod
    def create_show(cls, data):
        query = ""
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def show_all(cls):
        query = ""
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_shows = []
            for recipe in results:
                all_shows.append(cls(recipe))
            return all_shows
        return []
