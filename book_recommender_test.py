from book_recommender import Recommender, Book

def test_book_build():
    book1 = Book("Harry Potter and the Half-Blood Prince (Harry Potter #6)", "J.K. Rowling", 4.57, "long")
    assert(book1.compare("J.K. Rowling", 5, "long") == 3)

def test_recommender_build():
    recommender = Recommender()
    recommendation1 = recommender.recommendation("J.K. Rowling", 5, "long")
    assert(recommendation1 != None)
    assert (len(recommendation1) > 0)
    assert(recommendation1[0].title == "Harry Potter and the Half-Blood Prince (Harry Potter #6)")

if __name__ == "__main__":
    test_book_build()
    test_recommender_build()
