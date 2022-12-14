import uuid

# To create a new Book object and retrieve information to load to Inventory
class Book:
    def __init__(self,ISBN,title,author,genre,publishing_year):
        self.isbn=ISBN
        self.title=title
        self.author=author
        self.genre=genre
        self.publishing_year=publishing_year
    def get_book(self):
        return {
            "ISBN": self.isbn,
            "Title": self.title,
            "Author" : self.author,
            "Genre" : self.genre,
            "PublishingYear" : self.publishing_year
        }

        