from datacollection.get_news import GetNews
from datastorage.data_manage import DataManage
from dataanalysis.preprocess import PreProcess
from dataanalysis.news_evaluator import NewsEvaluator

def fetch_store_news(key,keywords_file):
    """
    Fetches news data, evaluates its importance, preprocesses it, and stores it in the database.

    Args:
        key (str): The keyword to search for news.
        keywords_file (str): The path to the keywords file.

    Returns:
        None
    """
    getnews = GetNews()
    news = getnews.get_news(key)
    preprocess = PreProcess()
    evaluator = NewsEvaluator(keywords_file)
    new_news = []
    for item in news:
        important_level = evaluator.evaluate_importance(item)
        new_item = {
            'ID': preprocess.generate_unique_id(item),
            'title': preprocess.title_truncate(item),
            'level': important_level,
            'url': item['url'],
            'publisher': item['publisher'],
            'published_date': preprocess.get_published_date(item)
        }
        new_news.append(new_item)
    
    data_manager = DataManage()
    data_manager.store_news(new_news)
    
    return data_manager
    
