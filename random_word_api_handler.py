"""This module is responsibile for handling Random Word API's responses."""

from __future__ import annotations
from typing import List
import requests
from exceptions import RandomWordAPIException

class RandomWordAPIHandler:
    def __init__(self) -> None:
        pass

    def get_random_words(self, num:int) -> List[str]:
        random_words = set()

        # Query the Random Word API
        response = requests.get("https://random-word-api.herokuapp.com/word?number=" + str(num))
        
        # Check if the query was successful
        if response.status_code == 200:
            random_words = set(response.json())
        else:
            raise RandomWordAPIException(f"Error: Random Words API query returned {response.status_code}.")

        if len(random_words) >= num:
            return sorted(random_words)
        else:
            # For loop ensures that it does not query API infinitely
            for _ in range(100):
                # Query the Random Word API
                response = requests.get("https://random-word-api.herokuapp.com/word")
                
                # Check if the query was successful
                if response.status_code != 200:
                    raise RandomWordAPIException(f"Error: Random Words API query returned {response.status_code}.")

                random_words.add(response.json()[0])
                
                if len(random_words) >= num:
                    return self.sorted(random_words)
        
        # Raise exception if the for loop has terminated
        raise RandomWordAPIException(f"Error: Could not find the required number of unique words ({num}).")