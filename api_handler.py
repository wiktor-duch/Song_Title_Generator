"""This module handles querying MusicBrainz and Random Word APIs."""

from __future__ import annotations
import requests
from typing import List, Dict
from exceptions import MusicBrainzAPIException, RandomWordAPIException

def get_songs(words:List[str]) -> Dict:
    results = dict()
    title_list = list() # Keeps track of titles and duplicates

    for word in words:
        result = dict()
        response = requests.get(f"https://musicbrainz.org/ws/2/recording/?query=recording:{word}&limit=25&fmt=json")

        if response.status_code == 200:
            count = response.json().get("count")
            # Check if any results found
            if count == 0:
                results[word] = "No recording found!"
            else:
                num = 0
                allDuplicates = False
                while True:
                    # Get title
                    title = response.json().get("recordings")[num].get("title")
                    # Check for duplicates
                    if title not in title_list:
                        break
                    elif num >= count or num >= 25: # Exceed matches or limit
                        allDuplicates = True
                        break

                    num += 1
                
                if allDuplicates:
                    results[word] = "Only duplicates found!"
                else:
                    # Add title
                    title_list.append(title)
                    result["title"] = title

                    # Get artists
                    if "artist-credit" in response.json().get("recordings")[num].keys():
                        artists = list()
                        for i in range(len(response.json().get("recordings")[num].get("artist-credit"))):
                            artists.append(response.json().get("recordings")[num].get("artist-credit")[i].get("name"))
                        result["artists"] = artists
                    else:
                        result["artists"] = "None"

                    # Get album
                    if ("releases" in response.json().get("recordings")[num].keys()
                        and "title" in response.json().get("recordings")[num].get("releases")[0].keys()):
                        result["album"] = response.json().get("recordings")[num].get("releases")[0].get("title")
                    else:
                        result["album"] = "None"

                    results[word] = result
        else:
            raise MusicBrainzAPIException(f"Error: MusicBrainz API query returned {response.status_code}.")
        
    return results

def get_random_words(num:int) -> List[str]:
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
                return sorted(random_words)
    
    # Raise exception if the for loop has terminated
    raise RandomWordAPIException(f"Error: Could not find the required number of unique words ({num}).")