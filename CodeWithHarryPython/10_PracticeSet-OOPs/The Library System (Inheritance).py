# Create a base class Material with attributes title and author.

# Create a subclass Book that adds a page_count attribute.

# Create another subclass Magazine that adds an issue_number attribute.

# Both should have a display_info() method that prints all their specific details.
class Material:
    def __init__(self,author,title):
        self.author = author
        self.title = title

    def display_info(self):
        print(f"Book title : {self.title}")
        print(f"Book author : {self.author}")
class Book(Material):
    def __init__(self, author, title,page):
        super().__init__(author, title)
        self.page = page
    def display_info(self):
        super().display_info()
        print(f"Book Pages : {self.page}")

class Magazine(Material):
    def __init__(self, author, title,issue_no):
        super().__init__(author, title)
        self.issue_no = issue_no
    def display_info(self):
        super().display_info()
        print(f"Book issue no : {self.issue_no}")

M1 = Magazine("Amish","Naga","hSKDJF89")
B1 = Book("Amish","Rama",267)

M1.display_info()
B1.display_info()