import tkinter as tk
from tkinter import messagebox

def add_contact():
    name = name_entry.get()
    phone_number = phone_entry.get()

    if name and phone_number:
        names.append(name)
        phone_numbers.append(phone_number)
        display_contacts()
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Both fields are required")

def display_contacts():
    display_area.delete('1.0', tk.END)
    display_area.insert(tk.END, "Name\t\tPhone Number\n")
    for name, phone_number in zip(names, phone_numbers):
        display_area.insert(tk.END, f"{name}\t\t{phone_number}\n")

def search_contact():
    search_term = search_entry.get()
    if search_term in names:
        index = names.index(search_term)
        phone_number = phone_numbers[index]
        messagebox.showinfo("Search Result", f"Name: {search_term}, Phone Number: {phone_number}")
    else:
        messagebox.showwarning("Not Found", "Name Not Found")

root = tk.Tk()
root.title("Contact Manager")

names = []
phone_numbers = []

tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Phone Number").grid(row=1, column=0, padx=10, pady=5)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Button(root, text="Add Contact", command=add_contact).grid(row=2, column=0, columnspan=2, pady=10)

tk.Label(root, text="Search Term").grid(row=3, column=0, padx=10, pady=5)
search_entry = tk.Entry(root)
search_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Button(root, text="Search", command=search_contact).grid(row=4, column=0, columnspan=2, pady=10)

display_area = tk.Text(root, height=10, width=40)
display_area.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()