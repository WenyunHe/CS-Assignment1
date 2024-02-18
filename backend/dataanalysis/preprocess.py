import hashlib
import json
import time
import random
from datetime import datetime

class PreProcess:
    """
    Class for preprocessing items.
    """

    def generate_unique_id(self, item):
        """
        Generate a unique ID for the item.

        Args:
            item (dict): The item to generate ID for.

        Returns:
            code: unique ID
        """
        timestamp = int(time.time() * 1000)
        random_number = random.randint(0, 999999)
        data_str = json.dumps(item) + str(timestamp) + str(random_number)
        unique_id = hashlib.sha256(data_str.encode('utf-8')).hexdigest()
        return unique_id

    def get_published_date(self, item):
        """
        Parse and convert the published date to datetime object.

        Args:
            item (dict): The item containing published date.

        Returns:
            datetime object: published date
        """
        published_str = item.get('published_date')
        if published_str:
            try:
                published_date = datetime.strptime(published_str, '%a, %d %b %Y %H:%M:%S %Z')
            except ValueError:
                return None
            else:
                return published_date
        return None

    def title_truncate(self, item):
        """
        Truncate the title of the item.

        Args:
            item (dict): The item containing the title.

        Returns:
            str: truncated title.
        """
        title = item['title']
        parts = title.rsplit('-', 1)
        return parts[0].strip()
