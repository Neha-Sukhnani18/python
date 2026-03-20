import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 6:
            messagebox.showwarning("Warning", "Length should be at least 6")
            return
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))

    password_field.delete(0, tk.END)
    password_field.insert(0, password)

window = tk.Tk()
window.title("Password Generator")
window.geometry("300x200")

tk.Label(window, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(window)
length_entry.pack()
length_entry.insert(0, "12") 
generate_btn = tk.Button(window, text="Generate", command=generate_password)
generate_btn.pack(pady=10)

password_field = tk.Entry(window, width=30)
password_field.pack(pady=5)

window.mainloop()
