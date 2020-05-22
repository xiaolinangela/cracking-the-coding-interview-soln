from collections import defaultdict


class Book:
    def __init__(self, book_id, details):
        self.id = book_id
        self.details = details

    def get_id(self):
        return self.book_id

    def get_details(self):
        return self.details


class User:
    def __init__(self, user_id, account_type):
        self.id = user_id
        self.account_type = account_type

    def get_id(self):
        return self.id

    def get_account_type(self):
        return self.account_type


class Library:

    def __init__(self):
        self.books = defaultdict(list)

    def add_book(self, book):
        self.books[book.id] = book

    def find_book(self, id):
        try:
            return self.books[id]
        except KeyError:
            print("Cannot find the book")

    def remove_book(self, id):
        try:
            del self.books[id]
        except KeyError:
            print("Cannot find the book")


class UserManager:

    def __init__(self):
        self.users = defaultdict(list)

    def add_user(self, user):
        self.users[user.id] = user

    def find_user(id):
        try:
            return self.users[id]
        except KeyError:
            print("Cannot find the user")

    def remove_user(self, id):
        try:
            del self.users[id]
        except KeyError:
            print("Cannot find the user")


class Display:

    def __init__(self):
        self.activate_book = None
        self.activate_user = None
        self.page_number = 0

    def display_book(self, book):
        self.activate_book = book

    def display_user(self, user):
        self.activate_user = user

    def turn_page_forward(self):
        self.page_number += 1

    def turn_page_backward(self):
        self.page_number -= 1


class OnlineReaderSystem:
    def __init__(self, library, user_manager, display):
        self.library = library
        self.user_manager = user_manager
        self.display = display

    def get_library(self):
        return self.library

    def get_user_manager(self):
        return self.user_manager

    def get_display(self):
        return self.display

    def get_active_book(self):
        return self.display.display_book

    def get_active_user(self):
        return self.display.display_user


if __name__ == "__main__":
    pass
