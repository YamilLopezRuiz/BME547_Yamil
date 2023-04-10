import tkinter as tk

filename = None

def main_window():

    filename = None

    def btn_cmd():
        nonlocal filename
        filename = "hello.jpg"
    
    root = tk.Tk()

    label = tk.Label(root, text="My label")

    btn = tk.Button(root, text="ok", command=btn_cmd)

    root.mainloop()