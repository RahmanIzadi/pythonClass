# V 2.1.0
import books_operation as bo
#--------------------main--------------------
while True:
    print("=================================================")
    print("press A to add a book")
    print("press L to list all books")
    print("press F to find a book")
    print("press D to delete a book")
    print("press Q to quit a book")
    print("=================================================")
    choice = input("enter your choice: ").upper()

    if choice == "A":
        bo.add_book() 
    elif choice == "L":
        bo.list_books()
    elif choice == "F":
        bo.find_books()
    elif choice == "D":
        bo.delete_books()
    elif choice == "Q":
        break
    else :
        print("wrong choice: ")