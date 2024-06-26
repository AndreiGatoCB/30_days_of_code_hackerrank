from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author
    @abstractmethod
    def display():
        pass

class MyBook(Book):
    def __init__(self, title, author, price):
        Book.__init__(self, title=title, author=author)
        self.price = price

    def display(self):
        print(f'''Title: {self.title}
Author: {self.author}
Price: {self.price}''')

#Write MyBook class

title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()
