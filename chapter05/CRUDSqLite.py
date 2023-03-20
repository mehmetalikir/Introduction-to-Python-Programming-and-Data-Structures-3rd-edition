import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

def create_table():
    cursor.execute("create table if not exists books (bookName text, author text, publisher text, pages int)")
    conn.commit()

def insert_items(bookName, author, publisher, pages):
    cursor.execute("insert into books values (?, ?, ?, ?)", (bookName, author, publisher, pages))
    conn.commit()

def update_items(old, new):
    cursor.execute("update books set bookName = ? where bookName == ?",(old, new))
    conn.commit()
def delete_items(bookName):
    cursor.execute("delete from books where bookName == ?",(bookName))
    conn.commit()
def list_items():
    cursor.execute("select booksName, pages from books")
    list  =  cursor.fetchall()

    for i in list:
        print(i)



create_table()


bookName = input("Please enter book name: ")
author = input("Please enter author name:")
publisher =input("Please enter publisher name:")
pages = int(input("Please enter page number:"))
insert_items(bookName, author, publisher, pages)


old = input("Please enter old book name:")
new = input("Please enter new book name:")
update_items(old, new)

bookName = input("Please enter to delete book name:")
delete_items(bookName)

list_items()

conn.close()