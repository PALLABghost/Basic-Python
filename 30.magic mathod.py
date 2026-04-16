#magic method = Dunder methods(double underscore) __init,__str__,__eq__
            #allow to use customize behavior of objects using python build in operator

class Book:
    def __init__(self,title,author,num_page):
        self.title = title
        self.author = author
        self.num_page = num_page

    def __str__(self):
        return f"{self.title} by {self.author}"
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    def __lt__(self,other):
        return  self.num_page < other.num_page
    def __gt__(self,other):
        return  self.num_page > other.num_page
    def __add__(self, other):
        return self.num_page + other.num_page
    def __contains__(self, item):
        return item in self.title or item in self.author
    def __getitem__(self, item):
        if item == "title":
            return self.title
        if item == "author":
            return self.author
        if item == "num_page":
            return self.num_page
        else:
            return f"{item} was not found"

book1 = Book("The Hobbit", "J.R.R Tolkien", 310)
book2 = Book("Harry Potter","J.K Rowling", 223)

print(book1)    #__str__
print(book2)
print(book1 == book2)       #__eq__
print(book1 < book2)        # __lt__
print(book1 > book2)        #__gt__
print(book1 + book2)    #__add__
print("Hobbit" in book1)    #__contains__
print(book1["title"])
print(book2["author"])      #__getitem__

