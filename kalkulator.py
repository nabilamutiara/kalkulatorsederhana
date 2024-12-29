import tkinter as tk
from tkinter import messagebox
import math


def click(button_text):
    current_text = entry.get()
    if current_text == "ERROR":
        entry.delete(0, tk.END)
        current_text = ""
    entry.insert(tk.END, button_text)


def clear():
    entry.delete(0, tk.END)


def calculate():
    try:
        expression = entry.get()
        result = eval(expression)  
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "ERROR")


def sqrt():
    try:
        value = float(entry.get())
        result = math.sqrt(value)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "ERROR")


def square():
    try:
        value = float(entry.get())
        result = value ** 2
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "ERROR")


root = tk.Tk()
root.title("Calculator")

# Menyesuaikan ukuran jendela
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 400
window_height = 600
window_x = (screen_width - window_width) // 2
window_y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")


entry = tk.Entry(root, font=("Arial", 24), borderwidth=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=15, padx=10, pady=10)


buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("(", 4, 2), (")", 4, 3),
    ("C", 5, 0), ("√", 5, 1), ("x²", 5, 2), ("+", 5, 3),
    ("=", 6, 0),
]


for (text, row, col) in buttons:
    if text == "=":
        button = tk.Button(root, text=text, font=("Arial", 18), command=calculate)
        button.grid(row=row, column=col, columnspan=4, sticky="nsew", padx=10, pady=10, ipadx=40, ipady=20)
    elif text == "C":
        button = tk.Button(root, text=text, font=("Arial", 18), command=clear)
        button.grid(row=row, column=col, sticky="nsew", padx=10, pady=10, ipadx=20, ipady=20)
    elif text == "√":
        button = tk.Button(root, text=text, font=("Arial", 18), command=sqrt)
        button.grid(row=row, column=col, sticky="nsew", padx=10, pady=10, ipadx=20, ipady=20)
    elif text == "x²":
        button = tk.Button(root, text=text, font=("Arial", 18), command=square)
        button.grid(row=row, column=col, sticky="nsew", padx=10, pady=10, ipadx=20, ipady=20)
    else:
        button = tk.Button(root, text=text, font=("Arial", 18), command=lambda t=text: click(t))
        button.grid(row=row, column=col, sticky="nsew", padx=10, pady=10, ipadx=20, ipady=20)


for i in range(7):  
    root.grid_rowconfigure(i, weight=1)
for i in range(4):  
    root.grid_columnconfigure(i, weight=1)


root.mainloop()
