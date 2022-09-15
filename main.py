print("Welcome to the library!")
books = {
  
}


def main():
  quit = False;
  while quit == False:
    choice = input("Please enter: \n (A) To add a book to the library \n (M) To modify the number of pages in an existing book \n (L) To print out the number of pages of a book \n (R) To remove a book from the library \n (P) To print out a list of every book in the library \n (Q) To quit \n");
    
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
      printall();
      stoploop();
      
    elif (choice == "q") or (choice == "Q"):
      quit = True;
      print("Goodbye!");

    elif (choice == "r") or (choice == "R"):
      remove();
      stoploop();

    else:
      valid_options = ["a", "A", "m", "M", "l", "L", "r", "R", "p", "P", "q", "Q"]
      loop = True;
      while loop == True:
        print("Invalid input, please try again.");
        choice = input("Please enter: \n (A) To add a book to the library \n (M) To modify the number of pages in an existing book \n (L) To print out the number of pages of a book \n (R) To remove a book from the library \n (P) To print out a list of every book in the library \n (Q) To quit \n");
        if choice in valid_options:
          loop = False;
        elif choice not in valid_options:
          loop = True;
        


def add():
  introductions = ['Author: ', 'Pages: ', 'Genre: ', 'Year: ']
  title = input("Enter the books' name: ")
  author = input("Enter the author of {}: ".format(title))
  year = input("Enter the year {} was published: ".format(title))
  genre = input("Enter the genre of {}: ".format(title))
  pages = input("Enter how many pages {} has: ".format(title))
  intro_values = [str(author), str(pages), str(genre), str(year)]
  book_info = dict(zip(introductions,intro_values))
  new_book = {title : book_info}
  books.update(new_book)
  print(books)

def remove():
  book_remove = str(input("Which book would you like to remove?: "))
  if book_remove in books:
    books.pop(book_remove)
  elif book_remove not in books:
    print("That book isn't in the library")

def modify():
  booktomodify = str(input("For which book do you want to modify the number of pages? "))
  if booktomodify in books:
    print(booktomodify + " currently has " + books[booktomodify]["Pages: "] + " pages.")
    newpagenumber = input("What do you want to update the number to? ")
    books[booktomodify]["Pages: "] = newpagenumber
    print(booktomodify + " now has " + books[booktomodify]["Pages: "] + " pages.")

  elif booktomodify not in books:
    print("That book does not exist in the library")

def printpage():
  pagetoprint = str(input("For which book do you want to know the number of pages? "))
  if pagetoprint in books:
    print('{} has '.format(pagetoprint) + books[pagetoprint]['Pages: '] + ' pages.')
  elif pagetoprint not in books:
    print("That book does not exist in the library")

def printall():
  print(books)


def stoploop():
  end = input("Would you like to continue? Y/N: ")
  ok = False;
  while ok == False:
    if (end == "N") or (end == "n"):
      quit = True;
      ok = True;
    elif (end == "Y") or (end == "y"):
      quit = False;
      ok = True;
    else:
      end = input("Invalid entry. please enter \"Y\" or \"N\"")


main()