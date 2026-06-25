import tkinter as tk
from tkinter import messagebox

# Create main window
window = tk.Tk()

# Set window title
window.title("To-Do List")

# Set window size (width x height)
window.geometry("400x500")

# Set background color
window.configure(bg="#E6F3FF")
# Function to add a task
def add_task():
    task = task_entry.get()  # Get text from the input box

    if task != "":
         task_list.insert(tk.END, task)  # Add task to list
         task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!") 
def delete_task():
    selected_task = task_list.curselection()

    if selected_task:
        task_list.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete!")        
                # Clear input box
# Heading Label
heading = tk.Label(
    window,
    text="TO-DO LIST",
    font=("Arial", 20, "bold"),
    bg="#E6F3FF",
    fg="#003366"
)
heading.pack(pady=20)

# Task input box
task_entry = tk.Entry(
    window,
    width=30,
    font=("Arial", 14),
    bd=3
)
task_entry.pack(pady=10)

# Add Task button
add_button = tk.Button(
    window,
    text="Add Task",
    font=("Arial", 12),
    width=15,
    bg="#4CAF50",
    fg="white",
    command=add_task
)
add_button.pack(pady=10)
# List to display tasks
task_list = tk.Listbox(
    window,
    width=30,
    height=10,
    font=("Arial", 14),
    bd=3
)

task_list.pack(pady=20)

delete_button = tk.Button(
    window,
    text="Delete Task",
    font=("Arial", 12),
    width=15,
    bg="#F44336",
    fg="white",
    command=delete_task
)

delete_button.pack(pady=10)

# Keep the window running
window.mainloop()