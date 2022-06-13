"""This module is the main class"""

from exceptions import RandomWordAPIException
from random_word_api_handler import RandomWordAPIHandler
import sys

if __name__ == "__main__":

    while True:
        try:
            random_words = RandomWordAPIHandler().get_random_words(10)
            print(random_words)
            break
        except RandomWordAPIException:
            # Ask the user to try again
            print("\nERROR: An error occured when communicating with Random Word API.\n")
            answer = input("Would you like to try again [yes/no]? ")
            
            # If the answer is negative, exit the application
            if answer not in ["Yes", "yes", "Y", "y"]:
                sys.exit()

    print('the rest of the code')
