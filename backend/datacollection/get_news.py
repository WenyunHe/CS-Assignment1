import warnings
import feedparser
import re
import requests

class GetNews:
    GOOGLE_NEWS_URL = 'https://news.google.com'
    BASE_URL = "{}/rss".format(GOOGLE_NEWS_URL)
    GOOGLE_NEWS_REGEX = r'^http(s)?://(www\.)?news\.google\.com.*'

    def __init__(self, max_results=20, period='30d', start_date=None, end_date=None):
        """
        Initialize the GetNews object.

        Args:
            max_results (int): The maximum number of results to return.
            period (str): The period of time from which you want the news.
            start_date (str): Date after which results must have been published.
            end_date (str): Date before which results must have been published.
        """
        self._max_results = max_results
        self._period = period
        self._start_date = start_date 
        self._end_date = end_date 

    @property
    def max_results(self):
        """
        Get the maximum number of results to return.
        """
        return self._max_results

    @max_results.setter
    def max_results(self, size):
        """
        Set the maximum number of results to return.

        Args:
            size (int): The maximum number of results.
        """
        self._max_results = size
    
    @property
    def period(self):
        """
        Get the period of time from which you want the news.
        """
        return self._period

    @period.setter
    def period(self, period):
        """
        Set the period of time from which you want the news.

        Args:
            period (str): The period of time.
        """
        self._period = period

    @property
    def start_date(self):
        """
        Get the start date for filtering news by date.
        """
        if self._start_date is None:
            return None
        self._period = None
        return self._start_date.strftime("%Y-%m-%d")
    
    @start_date.setter
    def start_date(self, start_date):
        """
        Set the start date for filtering news by date.

        Args:
            start_date (str): The start date.
        """
        if self._end_date and start_date >= self._end_date:
            warnings.warn("End date should be after start date.")
        self._start_date = start_date
    
    @property
    def end_date(self):
        """
        Get the end date for filtering news by date.
        """
        if self._end_date is None:
            return None
        self._period = None
        return self._end_date.strftime("%Y-%m-%d")
    
    @end_date.setter
    def end_date(self, end_date):
        """
        Set the end date for filtering news by date.

        Args:
            end_date (str): The end date.
        """
        if self._start_date and end_date <= self._start_date:
            warnings.warn("End date should be after start date.") 
        self._end_date = end_date
    
    def _ceid(self):
        """
        Construct the time query for Google News URL.

        Returns:
            str: The time query.
        """
        time_query = ''
        if self._start_date or self._end_date:
            if self._period:
                warnings.warn(message=f'\nPeriod ({self.period}) will be ignored in favour of the start and end dates.')
            if self._start_date is not None:
                time_query += '%20after%3A{}'.format(self._start_date)
            if self._end_date is not None:
                time_query += '%20before%3A{}'.format(self._end_date)
        elif self._period:
            time_query += '%20when%3A{}'.format(self._period)
        return time_query + '&hl=en-US&gl=US&ceid=US:en'
   
    def _process(self, item):
        """
        Process each news item.

        Args:
            item (dict): The news item.

        Returns:
            dict or None: Processed news item or None if processing fails.
        """
        url = item.get('link')
        if re.match(self.GOOGLE_NEWS_REGEX, url):
            url = requests.head(url).headers.get('location', url)
        if url:
            return {
                'title': item.get("title", ""),
                'url': url,
                'publisher': item.get("source", "").get("title", ""),
                'published_date': item.get("published", "")
            }
        return None   
        
    def _get_news(self, query):
        """
        Get news data from the Google News RSS feed based on the provided query.

        Args:
            query (str): The query string for searching news.

        Returns:
            list: List of processed news items.
        """
        url = self.BASE_URL + query + self._ceid()
        try:
            feed_data = feedparser.parse(url)
            return [self._process(item) for item in feed_data.entries[:self._max_results] if item]
        except Exception as e:
            print("Error fetching news:", e)
            return []
        
    def get_news(self, key):
        """
        Get news based on the provided keyword.

        Args:
            key (str): The keyword to search for.

        Returns:
            list: List of news items.
        """
        if key:
            key = "%20".join(key.split(" "))
            query = '/search?q={}'.format(key)
            return self._get_news(query)
        warnings.warn("Enter valid key.")   
        return [] 