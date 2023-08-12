# whatabook.py
# Alex Bailey
# August 7 2023
# WhatABook User Interface

# Import and Config as provided by Professor Haas
# at URL: https://cyberactive.bellevue.edu/ultra/courses/_518940_1/cl/outline
import mysql.connector
from mysql.connector import errorcode
# Configuring based on my system and my whatabook_user access
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "localhost",
    "database": "whatabook",
    "raise_on_warnings": True
}

# Function for displaying the Main Menu
# Multi-line printing format from BowlOfRed
# at URL: https://discuss.python.org/t/pythonic-way-of-printing-multi-line-strings/19681
def show_menu():
    print("\n---MAIN MENU---")

    print("1. View Books"
          "\n2. View Store Locations"
          "\n3. My Account"
          "\n4. Exit Program")

    try:
        choice = int(input("\nChoose Your Path: "))

        return choice
    except ValueError:
        print("\nThere Is No Path This Way"
                  "\nPlease Try Again...")
        show_menu()

# Function for displaying all Books
def show_books(_cursor):
    
    query1 = ("SELECT book_id, book_name, author, details from book")
    _cursor.execute(query1)
    books = _cursor.fetchall()

    print("\n---BOOKS---")
    
    for book in books:
        print("Book Name: {}"
              "\nAuthor: {}"
              "\nDetails: {}\n"
              .format(book[1], book[2], book[3]))

# Function for displaying all Locations
def show_locations(_cursor):

    query2 = ("SELECT store_id, locale from store")
    _cursor.execute(query2)
    locations = _cursor.fetchall()

    print("\n---LOCATIONS---")

    for location in locations:
        print("Location {}: {}"
              .format(location[0], location[1]))
        print("(Open 8am - 6pm At All Available Locations)")

# Function for validating Users by their IDs
def validate_user():
    try:
        user_id = int(input("\nPlease Enter Your User ID Number: "))

        if user_id < 1 or user_id > 3:
            print("\nWe Don't Recognize This Adventurer"
                  "\nPlease Try Again...")
            validate_user()

        return user_id
    
    except ValueError:
        print("\nWe Don't Recognize This Adventurer"
              "\nPlease Try Again...")
        validate_user()

# Function for displaying the User Menu
def show_account_menu():
    try:
        print("\n---USER MENU---")
        print("1. Wishlist"
              "\n2. Add Book"
              "\n3. Main Menu")
        account_choice = int(input('Choose Your Path: '))

        return account_choice
    
    except ValueError:
        print("\nThere Is No Path This Way"
                  "\nPlease Try Again...")
        show_account_menu()

# Function for displaying a User's Wishlist
# Inner Join Query format as provided by Professor Haas
# at URL: https://cyberactive.bellevue.edu/ultra/courses/_518940_1/cl/outline
# Multi-Line string format from AlixaProDev
# at URL:  https://sparkbyexamples.com/python/python-create-a-long-multi-line-string/
def show_wishlist(_cursor, _user_id):
    query3 = ("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author "
                    "FROM wishlist "
                    "INNER JOIN user ON wishlist.user_id = user.user_id "
                    "INNER JOIN book ON wishlist.book_id = book.book_id "
                    "WHERE user.user_id = {}".format(_user_id))
    _cursor.execute(query3)
    wishlist = _cursor.fetchall()

    print("\n---WISHLIST---")

    for book in wishlist:
        print("Book Name: {}"
              "\nAuthor: {}\n"
              .format(book[4], book[5]))

# Function for displaying all Books not already in the User's Wishlist
def show_books_to_add(_cursor, _user_id):
    query4 = ("SELECT book_id, book_name, author, details "
            "FROM book "
            "WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})"
            .format(_user_id))
    _cursor.execute(query4)
    books_remaining = _cursor.fetchall()

    print("\n---OPTIONS---")

    for book in books_remaining:
        print("Book Id: {}"
              "\nBook Name: {}"
              "\nAuthor: {}"
              "\nDetails: {}\n"
              .format(book[0], book[1], book[2], book[3]))
        

# Function for adding a Book to a User's Wishlist
def add_book_to_wishlist(_cursor, _user_id, _book_id):
    query5 = ("INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(_user_id, _book_id))
    _cursor.execute(query5)





# Attempting to connect with MySQL using Try-Block provided by Professor Haas
# at URL: https://cyberactive.bellevue.edu/ultra/courses/_518940_1/cl/outline
try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

# Initial Menu display
    print("\nWhatABook: Virtual User Interface")

    menu_choice = show_menu()

# While loop for Main Menu options
    while menu_choice != 4:

# Conditional statement for Main Menu options
        if menu_choice == 1:
            print("\nLet's See What Adventures Await...")
            show_books(cursor)

        if menu_choice == 2:
            show_locations(cursor)

        if menu_choice == 3:
            my_user_id = validate_user()
            print("\nWelcome Back, Adventurer!!!")
            account_choice = show_account_menu()

# While loop for User Menu options
            while account_choice != 3:

# Conditional statements for Use Menu options
                if account_choice == 1:
                    show_wishlist(cursor, my_user_id)

                if account_choice == 2:
                    show_books_to_add(cursor, my_user_id)
# Try Block for handling input error from the book "A Primer on Scientific Programming with Python" by H. P. Langtangen, 5th edition, Springer, 2016.  
                    try:
                        book_choice = int(input("\nWhich Journey Would You Like To Save For Another Time?"
                                            "\nBook ID: "))

                        if book_choice <0 or book_choice >9:
                            print("\nNo Such Journey Exists"
                                  "\nPlease Choose Another Path...")
                        
                        else:
                            add_book_to_wishlist(cursor, my_user_id, book_choice)
                            db.commit()
                            print("\nAdventure Number {} was added to your wishlist!".format(book_choice))

                    except:
                          print("\nNo Such Journey Exists"
                                  "\nPlease Choose Another Path...")  
 
                if account_choice < 1 or account_choice > 3:
                    print("\nThis Path Is Blocked"
                          "\nPlease Try Another...")

# Return to User Menu after option selection
                account_choice = show_account_menu()
        
# Main Menu input error handling
        if menu_choice < 1 or menu_choice > 3:
            print("\nThis Path Is Blocked"
                  "\nPlease Try Another...")
            
# Return to Main Menu after certain options
        menu_choice = show_menu()

    print("\nYour Journey Is At An End..."
          "\nWe Hope To See You Soon For Another Adventure!")

# Same error notations if code fails as previous files
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist") 

    else:
        print(err)
        
finally:
    db.close()
