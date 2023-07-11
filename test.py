# import tkinter as tk
# from tkinter import messagebox
# from tkinter import ttk

# items = ["Item 1", "Item 2", "Item 3", "Item 4"]
# clients = ["Client 1", "Client 2", "Client 3", "Client 4"]


# def submit_values():
#     client = client_dropdown.get()
#     if not client:
#         messagebox.showerror("Error", "Please select a client.")
#         return

#     values = []
#     for index, entry in enumerate(entry_list):
#         value = entry.get()
#         if not value.isdigit():
#             messagebox.showerror(
#                 "Error", "Please enter a valid numerical value.")
#             return
#         values.append(int(value))

#     # Process the values (e.g., print or store them)
#     print("Client:", client)
#     print("Values:", values)
#     # TODO: Further processing or storage logic

#     messagebox.showinfo("Success", "Values submitted successfully.")


# window = tk.Tk()
# window.title("Numerical Input")
# window.geometry("300x250")
# window.configure(padx=10, pady=10)

# # Create the client dropdown menu
# client_label = ttk.Label(window, text="Select Client:")
# client_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
# client_dropdown = ttk.Combobox(window, values=clients, state='readonly')
# client_dropdown.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)

# entry_list = []

# for index, item in enumerate(items):
#     label = tk.Label(window, text=item)
#     label.grid(row=index+1, column=0, padx=5, pady=5, sticky=tk.W)
#     entry = tk.Entry(window)
#     entry.grid(row=index+1, column=1, padx=5, pady=5, sticky=tk.W)
#     entry_list.append(entry)

# submit_button = tk.Button(window, text="Submit", command=submit_values)
# submit_button.grid(row=len(items)+1, columnspan=2, padx=5, pady=10)

# window.mainloop()
from main import get_clients, get_corresponding_baskets

x = get_corresponding_baskets('home')
print(x)
