import tkinter as tk
from tkinter import filedialog
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        with open(file_path, 'r') as file:
            text_area.delete('1.0', tk.END)
            text_area.insert(tk.END, file.read())
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension='.txt')
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_area.get('1.0', tk.END))
def clear_text():
    text_area.delete('1.0', tk.END)
root = tk.Tk()
root.title("Notepad")
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Clear", command=clear_text)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
root.config(menu=menu_bar)
text_area = tk.Text(root)
text_area.pack()
root.mainloop()