class Bookstore(object):
    def __init__(self, bookstore):
        self.bookstore = bookstore
    
    def create_bookstore(name):
        return {'bookstore_name': name,
            'authors' : [],
            'books' : [],
            'next_author_id' : 0,
            'next_book_id' : 0}

    def get_bookstore_name(bookstore):
        return bookstore['bookstore_name']


    def add_author(bookstore, name, nationality):
        author = { 'id' : bookstore['next_author_id'],
               'name' : name,
               'nationality' : nationality}
        bookstore['authors'].append(author)
        bookstore['next_author_id'] +=1
        return author
 

    def get_author_by_name(bookstore, name):
        for author in bookstore['authors']:
            if name == author['name']:
                return author
        return None


    def add_book(bookstore, title, isbn, author):
        book = { 'id' : bookstore['next_book_id'],
             'title' : title,
             'isbn' : isbn,
             'author' : get_author_by_name(bookstore, author)['name']}
        bookstore['books'].append(book)
        bookstore['next_book_id'] += 1
        return book


    def get_book_by_title(bookstore, title):
        for book in bookstore['books']:
            if title == book['title']:
                return book
        return None


    def get_books_by_author(bookstore, author):
        booklist = []
        for book in bookstore['books']:
            if author == book['author']:
                booklist.append(book)
        return booklist
    
    #b1 = Bookstore()
    bookstore = create_bookstore(name)
 
