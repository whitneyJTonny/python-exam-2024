
class Book():
    def __init__(self,title,author):
        self.title = title
        self.author = author
    def display_info(self):
        print(f'title: {self.title}')
        print(f'author: {self.author}')
my_book = Book('Charlie bone and the wilderness worlf','Jenny Nimmo')
my_book.display_info()