books = []
def add_book():
    global books # optional code
    book = {}
    book["title"]= input("enter title of the book: ")
    book["author"]= input("enter name of the author: ")
    book["pages"]= int(input("enter number of the pages: "))
    book["price"]= float(input("enter price of the book: "))
    book["isbn"]= input("enter isbn of the book: ")
    books.append(book)

def list_books():
    for book in books:    
        print(f"title of book :, {book['title']}")
        print(f"author of book : , {book['author']}")
        print(f"number of pages : , {book['pages']}")
        print(f"price  of book : , {book['price']}")
        print(f"isbn of book : , {book['isbn']}")
        print("==========================================")


def find_books():
    isbn = input("enter isbn for find a book: ")
    for book in books:
        if book["isbn"] == isbn:
            print(f"title of book :, {book['title']}")
            print(f"author of book : , {book['author']}")
            print(f"number of pages : , {book['pages']}")
            print(f"price  of book : , {book['price']}")
            print(f"isbn of book : , {book['isbn']}")
            print("==========================================")   
            break
    else :
        print("there is no book with this isbn")
            

def delete_books():
    isbn = input("enter isbn for delete a book: ")
    for book in books:
        if book["isbn"] == isbn:
            books.remove(book)
            print("the book was deleted")
            break