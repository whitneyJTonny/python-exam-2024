
class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        
    def get_book_info(self):
        return f"Title:{self.title}, Author:{self.author}"

class EBook(Book):
    def __init__(self, title, author, format):
        super().__init__(title, author)
        self.format = format
        
    def display_info(self):
        return f"{self.get_book_info()}, Format:{self.format}"
    
if __name__ == "__main__" :  
        ebook = EBook("Charlie bone and the wilderness wolf", "Jenny Nimmo","PDF")
print(ebook.display_info())

