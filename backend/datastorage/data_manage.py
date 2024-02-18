from datastorage.database_query import MongodbQuery

import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

class DataManage:
    def __init__(self):
        self.db = self.database_connection()

    def database_connection(self):
        """
        Establishes a connection to the MongoDB database using environment variables.

        Returns:
            MongodbQuery: Database connection object.
        """
        try:
            load_dotenv()
            db_user = os.getenv("DB_USER")
            db_pw = os.getenv("DB_PW")
            db_name = os.getenv("DB_NAME")
            collection_name = os.getenv("COLLECTION_NAME")
            return MongodbQuery(db_name=db_name, collection_name=collection_name, username=db_user, password=db_pw)
        except Exception as e:
            print(f"Error connecting to database: {e}")
            return None

    def store_news(self, news):
        """
        Stores news items in the database.

        Args:
            news (list): List of news items to be stored.

        Returns:
            MongodbQuery: Database connection object.
        """
        if news:
            for item in news:
                self.db.update_one(item)
        return self.db

    def calculate_start_date_from_range(self, time_range):
        """
        Calculates the start date based on the given time range.

        Args:
            time_range (str): Time range in the format "Xd" where X is the number of days.

        Returns:
            datetime: Start date.
        """
        try:
            days = int(time_range[:-1])
            current_date = datetime.now()
            start_date = current_date - timedelta(days=days)
            return start_date
        except ValueError:
            print("Invalid time range format. Please use 'Xd' format where X is the number of days.")
            return None

    def filter_by_period(self, time_range):
        """
        Filters news items based on the specified time range.

        Args:
            time_range (str): Time range in the format "Xd" where X is the number of days.

        Returns:
            list: List of news items filtered by the specified time range.
        """
        start_date = self.calculate_start_date_from_range(time_range)

        if start_date:
            query = {"published_date": {"$gte": start_date}}
            news_items = list(self.db.find(query))

            serialized_news = []
            for item in news_items:
                published_date = item.get('published_date')
                date_string = published_date.strftime("%Y-%m-%d") if published_date else None

                serialized_item = {
                    'ID': str(item.get('ID', '')),
                    'title': item.get('title', ''),
                    'level': item.get('level', 1),
                    'url': item.get('url', ''),
                    'publisher': item.get('publisher', ''),
                    'published_date': date_string
                }
                serialized_news.append(serialized_item)

            return serialized_news
        return None
