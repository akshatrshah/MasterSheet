import tkinter as tk
import subprocess


def run_tkinter_app():
    # Replace 'tkinter_app.py' with the name of your Tkinter application script
    subprocess.Popen(['python', 'runner.py'])


window = tk.Tk()
window.title("Lets Start")
window.geometry('+0+0')

button = tk.Button(window, text="CLICK HERE TO START", command=run_tkinter_app)
button.pack(padx=300, pady=300)

window.mainloop()
