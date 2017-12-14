class Bookstore(object):
    def __init__(self, name):
        self.bookstore = self.create_bookstore(name)
    
    def create_bookstore(self, name):
        return {'bookstore_name': name,
            'authors' : [],
            'books' : [],
            'next_author_id' : 0,
            'next_book_id' : 0}

    def get_bookstore_name(self):
        return self.bookstore['bookstore_name']


    def add_author(self, name, nationality):
        author = { 'id' : self.bookstore['next_author_id'],
               'name' : name,
               'nationality' : nationality}
        self.bookstore['authors'].append(author)
        self.bookstore['next_author_id'] +=1
        return author
 

    def get_author_by_name(self, name):
        for author in self.bookstore['authors']:
            if name == author['name']:
                return author
        return None


    def add_book(self, title, isbn, author):
        book = { 'id' : self.bookstore['next_book_id'],
             'title' : title,
             'isbn' : isbn,
             'author' : get_author_by_name(bookstore, author)['name']}
        self.bookstore['books'].append(book)
        self.bookstore['next_book_id'] += 1
        return book


    def get_book_by_title(self, title):
        for book in self.bookstore['books']:
            if title == book['title']:
                return book
        return None


    def get_books_by_author(self, author):
        booklist = []
        for book in self.bookstore['books']:
            if author == book['author']:
                booklist.append(book)
        return booklist
    
b1 = Bookstore('the_bookstore')
print(b1.get_bookstore_name())
print(b1.add_author('Elena Ferrante', 'Italy'))

