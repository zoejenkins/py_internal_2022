print("Welcome to the bookstore baby")
print("Please enter: \n (A) To Add a book \n (M) To Modify the number of pages of a book \n (L) to Print out the number of pages of a book \n (P) to Print out all books’ titles with their authors and the number of pages \n (Q) to Quit")
books = {'Harry Potter': '12'}
add_book = input("Add a book: ")
add_page = input("How many pages? ")
books[add_book] = add_page
print(books)

def addingfunction(adding):