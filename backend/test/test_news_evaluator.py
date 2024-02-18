import unittest
from dataanalysis.news_evaluator import NewsEvaluator

class TestNewsEvaluator(unittest.TestCase):
    def setUp(self):
        self.keywords_file = "testkeywords.txt"
        self.evaluator = NewsEvaluator(self.keywords_file)

    def test_load_keywords(self):
        expected_keywords = {"keyword1", "keyword2", "keyword3"}
        self.assertEqual(self.evaluator.keywords, expected_keywords)

    def test_evaluate_importance(self):
        item_no_keywords = {'title': 'This is a test title with no keywords'}
        self.assertEqual(self.evaluator.evaluate_importance(item_no_keywords), 1)

        item_one_keyword = {'title': 'This is a test title with keyword1'}
        self.assertEqual(self.evaluator.evaluate_importance(item_one_keyword), 2)

        item_three_keywords = {'title': 'This is a test title with keyword1  keyword2  and keyword3'}
        self.assertEqual(self.evaluator.evaluate_importance(item_three_keywords), 3)
