import tkinter as tk
from tkinter import messagebox
import sqlite3
conn = sqlite3.connect("library.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER NOT NULL
    )
""")
conn.commit()
def add_book():
    title = title_entry.get()
    author = author_entry.get()
    year = year_entry.get()
    if title and author and year:
        cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
        conn.commit()
        messagebox.showinfo("Success", "Book added successfully.")
        clear_fields()
        load_books()
    else:
        messagebox.showerror("Error", "Please fill in all the fields.")
def delete_book():
    selected_book = book_listbox.get(tk.ACTIVE)
    if selected_book:
        cursor.execute("DELETE FROM books WHERE id=?", (selected_book,))
        conn.commit()
        messagebox.showinfo("Success", "Book deleted successfully.")
        load_books()
def clear_fields():
    title_entry.delete(0, tk.END)
    author_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
def load_books():
    book_listbox.delete(0, tk.END)
    cursor.execute("SELECT id, title, author, year FROM books")
    books = cursor.fetchall()
    for book in books:
        book_listbox.insert(tk.END, book[1])
root = tk.Tk()
root.title("Library Management")
title_label = tk.Label(root, text="Title:")
title_label.grid(row=0, column=0, padx=5, pady=5)
title_entry = tk.Entry(root)
title_entry.grid(row=0, column=1, padx=5, pady=5)
author_label = tk.Label(root, text="Author:")
author_label.grid(row=1, column=0, padx=5, pady=5)
author_entry = tk.Entry(root)
author_entry.grid(row=1, column=1, padx=5, pady=5)
year_label = tk.Label(root, text="Year:")
year_label.grid(row=2, column=0, padx=5, pady=5)
year_entry = tk.Entry(root)
year_entry.grid(row=2, column=1, padx=5, pady=5)
add_button = tk.Button(root, text="Add Book", command=add_book)
add_button.grid(row=3, column=0, padx=5, pady=5)
delete_button = tk.Button(root, text="Delete Book", command=delete_book)
delete_button.grid(row=3, column=1, padx=5, pady=5)
book_listbox = tk.Listbox(root, width=40)
book_listbox.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
scrollbar = tk.Scrollbar(root)
scrollbar.grid(row=4, column=2, sticky=tk.N+tk.S)
book_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=book_listbox.yview)
load_books()
root.mainloop()