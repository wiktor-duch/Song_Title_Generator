import imp
"""This module is the main class"""

from random_word_api_handler import RandomWordAPIHandler

if __name__ == "__main__":
    random_words = RandomWordAPIHandler().get_random_words(10)
    print(random_words)
