"""This module handles querying MusicBrainz and Random Word APIs."""

from __future__ import annotations
import requests
from typing import List, Dict
from exceptions import MusicBrainzAPIException

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
                    artists = list()
                    for i in range(len(response.json().get("recordings")[num].get("artist-credit"))):
                        artists.append(response.json().get("recordings")[num].get("artist-credit")[i].get("name"))
                    result["artists"] = artists

                    # Get album
                    result["album"] = response.json().get("recordings")[num].get("releases")[0].get("title")

                    results[word] = result
        else:
            raise MusicBrainzAPIException(f"Error: MusicBrainz API query returned {response.status_code}.")
        
    return results
    
songs = get_songs(["a","zxzcxzxczxvzxvczxczx","b", "a a", "a a a"])
print(songs)
# print(requests.get(f"https://musicbrainz.org/ws/2/recording/?query=recording:zxzcxzxczxvzxvczxczxv&limit=1&fmt=json").json())