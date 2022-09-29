# Welcomes user to library
print("Welcome to the library!")


# Creates a dictionary for all of the books in the library
books = {
  # Nested dictionary of example book
  'Harry Potter': {
    'Author: ' : 'J.K. Rowling',
    'Pages: ' : '600',
    'Genre: ' : 'Fantasy',
    'Year: ' : '2000',
  }
}


def add():
  """
  Function for adding a book to the library
  Takes in values from users inputs, makes sure they are valid within set boundaries, then adds them to the 'books' dictionary as a nested dictionary
  """
  introductions = ['Author: ', 'Pages: ', 'Genre: ', 'Year: ']

  invalid_title = True
  while invalid_title == True:
    title = input("Enter the books' name: ")
    if title in books:
      print("This book already exists in the library")
      invalid_title = True
    elif len(title) < 1 or title.isspace():
      print("The book must have a title")
      invalid_title = True
    else:
      invalid_title = False
      
  invalid_author = True
  while invalid_author == True:
    author = input("Enter the author of {}: ".format(title))
    if any(char.isdigit() for char in author):
      print("Author's name cannot include a number")
      invalid_author = True
    elif len(author) < 1 or author.isspace():
      print("Author must have a name.")
      invalid_author = True
    else:
      invalid_author = False
      
  max_year = 2022
  min_year = 868
  
  invalid_year = True
  while invalid_year == True:
    year = input("Enter the year {} was published: ".format(title))
    try:
      if int(year) > int(max_year):
        print("The year you entered is not valid. Please enter a smaller year")
        invalid_year = True
      elif int(year) < int(min_year):
        print("The earliest book published was in 868 AD. Please enter a larger year.")
        invalid_year = True
      else:
        invalid_year = False
    except ValueError:
      print("The year published must be a number.")
      invalid_year = True  

  invalid_genre = True
  while invalid_genre == True:
    genre = input("Enter the genre of {}: ".format(title))
    if any(char.isdigit() for char in genre):
      print("Genre cannot include a number")
      invalid_genre = True
    elif len(genre) < 1 or genre.isspace():
      print("Genre must have a name.")
      invalid_genre = True
    else:
      invalid_genre = False
  
  max_pages = 3000000
  min_pages = 1
  
  invalid_pages = True
  while invalid_pages == True:
    pages = input("Enter how many pages {} has: ".format(title))
    try:
      if int(pages) > int(max_pages):
        print("ERROR: the book with the most pages has 3 million pages. Please enter a lower value.")
        invalid_pages = True
      elif int(pages) < int(min_pages):
        print("ERROR: Your book can't have less than 1 page")
        invalid_pages = True
      else:
        invalid_pages = False
    except ValueError: 
      print("Your page value must be a number.")
      invalid_pages = True
      
  intro_values = [str(author), str(pages), str(genre), str(year)]
  book_info = dict(zip(introductions,intro_values))
  new_book = {title : book_info}
  books.update(new_book)
  print(books)


def modify():
  """
  Function that lets user access and modify the number of pages in a book of their choice
  """
  max_pages = 3000000
  min_pages = 1
  book_to_modify = str(input("For which book do you want to modify the number of pages? "))
  if book_to_modify in books:
    print(book_to_modify + " currently has " + books[book_to_modify]["Pages: "] + " pages.")
    invalid_pages = True
    while invalid_pages == True:
      new_page_number = input("What do you want to update the number to? ")
      try:
        if int(new_page_number) > int(max_pages):
          print("ERROR: the book with the most pages has 3 million pages. The number you entered was higher than this.")
          invalid_pages = True
        elif int(new_page_number) < int(min_pages):
          print("ERROR: Your book can't have less than 1 page")
          invalid_pages = True
        else:
          books[book_to_modify]["Pages: "] = new_page_number
          print(book_to_modify + " now has " + books[book_to_modify]["Pages: "] + " pages.")
          invalid_pages = False
      except ValueError: 
        print("Your page value must be a number.")
        invalid_pages = True

  elif book_to_modify not in books:
    print("That book does not exist in the library. Make sure you spelled everything correctly.")


def print_page():
  """
  function that prints out how many pages a specific book has from the 'books' dictionary, chosen by the user
  """
  page_to_print = str(input("For which book do you want to know the number of pages? "))
  if page_to_print in books:
    print('{} has '.format(page_to_print) + books[page_to_print]['Pages: '] + ' pages.')
  elif page_to_print not in books:
    print("That book does not exist in the library.")


def remove():
  """
  Function that removes a book (nested dictionary) of the user's choice from the book library ('books' dictionary)
  """
  book_remove = str(input("Which book would you like to remove?: "))
  if book_remove in books:
    print("{} has been removed from the library".format(book_remove))
    books.pop(book_remove)
  elif book_remove not in books:
    print("That book isn't in the library. Make sure you spelled everything correctly.")


def print_all():
  """
  function that prints out the entire 'books' dictionary
  """
  print(books)


def main():
  """
  main function of the program that runs on a loop; asks users to select which function they would like to use, uses if/else to determine which function to run, runs the chosen function from there
  """
  quit = True
  while quit == True:
    choice = input("Please enter:\n (A) To add a book to the library\n (M) To modify the number of pages in an existing book\n (L) To print out the number of pages of a book\n (R) To remove a book from the library\n (P) To print out a list of every book in the library\n (Q) To quit\n");
    
    if choice == "a" or choice == "A":
      add()
      
    elif choice == "m" or choice == "M":
      modify()
      
    elif choice == "l" or choice == "L":
      print_page()
      
    elif choice == "p" or choice == "P":
      print_all()
      
    elif choice == "q" or choice == "Q":
      quit = False
      print("Goodbye!")

    elif choice == "r" or choice == "R":
      remove()

    else:
      print("Invalid option, try again.")


# calls the main function
main()