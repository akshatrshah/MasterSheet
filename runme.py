import tkinter as tk
import subprocess


def run_tkinter_app():
    # Replace 'tkinter_app.py' with the name of your Tkinter application script
    subprocess.Popen(['python', 'runner.py'])


root = tk.Tk()
root.title("Master R&D")

button = tk.Button(root, text="CLICK HERE TO START", command=run_tkinter_app)
button.pack(pady=20)

root.mainloop()
