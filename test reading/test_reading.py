import subprocess
import sys
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import pandas as pd
import numpy as np
import warnings


class Colors:
    GREEN = '\033[32m'
    RESET = '\033[0m'
    RED = '\033[31m'


warnings.filterwarnings("ignore")


# def myfunc(update_clients, basket_name, stock_name):
#     # print("Basket Name: "+Colors.GREEN+basket_name.upper() + Colors.RESET +
#     #       " allocation available: ")
#     print("Basket Name: "+basket_name.upper() + " allocation available: ")
#     for i in update_clients:
#         dfmain = pd.read_excel('Master R&D.xlsx', sheet_name=None)
#         df = dfmain[i]
#         column_indices_to_keep = [0, 1, 2, 3, 4, 5]
#         df = df.iloc[:, column_indices_to_keep]
#         columns_with_merged_cells = [0, 1, 2, 5]
#         df.iloc[:, columns_with_merged_cells] = df.iloc[:,
#                                                         columns_with_merged_cells].fillna(method='ffill')
#         column_name = 'Strategy'
#         value_to_find = basket_name
#         mask = df[column_name] == value_to_find
#         filtered_rows = df[mask][df[mask].isnull().any(axis=1)]
#         content = filtered_rows['Allocated'].to_list()
#         content = [round(num, 2) for num in content]
#         content = ' '.join(map(str, content))
#         # if len(content) >= 1:
#         #     print('Client Name: '+Colors.GREEN+i.capitalize() +
#         #           Colors.RESET+": "+str(content))
#         # else:
#         #     print('Client Name: '+Colors.RED+i.capitalize() +
#         #           Colors.RESET+": "+str(content))
#         if len(content) >= 1 and content is all :
#             print('Client Name: '+i.capitalize() + "  " + str(content))
#         else:
#             print('Client Name: '+i.capitalize() + "  " + str(content))


def myfunc(update_clients=['home'], basket_name='Split (Corporate Action)', stock_name=''):
    # print("Basket Name: "+Colors.GREEN+basket_name.upper() + Colors.RESET +
    #       " allocation available: ")
    print("Basket Name: "+basket_name.upper() + " allocation available: ")
    for i in update_clients:
        dfmain = pd.read_excel('./Master R&D.xlsx', sheet_name=None)
        df = dfmain[i]
        # print(df)
        column_indices_to_keep = [0, 1, 2, 3, 4, 5]
        df = df.iloc[:, column_indices_to_keep]
        columns_with_merged_cells = [0, 1, 2, 5]
        df.iloc[:, columns_with_merged_cells] = df.iloc[:,
                                                        columns_with_merged_cells].fillna(method='ffill')
        column_name = 'Strategy'
        value_to_find = basket_name
        mask = df[column_name] == value_to_find
        filtered_rows = df[mask][df[mask].isnull().any(axis=1)]
        content = filtered_rows['Allocated'].to_list()
        # print('x', content)
        content = [round(num, 2) for num in content]
        content = [str(num)
                   for num in content if pd.notnull(num)]  # Remove NaN values
        content = ' '.join(content)
        if content:
            print('Client Name: '+i.capitalize() + "  " + content)


def nammer():
    dfmain = pd.read_excel('./Master R&D.xlsx', sheet_name=None)
    df = dfmain['sheet1']
    sheet_names = pd.ExcelFile('Master R&D.xlsx').sheet_names
    sheet_names = [element.lower() for element in sheet_names]
    clients = df['CLIENT NAME'].tolist()
    baskets = df.columns.tolist()
    baskets.pop(0)
    return baskets


def main(stock_name, number):
    number = number-1
    dfmain = pd.read_excel('Master R&D.xlsx', sheet_name=None)
    df = dfmain['sheet1']
    baskets = nammer()
    data_dict = {}
    for index, row in df.iterrows():
        key = row.iloc[0]
        values = row.iloc[1:].tolist()
        data_dict[key] = values
    string_to_drop = 'n'
    data_dict = {key: [value for value in values if value !=
                       string_to_drop] for key, values in data_dict.items()}

    update_clients = []
    for key, value in data_dict.items():
        for i in value:
            if baskets[number] == i:
                update_clients.append(key)
    myfunc(update_clients, baskets[number], stock_name)
    return baskets


# myfunc()


# def delete_cell():
#     subprocess.Popen(["python", "./delete.py"])


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


# def open_new_client_window():
#     subprocess.Popen(["python", "./new_client.py"])


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

# new_client_button = tk.Button(
#     window, text="Create New Client", command=open_new_client_window)
# new_client_button.pack(padx=10, pady=10)

# new_client_button = tk.Button(
#     window, text="Clear Data", command=delete_cell)
# new_client_button.pack(padx=20, pady=10)
window.mainloop()
