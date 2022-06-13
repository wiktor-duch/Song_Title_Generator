"""This module is responsibile for handling Random Word API's responses."""

from __future__ import annotations
from typing import List
import requests
from exceptions import RandomWordAPIException

class RandomWordAPIHandler:
    def __init__(self) -> None:
        pass

    def get_random_words(self, num:int) -> List[str]:
        # Query the Random Word API
        response = requests.get("https://random-word-api.herokuapp.com/word?number=" + str(num))
        
        # Check if the query was successful
        if response.status_code != 200:
            raise RandomWordAPIException(f"Error: Random Words API query returned {response.status_code}")

        return response.json()