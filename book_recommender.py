"""A template for a python script deliverable for INST326.

Authors: Trent Williams, Melissa Kavege, Kai Jung
Assignment: Final Project
Date: 4_15_2022

Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import sys
import argparse

class Book:
    """A class to represent a Book object.
    
    Attributes:
        title (string): The title of a book.
        author (string): The author of a book.
        genre (tuple of strings): A tuple containing the different genres of a book.
        avg_rating (float): The avg_rating for a book based on goodreads reviews.
        length (string): The length of a book either being 'short' or 'long' based on page count.
    """
    def __init__(self, title, author, genre, avg_rating, length):
        """Initializes a Book object.
        
        Args:
            title (string): See class documentation.
            author (string): See class documentation.
            genre (tuple of strings): See class documentation.
            avg_rating (float): See class documentation.
            length (string): See class documentation.
        """
        
class Recommender:
    """A class for holding responses from the user about their book preferences.
    
        Attributes:
            preferred_author (String): User response to preferred author question
            preferred_genre (String): User response from terminal about their favorite genres
            preferred_rating (float): User response from terminal about their preferred rating (1 - 5)
            preferred_length (String): User response from terminal about preferred length of a book (short or long)
    """

def main(parameter1, parameter2):
    pass

def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as arguments
    
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('required', type=float, help='This is an example of a required argument.')
    parser.add_argument('--optional', '-o', type=int, default=12, help='This is an example of an optional argument')  
    
    args = parser.parse_args(args_list)

    return args

data = pd.read_csv(r"C:books.csv")

descriptions = data['title'] +' '+ data['author'] + ' ' + data['genre'] +' '+ data['ratings'] +' '+ data['pages']
""""""

if __name__ == "__main__":
    
    arguments = parse_args(sys.argv[1:])
    
    main(arguments.required, arguments.optional)


