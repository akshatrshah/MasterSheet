import tkinter as tk
from tkinter import messagebox

from main import nammer
from new_client_logic import create, create_new_client


def submit():
    client_name = name_entry.get().strip()
    selected_items = listbox.curselection()
    total = Total_entry.get()

    if not client_name or not selected_items:
        messagebox.showerror(
            "Error", "Please enter a client name and select items.")
    else:
        items = [listbox.get(index) for index in selected_items]
        messagebox.showinfo(
            "Success", f"New client '{client_name}' added with items:\n- {', '.join(items)}")
        create_new_client(client_name, items, total)
        # print(client_name)
        # print(selected_items)
        # print(total)
        clear_fields()


def clear_fields():
    name_entry.delete(0, tk.END)
    listbox.selection_clear(0, tk.END)
    Total_entry.delete(tk.END)


window = tk.Tk()
window.title("Add New Client")

# Create a frame for the input fields
input_frame = tk.Frame(window)
input_frame.pack(padx=10, pady=10)

# Create a label and entry for the client name
name_label = tk.Label(input_frame, text="Client Name:")
name_label.grid(row=0, column=0, sticky=tk.W)
name_entry = tk.Entry(input_frame, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=5)

# Create a label for the item selection
items_label = tk.Label(window, text="Select Items:")
items_label.pack(anchor=tk.W, padx=10, pady=(10, 0))

# Create a listbox for the item selection
items = nammer()
listbox = tk.Listbox(window, selectmode=tk.MULTIPLE, width=40, height=5)
for item in items:
    listbox.insert(tk.END, item)
listbox.pack(padx=10, pady=(0, 10))


Total_label = tk.Label(input_frame, text="Total:")
Total_label.grid(row=3, column=0, sticky=tk.W)
Total_entry = tk.Entry(input_frame, width=30)
Total_entry.grid(row=3, column=1, padx=10, pady=5)

# Create a submit button
submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack()

# Add padding and center the window on the screen
window.update_idletasks()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Set focus to the client name entry field
name_entry.focus_set()

# Start the Tkinter event loop
window.mainloop()
