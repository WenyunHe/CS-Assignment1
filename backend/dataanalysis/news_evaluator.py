class NewsEvaluator:
    def __init__(self, keywords_file):
        self.keywords = self.load_keywords(keywords_file)

    def load_keywords(self, keywords_file):
        """
        Load keywords from a file.

        Args:
            keywords_file (str): The path to the keywords file.

        Returns:
            set: A set of keywords.
        """
        with open(keywords_file, 'r', encoding='utf-8') as file:
            return {keyword.strip() for keyword in file}

    def evaluate_importance(self, item):
        """
        Evaluate the importance level of a news title based on keyword matching.

        Args:
            title (str): The title of the news item to evaluate.

        Returns:
            int: The importance level (1 to 5).
        """
        title = item.get('title', '')
        title_lower = title.lower()
        keyword_count = sum(1 for keyword in self.keywords if keyword.lower() in title_lower)
        if keyword_count == 0:
            return 1  
        elif keyword_count <= 2:
            return 2  
        elif keyword_count <= 4:
            return 3  
        elif keyword_count <= 6:
            return 4  
        else:
            return 5  