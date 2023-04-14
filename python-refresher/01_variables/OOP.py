# class Student:
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades

#     def average(self):
#         return sum(self.grades) / len(self.grades)


# bob = Student("Bob", (90, 90, 93, 78, 90))
# print(bob.average())


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __str__(self):
#         return f"Person {self.name}, {self.age} years old"

#     def __repr__(self):
#         return f"<Person({self.name}, {self.age})>"


# bob = Person("Bob", 35)
# print(bob)


# class Device:
#     def __init__(self, name, connected_by):
#         self.name = name
#         self.connected_by = connected_by
#         self.connected = True

#     def __str__(self):
#         return f"Device {self.name!r} ({self.connected_by})"

#     def disconnected(self):
#         self.connected = False
#         print("Disconnected")


# class Printer(Device):
#     def __init__(self, name, connected_by, capacity):
#         super().__init__(name, connected_by)
#         self.capacity = capacity
#         self.remaining_pages = capacity

#     def __str__(self):
#         return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

#     def print(self, pages):
#         if not self.connected:
#             print("Your printer is not connected!")
#             return
#         print(f"Printing {pages} pages")
#         self.remaining_pages -= pages


# printer = Printer("Printer", "USB", 500)
# printer.print(20)
# print(printer)
# printer.disconnected()


# class Bookshelf:
#     def __init__(self, *books):
#         self.books = books

#     def __str__(self):
#         return f"Bookshelf with {len(self.books)} books."


# class Book:
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return f"Book {self.name}"


# book = Book("Harry Potter")
# book2 = Book("Python 101")

# shelf = Bookshelf(book, book2)
# print(shelf)
# print(shelf.books)

from typing import List


def list_avg(sequence: List) -> float:
    return sum(sequence) / len(sequence)


total = list_avg([25, 50])
print(total)
