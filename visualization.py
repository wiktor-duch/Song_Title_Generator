"""This module handles visualization to the user."""

from typing import List, Dict

def display_words(words:List[str]) -> None:
    print("\nRandom words from API are:")
    for i in range(0, len(words)):
        print(f"\t{i+1}: {words[i]}")

def display_songs(songs:Dict) -> None:
    print("\nRecordings found for each word:")
    i = 1
    for entry in songs:
        print(f"  {i}. {entry}:")
        if isinstance(songs.get(entry), str):
            print(f"\t{songs.get(entry)}", end="\n\n")
        else:
            print(f"\tTITLE: {songs.get(entry).get('title')}")
            print(f"\tARTISTS: ", end="")
            print(*songs.get(entry).get('artists'), sep=", ")
            print(f"\tALBUM: {songs.get(entry).get('album')}", end="\n\n")
        i += 1