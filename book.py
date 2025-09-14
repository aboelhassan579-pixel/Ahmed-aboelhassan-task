class Book:
    def __init__(self, title, author, isbn, available=True):
        self.title = title
        self.author = author
        self.__isbn = isbn           
        self.available = available

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Available: {self.available}")

    
    def isbn(self):
        return self.__isbn

    
    def isbn(self, new_isbn):
        self.__isbn = new_isbn
