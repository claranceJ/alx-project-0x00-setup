
# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#     def __int__(self):
#         return f"The Title {self.title} and the Auther {self.author} who published in {self.year}"
#
# class LibraryBook(Book):
#     def __init__(self, title, author,isbn, copiesAvailable):
#         super().__init__(title,author)
#         self.isbn = isbn
#         self.copiesAvailable = copiesAvailable
#     def borrow_book(self):
#         if self.copiesAvailable > 0:
#             self.copiesAvailable -= 1
#             return f"{self.title} borrowed. Copies left: {self.copiesAvailable}"
#         else:
#             return f"{self.title} borrowed. No copies left"
#
#     def return_book(self):
#         self.copiesAvailable +=1
#         return f"{self.title} returned. Copies left: {self.copiesAvailable}"
#
# #usage example
# book1=LibraryBook("Gifted Hands", "Ben Carson", "20")
# print(book1)
#---------------------FINISH THE ABOVE-----------------------------#

# managing a library system
# parent class
class Book:
    def __init__(self,tittle,author):
        self.tittle=tittle
        self.author=author
    def display_info(self):
        return f"The Tittle {self.tittle},Author {self.author}"
# child class/ derived class

class LibraryBook(Book):
    def __init__(self,tittle,author,isbn,copies_available):
        super().__init__(tittle,author)
        self.isbn=isbn
        self.copies_available=copies_available
    def borrow_book(self):
        if self.copies_available > 0:
            self.copies_available -=1
            return f"{self.tittle} borrowed. Copies left: {self.copies_available}"
        else:
            return f"No of copies  {self.tittle} unavailable"
    def return_book(self):
        self.copies_available +=1

        return f"{self.tittle} returned. Copies left: {self.copies_available}"

# usage example
book1=LibraryBook("Inheritance","Adrian",123456-986,20)

print(book1.display_info())

print(book1.borrow_book())

print(book1.return_book())