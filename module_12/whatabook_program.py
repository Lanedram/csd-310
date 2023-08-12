# Lanedra Moore
# July 20, 2023
# CYBR410 Data/Database Security
# Whatabook Query: Creating a program that queries a mysql database

import sys
import mysql.connector
from mysql.connector import errorcode

#The information needed to access the database
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

#Shows the menu for whatabook
def show_menu():
    print("Main Menu")
    print("\t1. View Available Books")
    print("\t2. View Store Location")
    print("\t3. View Your Account")
    print("\t4. Quit")
    choice = input("Please make your selection: ")

    #if the user does not choose a correct option, program quits
    if (choice != '1' or choice != '2' or choice != '3' or choice != '4'):
        print("You selected an invalid choice. The program is terminating.")
       sys.exit(0)

    
    return choice


def show_books(cursor):
    #execute the SQL
    cursor.execute("SELECT * from books")
    books = cursor.fetchall()

def validate_user():
    #Get the users id
    user_id = input("\nEnter the customer's ID: ")
    #determine if a correct user id was entered; if not, exit the program
    if user_id != '1' or user_id != '2' or user_id != '3':
        print("Incorrect customer ID. Closing the program.")
        sys.exit(0)
    #return the user id to get the right results
    return user_id


def customer_menu():
    #show the customer's menu
    print("\nCustomer Menu:\n")
    print("\t1. Wishlist")
    print("\t2. Add Book")
    print("\t3. Main Menu")

    option = input("Please select the menu option you would like to use: ")

    if (option != '1' or option != '2' or option != '3'):
        print("Invalid menu option. Terminating the program...")
        sys.exit(0)
    return option


def main():
    #attempting to access the database
    try:
        db = mysql.connector.connect(**config)

        print("\n  Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))
        
        #Welcome and options
        print("\n\nWelcome to the Whatabook program!")
        choice = show_menu()

        cursor = db.cursor()

        #continue to loop until option 4 is chosen
        while (choice != '4'):
            #shows books if choice is 1
            if (choice == '1'):
                #define the SQL query and show results using cursor
                sqlQuery = """SELECT * FROM book;"""
                cursor.execute(sqlQuery)

                print("\tAvailable Books\n")

                #make a list of the available books and print results
                books = cursor.fetchall()
                for book in books:
                    print("Book Name: {}".format(book[0]))
                    print("Author: {}".format(book[1]))
                    print("Details: {}".format(book[2]))

            #shows locations if 2 is chosen
            elif (choice == '2'):
                #define sql query and show results from store
                sqlQuery = "Select * from store;"
                cursor.execute(sqlQuery)

                print("\n\tStore Location Information:")

                #make a list of the available stores and print results
                stores = cursor.fetchall()
                for store in stores:
                    print("Store Number: {}".format(store[0]))
                    print("Store Information: {}".format(print[1]))
                
            #shows user account if 3 is chosen
            elif (choice == '3'):
                #determine if a correct choice was made, if not terminate program
                user_id = validate_user()
                menu_option = customer_menu()

                #Create a loop until user picks option 3
                while (menu_option != '3'):
                    #show wishlist for specified customer
                    if (menu_option == '1'):
                        #Need two inner joins in sql statement to lock in both user and books and wishlist
                        sqlQuery = ("SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author FROM wishlist " +
                        "INNER JOIN user ON wishlist.user_id = user.user_id " +
                        "INNER JOIN book ON wishlist.book_id = book.book_id " +
                        "WHERE user.user_id = " + user_id)
                        cursor.execute(sqlQuery)

                        #make a list of the wishlist
                        wishlist = cursor.fetchall()

                        #print the results of the wishlist
                        print("\n\tDisplaying Wishlist Items")

                        for book in wishlist:
                            print("\tBook Name: {}".format(book[4]))
                            print("\tAuthor: {}".format(book[5]))

                    #Show books that could be added not currently in wishlist
                    elif (menu_option == '2'):
                        sqlQuery = ("SELECT * FROM book WHERE book_id NOT IN " +
                                    "(SELECT book_id FROM wishlist WHERE user_id = " + user_id + ")")
                        cursor.execute(sqlQuery)

                        books_not_in_wishlist = cursor.fetchall()

                        print("\n\t Showing Books Not In Your Wishlist\n")
                        for book in books_not_in_wishlist:
                            print("\tBook ID: {}".format(book[0]))
                            print("\tBook Name: {}".format(book[1]))

                        #Choose the book you want to add to the wishlist
                        book_to_add = input("Please select the book you would like to add by the book id: ")
                        cursor.execute("INSERT INTO wishlist (user_id, book_id) VALUES({}, {})".format(user_id, book_to_add))

                        #commit the changes to the wishlist
                        db.commit()
                        print("\n\t Book ID {} was added to your wishlist".format(book_to_add))

                    elif menu_option != '1' or menu_option != '2' or menu_option != '3':
                        print("Incorrect menu option. Please try again.")
                    
                    #Let customer choose new menu option
                    menu_option = customer_menu()

            
            choice = show_menu()

        
        print("Thank you for using the whatabook program!")
        input("\n\n   Press any key to continue...")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("  The supplied username or password are invalid")

        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("   The specified database does not exist")
        
        else:
            print(err)

    finally:
        db.close()

main()