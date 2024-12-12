

class Book:
    def __init__(self,author,title,pages):
        self.author = author
        self.title = title
        self.pages = pages
    def display_info(self):
        print(f"Title:{self.author}")
        print(f"Author:{self.title}")  
        print(f"Pages:{self.pages}")
book = Book("Charlie bone and the wilderness wolf","Jenny Nimmo",358)
book.display_info()
        