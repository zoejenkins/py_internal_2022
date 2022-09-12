print("Welcome to the bookstore baby")
books = {
  'Harry Potter': {
    'Pages: ' : 600,
    'Author: ': 'JK Rowling',
    'Published : ' : 2000,
    'Genre: ' : 'Fantasy'
  }
}


def main():
  quit = False;
  while quit == False:
    choice = input("Please enter: \n (A) To add a book \n (M)   To modify the number of pages of a book \n (L) To print out the number of pages of a book \n (P) To print out all books’ titles with their authors and the number of pages \n (Q) to Quit \n");
    
    if (choice == "a") or (choice == "A"):
      add();
      stoploop();
      
    elif (choice == "m") or (choice == "M"):
      modify();
      stoploop();
      
    elif (choice == "l") or (choice == "L"):
      printpage();
      stoploop();
      
    elif (choice == "p") or (choice == "P"):
      printall()
      stoploop();
      
    elif (choice == "q") or (choice == "Q"):
      quit = True;
      print("Goodbye!");

    else:
      print("What went wrong");


def add():
  introductions = ['Title: ', 'Author: ', 'Pages: ', 'Genre: ', 'Year: ']
  title = input("Enter the books' name: ")
  author = input("Enter the author of {}: ".format(title))
  year = input("Enter the year {} was published: ".format(title))
  genre = input("Enter the genre of {}: ".format(title))
  pages = input("Enter how many pages {} has: ".format(title))
  intro_values = [str(title), str(author), str(pages), str(genre), str(year)]
  new_book = dict(zip(introductions,intro_values))
  books.update(new_book)
  print(books)

def remove():
  book_remove = input("Which book would you like to remove?: ")
  books.pop()

def modify():
  thisdict["year"] = input("How many pages does the book have?")

def printpage():
  print("printpage")

def printall():
  print(books)


def stoploop():
  end = input("Would you liek to continue? Y/N: ")
  ok = False;
  while ok == False:
    if end == "N":
      quit = True;
      ok = True;
    elif end == "Y":
      quit = False;
      ok = True;
    else:
      end = input("Invalid entry. please enter \"Y\" or \"N\"")


main()