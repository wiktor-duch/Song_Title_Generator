"""This module handles visualization to the user."""

from typing import List

def display_words(words:List[str]) -> None:
    print("\nRandom words from API are:")
    for i in range(0, len(words)):
        print(f"\t{i+1}: {words[i]}")