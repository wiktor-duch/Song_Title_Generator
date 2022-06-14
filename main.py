"""This module is the main class"""

from exceptions import RandomWordAPIException
from random_word_api_handler import RandomWordAPIHandler
import sys
from visualization import display_words

if __name__ == "__main__":
    print("Song Title Generator\n")

    # Ask the user for number of random words
    while True:
        try:
            num_words = int(input("How many different words would you like to generate [5-20]? ").strip())
            if num_words >= 5 and num_words <= 20:
                break
            else:
                print("Entered number must be between 5 and 20!")
        except ValueError:
            print('You must enter a number between 5 and 20!')

    # Get the required number of random words from the Random Word API
    while True:
        try:
            random_words = RandomWordAPIHandler().get_random_words(num_words)
            break
        except RandomWordAPIException:
            # Ask the user to try again
            print("\nERROR: An error occured when communicating with Random Word API.\n")
            answer = input("Would you like to try again [yes/no]? ")
            
            # If the answer is negative, exit the application
            if answer not in ["Yes", "yes", "Y", "y"]:
                sys.exit()

    # Display the words to the user
    display_words(random_words)