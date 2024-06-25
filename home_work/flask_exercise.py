from flask import Flask, render_template, request, redirect, url_for
import json
import os

app = Flask(__name__)


class Book:
    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre


class Library:
    def __init__(self, filename='library.json'):
        self.filename = filename
        self.books = self.load_library()

    def load_library(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                books = json.load(file)
                return [Book(**book) for book in books]
        return []

    def save_library(self):
        with open(self.filename, 'w') as file:
            json.dump([book.__dict__ for book in self.books], file)

    def add_book(self, book):
        self.books.append(book)
        self.save_library()

    def edit_book(self, index, new_book):
        self.books[index] = new_book
        self.save_library()

    def delete_book(self, index):
        self.books.pop(index)
        self.save_library()


library = Library()


@app.route('/')
def index1():
    return render_template('home.html')


@app.route('/add', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        genre = request.form['genre']
        new_book = Book(title, author, year, genre)
        library.add_book(new_book)
        return redirect(url_for('list_books'))
    return render_template('add_book.html')





@app.route('/list')
def list_books():
    books = library.books
    return render_template('list_books.html', books=books)


@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_book(index):
    book = library.books[index]
    if request.method == 'POST':
        book.title = request.form['title']
        book.author = request.form['author']
        book.year = request.form['year']
        book.genre = request.form['genre']
        library.edit_book(index, book)
        return redirect(url_for('list_books'))
    return render_template('edit_book.html', book=book, index=index)


@app.route('/delete/<int:index>', methods=['POST'])
def delete_book(index):
    library.delete_book(index)
    return redirect(url_for('list_books'))
