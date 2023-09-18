import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        selected_task = listbox.get(listbox.curselection())
        listbox.delete(listbox.curselection())
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_task():
    try:
        selected_task = listbox.get(listbox.curselection())
        entry.delete(0, tk.END)
        entry.insert(0, selected_task)
        listbox.delete(listbox.curselection())
    except:
        messagebox.showwarning("Warning", "Please select a task to update.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create an entry widget to add tasks
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

# Create buttons for adding, updating, and removing tasks
add_button = tk.Button(root, text="Add Task", command=add_task)
update_button = tk.Button(root, text="Update Task", command=update_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
add_button.pack()
update_button.pack()
remove_button.pack()

# Create a listbox to display tasks
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

# Run the application
root.mainloop()
