from datacollection.get_news import GetNews

from unittest import TestCase

class TestGetNews(TestCase):
    def setUp(self):
        self.getnews = GetNews()
    
    def test_get_news(self):
        key = "Apple"
        news = self.getnews.get_news(key)
        self.assertTrue(isinstance(news,list))
        self.assertTrue(len(news)>0)
