from datastorage.data_manage import DataManage
from datastorage.database_query import MongodbQuery

from unittest import TestCase

class TestStoreNews(TestCase):
    def setUp(self):
        self.storenews = DataManage()

    def test_store_news(self):
        news = [{
                'title':'title 1',
                'url':'www.google.com',
                'publisher':'google',
                'published_date':'2024-2-8'
            }]
        db = self.storenews.store_news(news)
        self.assertTrue(isinstance(db,MongodbQuery))
        self.assertTrue(len(db.find({'title':'title 1'}))>0)

