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

  invalidtitle = True
  while invalidtitle == True:
    title = input("Enter the books' name: ")
    if len(title) < 1 or title.isspace():
      print("The book must have a title")
      invalidtitle = True
    else:
      invalidtitle = False
      
  invalidauthor = True
  while invalidauthor == True:
    author = input("Enter the author of {}: ".format(title))
    if any(char.isdigit() for char in author):
      print("Author's name cannot include a number")
      invalidauthor = True
    elif len(author) < 1 or author.isspace():
      print("Author must have a name.")
      invalidauthor = True
    else:
      invalidauthor = False
      
  maxyear = 2022
  minyear = 868
  yearinvalid = True
  while yearinvalid == True:
    year = input("Enter the year {} was published: ".format(title))
    try:
      if int(year) > int(maxyear):
        print("The year you entered is not valid. Please enter a smaller year")
        yearinvalid = True
      elif int(year) < int(minyear):
        print("The earliest book published was in 868 AD. Please enter a larger year.")
        yearinvalid = True
      else:
        yearinvalid = False
    except ValueError:
      print("Your year must be a number.")
      yearinvalid = True  

  invalidgenre = True
  while invalidgenre == True:
    genre = input("Enter the genre of {}: ".format(title))
    if any(char.isdigit() for char in genre):
      print("Genre cannot include a number")
      invalidgenre = True
    elif len(genre) < 1 or genre.isspace():
      print("Genre must have a name.")
      invalidgenre = True
    else:
      invalidgenre = False
  
  maxpages = 3000000
  minpages = 1
  invalidpages = True
  while invalidpages == True:
    pages = input("Enter how many pages {} has: ".format(title))
    try:
      if int(pages) > int(maxpages):
        print("ERROR: the book with the most pages has 3 million pages. Please enter a lower value.")
        invalidpages = True
      elif int(pages) < int(minpages):
        print("ERROR: Your book can't have less than 1 page")
        invalidpages = True
      else:
        invalidpages = False
    except ValueError: 
      print("Your page value must be a number.")
      invalidpages = True
      
  intro_values = [str(author), str(pages), str(genre), str(year)]
  book_info = dict(zip(introductions,intro_values))
  new_book = {title : book_info}
  books.update(new_book)
  print(books)

def remove():
  """
  Function that removes a book (nested dictionary) of the user's choice from the book library ('books' dictionary)
  """
  book_remove = str(input("Which book would you like to remove?: "))
  if book_remove in books:
    print("{} has been removed from the library".format(book_remove))
    books.pop(book_remove)
  elif book_remove not in books:
    print("That book isn't in the library")

def modify():
  """
  Function that lets user access and modify the number of pages in a book of their choice
  """
  maxpages = 3000000
  minpages = 1
  booktomodify = str(input("For which book do you want to modify the number of pages? "))
  if booktomodify in books:
    print(booktomodify + " currently has " + books[booktomodify]["Pages: "] + " pages.")
    invalidpages = True
    while invalidpages == True:
      newpagenumber = input("What do you want to update the number to? ")
      try:
        if int(newpagenumber) > int(maxpages):
          print("ERROR: the book with the most pages has 3 million pages. The number you entered was higher than this.")
          invalidpages = True
        elif int(newpagenumber) < int(minpages):
          print("ERROR: Your book can't have less than 1 page")
          invalidpages = True
        else:
          books[booktomodify]["Pages: "] = newpagenumber
          print(booktomodify + " now has " + books[booktomodify]["Pages: "] + " pages.")
          invalidpages = False
      except ValueError: 
        print("Your page value must be a number.")
        invalidpages = True

  elif booktomodify not in books:
    print("That book does not exist in the library. Make sure you spelled everything correctly.")

def printpage():
  """
  function that prints out how many pages a specific book has from the 'books' dictionary, chosen by the user
  """
  pagetoprint = str(input("For which book do you want to know the number of pages? "))
  if pagetoprint in books:
    print('{} has '.format(pagetoprint) + books[pagetoprint]['Pages: '] + ' pages.')
  elif pagetoprint not in books:
    print("That book does not exist in the library.")

def printall():
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
      printpage()
      
    elif choice == "p" or choice == "P":
      printall()
      
    elif choice == "q" or choice == "Q":
      quit = False
      print("Goodbye!")

    elif choice == "r" or choice == "R":
      remove()

    else:
      print("Invalid option, try again.")

# calls the main function
main()