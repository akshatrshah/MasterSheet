# tkinter of CLEAR SCRIPT
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from deleting import deleting_cells, deleting_the_specific_stock
from main import nammer


def on_first_dropdown_select(event):
    selected_item = first_dropdown.get()

    # Clear the options in the second dropdown menu
    second_dropdown.set('')
    second_dropdown['values'] = []
    second_dropdown['values'] = deleting_cells(selected_item)


def submit_values():
    selected_first = first_dropdown.get()
    selected_second = second_dropdown.get()

    if not selected_first or not selected_second:
        messagebox.showerror(
            "Error", "Please select values for both dropdowns.")
    else:
        deleting_the_specific_stock(selected_second, selected_first)
        messagebox.showinfo("Success", "You have deleted " +
                            selected_second + " from " + selected_first + ".")


# Create the main Tkinter window
window = tk.Tk()
window.title("Drop Script")

# Set padding for the window
window.geometry("300x200")
window.configure(padx=10, pady=10)

# Create the first dropdown menu
first_label = ttk.Label(window, text="Select Basket:")
first_label.pack(pady=5)
first_dropdown = ttk.Combobox(window, values=nammer(), state='readonly')
first_dropdown.pack(pady=5)
first_dropdown.bind("<<ComboboxSelected>>", on_first_dropdown_select)

# Create the second dropdown menu
second_label = ttk.Label(window, text="Select Stock Name:")
second_label.pack(pady=5)
second_dropdown = ttk.Combobox(window, state='readonly')
second_dropdown.pack(pady=5)

# Create the Submit button
submit_button = ttk.Button(window, text="Submit", command=submit_values)
submit_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
