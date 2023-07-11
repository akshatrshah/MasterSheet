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

    # if selected_item == 'Option 1':
    #     # Set the options for the second dropdown menu based on Option 1
    #     second_dropdown['values'] = ['Option 1.1', 'Option 1.2', 'Option 1.3']
    # elif selected_item == 'Option 2':
    #     # Set the options for the second dropdown menu based on Option 2
    #     second_dropdown['values'] = ['Option 2.1', 'Option 2.2', 'Option 2.3']
    # elif selected_item == 'Option 3':
    #     # Set the options for the second dropdown menu based on Option 3
    #     second_dropdown['values'] = ['Option 3.1', 'Option 3.2', 'Option 3.3']


def submit_values():
    selected_first = first_dropdown.get()
    selected_second = second_dropdown.get()

    if not selected_first or not selected_second:
        messagebox.showerror(
            "Error", "Please select values for both dropdowns.")
    else:
        deleting_the_specific_stock(selected_second, selected_first)
        messagebox.showinfo("Success", "You have deleted " +
                            selected_second+" from "+selected_first+". ")


# Create the main Tkinter window
window = tk.Tk()
window.title("Dropdown Example")
# Create the first dropdown menu
first_label = ttk.Label(window, text="Select Basket:")
first_label.pack()
first_dropdown = ttk.Combobox(
    window, values=nammer(), state='readonly')
first_dropdown.pack()
first_dropdown.bind("<<ComboboxSelected>>", on_first_dropdown_select)

# Create the second dropdown menu
second_label = ttk.Label(window, text="Select a sub-item:")
second_label.pack()
second_dropdown = ttk.Combobox(window, state='readonly')
second_dropdown.pack()

# Create the Submit button
submit_button = ttk.Button(window, text="Submit", command=submit_values)
submit_button.pack()

# Run the Tkinter event loop
window.mainloop()
