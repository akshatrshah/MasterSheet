import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sys
import subprocess
from main import main, nammer


def delete_cell():
    subprocess.Popen(["python", "delete.py"])


def redirect_stdout_to_text_widget(text_widget):
    class StdoutRedirector:
        def __init__(self, text_widget):
            self.text_widget = text_widget

        def write(self, message):
            self.text_widget.delete("1.0", tk.END)
            # Enable state temporarily
            self.text_widget.configure(state="normal")
            self.text_widget.insert(tk.END, message, ("stdout",))
            self.text_widget.configure(state="disabled")  # Disable state again
            self.text_widget.see(tk.END)

    sys.stdout = StdoutRedirector(text_widget)


def open_new_client_window():
    subprocess.Popen(["python", "new_client.py"])


def submit():
    stock_name = stock_name_entry.get()
    basket_name = basket_name_entry.get()
    lister = nammer()
    dictionary = {}
    for i in range(len(lister)):
        dictionary[lister[i]] = i+1

    if basket_name != '':
        # Perform action with the inputs

        x = main(stock_name, dictionary[basket_name])

    # Clear the entry fields
        stock_name_entry.delete(0, tk.END)
        basket_name_entry.delete(0, tk.END)

        messagebox.showinfo("Success", "Submitted successfully!")
    else:
        messagebox.showinfo("Failed", "Invalid Input!")


def runner(stock_name, quantity):
    # Replace with your desired functionality
    print("Stock Name:", stock_name)
    print("Quantity:", quantity)


# Create a new Tkinter window
window = tk.Tk()
window.geometry('+0+0')

# Create a frame for the input prompts
prompt_frame = tk.Frame(window)
prompt_frame.pack(anchor=tk.NW, padx=10, pady=10)

# Create an Entry for the stock name
stock_name_label = tk.Label(prompt_frame, text="Stock Name:")
stock_name_label.grid(row=0, column=0, sticky=tk.W)
stock_name_entry = tk.Entry(prompt_frame)
stock_name_entry.grid(row=0, column=1, padx=10, pady=10)


basket_name_label = tk.Label(prompt_frame, text="Basket Name:")
basket_name_label.grid(row=1, column=0, sticky=tk.W)
items = nammer()
basket_name_entry = ttk.Combobox(prompt_frame, values=items, state='readonly')
basket_name_entry.grid(row=1, column=1, padx=10, pady=10)
# Create a Submit button
submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack(anchor=tk.NW, padx=10, pady=10)


text_widget = tk.Text(window, state='disabled')
text_widget.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Redirect stdout to the Text widget
redirect_stdout_to_text_widget(text_widget)

new_client_button = tk.Button(
    window, text="Create New Client", command=open_new_client_window)
new_client_button.pack(padx=10, pady=10)

new_client_button = tk.Button(
    window, text="Clear Data", command=delete_cell)
new_client_button.pack(padx=20, pady=10)
# Start the Tkinter event loop
window.mainloop()
