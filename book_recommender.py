import sys
import argparse
"""
import csv
import pandas as pd
"""
""" A class for holding responses from the user about their book preferences.
        Attributes:
            preferred_author (String): User response to preferred author question
            preferred_genre (String): User response from terminal about their favorite genres
            preferred_rating (float): User response from terminal about their preferred rating (1 - 5)
            preferred_length (String): User response from terminal about preferred length of a book (short or long)
"""
"""
books_df = pd.read_csv("books.csv")

print(books_df)
"""

class Recommender:
    def __init__(self):
        """
        TODO: This is temporary: Need to make a process for importing csv file and converting each line to a Book object'
        self.book_list = {"Harry Potter and the Half-Blood Prince (Harry Potter  #6)": ["J.K. Rowling/Mary GrandPré", "4.57", "652", "Scholastic Inc."],
                     "The Ultimate Hitchhiker's Guide: Five Complete Novels and One Story (Hitchhiker's Guide to the Galaxy  #1-5)": ["Douglas Adams", "4.38", "815", "Gramercy Books"],
                     "A Short History of Nearly Everything": ["Bill Bryson", "4.21", "544", "Broadway Books"],
                     "J.R.R. Tolkien 4-Book Boxed Set: The Hobbit and The Lord of the Rings": ["J.R.R. Tolkien", "4.59", "1728", "Ballantine Books"],
                     "Hatchet (Brian's Saga  #1)": ["Gary Paulsen", "3.72", "208", "Atheneum Books for Young Readers: Richard Jackson Books"]}      
        self.books = list()
        for book in self.book_list:
            self.books.append(Book(book, self.book_list[book][0], self.book_list[book][1], self.book_list[book][2]))
        """
        self.books = []
        self.books.append(Book("Harry Potter and the Half-Blood Prince (Harry Potter #6)", "J.K. Rowling", 4.57, "long"))
   
    def recommendation(self, author, avg_rating, length):
        """TODO: make smarter ranking structure. For now, assume maximum score is 3
        """
        rankings = [[],[],[],[]]
        for book in self.books:
            score = book.compare(author, avg_rating, length)
            rankings[score].append(book)
        rank = 3
        while (rank>0):
            if (rankings[rank]):
                return rankings[rank]
            else:
                rank-=1
        return null
   
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
   
    def compare(self, author, avg_rating, length):
    #Returns a score (integer) of the match of a book to user's preferences
        score = 0
        if (author == self.author):
            score+=1
        if (self.avg_rating <= avg_rating):
            score+=1
        if (self.length == length):
            score+=1
        return score
   
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
    def books():
        #This function is to read the csv file and be added to a list based on selected elements
        f = open('books.csv')
        csv_f =csv.reader.(f)
        books = []

        f.close()
        
class Recommender:
    
    def __init__(self,book, user_author, user_genre,user_rating,user_length):
        #this is supposed to pass in the attribute from the book class to the recommendation class
        rating_scale = 
        self.book = book
        self.user_author = user_author
        self.user_genre = ()
        self.user_length = ()
        self.user_rating =


    def recommendation(self):
        #This is supposed to append the list of books given to the users based on their preferences
        for book in book_list:
            if book.author == user_author:
                recommendation.append(book)
        for book in book_list:
            if book.genre == user_genre:
                recommendation.append(book)
        for book in book_list:
            if book.rating == user_rating:
                recommendation.append(book)
        for book in book_list:
            if book.length == user_length:
                recommendation.append(book)
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


