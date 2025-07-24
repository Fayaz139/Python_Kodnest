def checkout_book(book_title, available_books):
    if book_title in available_books:
        available_books.remove(book_title)

def return_book(book_title, available_books):
    if book_title not in available_books:
        available_books.append(book_title)

def view_books(available_books):
    print(f"Available books: {available_books}")



library_books = ['Harry Potter', '1984', 'Pride and Prejudice']
    
view_books(library_books)
checkout_book('Harry Potter', library_books)
view_books(library_books)
return_book('Harry Potter', library_books)
view_books(library_books) 