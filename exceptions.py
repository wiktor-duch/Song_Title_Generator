"""This module handles exceptions in querying APIs."""

class RandomWordAPIException(Exception):
    """Raised when an error occured when communicating with Random Word API"""

class MusicBrainzAPIException(Exception):
    """Raised when an error occured when searching with MusicBrainz API"""