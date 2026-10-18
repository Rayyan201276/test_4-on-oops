books = ["Matilda", "harry potter", "wonder", "the jungle book", "charlie"]
copy_counts = [4, 0, 6, 3, 2]

library = {book: count for book, count in zip(books, copy_counts)}
print("Full Library stock:",library)

class Book:
    def __init__(self, title, copies):
        self.title = title
        self.copies = copies

    def show_details(self):
        print(self.title, "Available copies: ", self.copies)



class Library:
    def __init__(self, stock):
        self.stock = stock