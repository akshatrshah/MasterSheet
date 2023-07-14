import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from change_weightage_logic import change_weightage
from main import get_clients, get_corresponding_baskets


def submit_values():
    client = client_dropdown.get()
    if not client:
        messagebox.showerror("Error", "Please select a client.")
        return

    baskets = get_corresponding_baskets(client)
    if baskets:
        values = {}
        for index, basket in enumerate(baskets):
            value = entry_list[index].get()
            if not value.isdigit():
                messagebox.showerror(
                    "Error", "Please enter a valid numerical value for each basket.")
                return
            values[basket] = int(value)
        print(values)

        change_weightage(client, values)

        messagebox.showinfo("Success", "Values submitted successfully.")
    else:
        messagebox.showinfo(
            "No Baskets", "No corresponding baskets found for the selected client.")


def on_client_select(event):
    client = client_dropdown.get()
    if client:
        baskets = get_corresponding_baskets(client)
        if baskets:
            # Clear existing entries
            for entry in entry_list:
                entry.destroy()
            entry_list.clear()

            # Create new entries for each basket
            for index, basket in enumerate(baskets):
                label = tk.Label(window, text=basket)
                label.grid(row=index+1, column=0,
                           padx=10, pady=10, sticky=tk.W)
                entry = tk.Entry(window)
                entry.grid(row=index+1, column=1,
                           padx=10, pady=10, sticky=tk.W)
                entry_list.append(entry)
        else:
            messagebox.showinfo(
                "No Baskets", "No corresponding baskets found for the selected client.")

        # Adjust window size based on content
        update_window_size()


def update_window_size():
    num_baskets = len(entry_list)
    # Adjust height based on the number of baskets
    new_height = num_baskets * 50 + 120
    window.geometry(f"500x{new_height}")

    # Adjust padx and pady based on the number of baskets
    padx = 20
    pady = 20 + num_baskets * 5
    window.configure(padx=padx, pady=pady)


window = tk.Tk()
window.title("Numerical Input")
window.geometry("500x250")
window.configure(padx=20, pady=20)  # Increase padx and pady for more padding

clients = get_clients()
client_label = ttk.Label(window, text="Select Client:")
client_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
client_dropdown = ttk.Combobox(window, values=clients, state='readonly')
client_dropdown.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

entry_list = []

client_dropdown.bind("<<ComboboxSelected>>", on_client_select)

submit_button = tk.Button(window, text="Submit", command=submit_values)
submit_button.grid(row=len(clients)+1, columnspan=2, padx=10, pady=10)

window.mainloop()
