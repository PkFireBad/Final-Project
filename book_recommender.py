"""A template for a python script deliverable for INST326.

Authors: Trent Williams, Melissa Kavege, Kai Jung
Assignment: Final Project
Date: 4_15_2022

Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

import sys
import argparse
import csv

""" A class for holding responses from the user about their book preferences.
        Attributes:
            preferred_author (String): User response to preferred author question
            preferred_genre (String): User response from terminal about their favorite genres
            preferred_rating (float): User response from terminal about their preferred rating (1 - 5)
            preferred_length (String): User response from terminal about preferred length of a book (short or long) 
"""
class Recommender:
    def __init__(self):
        self.book_list = {"Harry Potter and the Half-Blood Prince (Harry Potter  #6)": ["J.K. Rowling/Mary GrandPré", "4.57", "652", "Scholastic Inc."],
                     "The Ultimate Hitchhiker's Guide: Five Complete Novels and One Story (Hitchhiker's Guide to the Galaxy  #1-5)": ["Douglas Adams", "4.38", "815", "Gramercy Books"],
                     "A Short History of Nearly Everything": ["Bill Bryson", "4.21", "544", "Broadway Books"],
                     "J.R.R. Tolkien 4-Book Boxed Set: The Hobbit and The Lord of the Rings": ["J.R.R. Tolkien", "4.59", "1728", "Ballantine Books"],
                     "Hatchet (Brian's Saga  #1)": ["Gary Paulsen", "3.72", "208", "Atheneum Books for Young Readers: Richard Jackson Books"]}       
        self.books = list()
        for book in self.book_list:
            self.books.append(Book(book, self.book_list[book][0], self.book_list[book][1], self.book_list[book][2]))
    
class Book:
    """A class to represent a Book object.
    
    Attributes:
        title (string): The title of a book.
        author (string): The author of a book.
        genre (tuple of strings): A tuple containing the different genres of a book.
        avg_rating (float): The avg_rating for a book based on goodreads reviews.
        length (string): The length of a book either being 'short' or 'long' based on page count.
    """
    def __init__(self, title, author, avg_rating, length):
        #See class documentation
        self.title = title
        self.author = author
        #self.genre = genre
        self.avg_rating = avg_rating
        self.length = length
            
def main(parameter1, parameter2):
    new_Recommender = Recommender()
    print(new_Recommender.books[0].length)
    
def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as arguments
    
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """
    
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--optional', type=float, help='This is an example of a required argument.')
    parser.add_argument('--optional', '-o', type=int, default=12, help='This is an example of an optional argument')  
    
    args = parser.parse_args(args_list)

    return args

if __name__ == "__main__":
    main(None, None)
