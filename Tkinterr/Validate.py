import tkinter as tk
from tkinter import messagebox
import re
def validate():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    mobile = mobile_entry.get().strip()
    if name == "":
        messagebox.showerror("Error", "Name is required")
    elif not name.replace(" ", "").isalpha():
        messagebox.showerror("Error", "Enter a valid name")
    elif not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        messagebox.showerror("Error", "Enter a valid email")
    elif not re.fullmatch(r"[6-9]\d{9}", mobile):
        messagebox.showerror("Error", "Enter a valid mobile number")
    else:
        messagebox.showinfo("Success", "All inputs are valid")
root = tk.Tk()
root.title("Form Validation")
root.geometry("350x280")
tk.Label(root, text="Form Validation",
         font=("Arial", 16, "bold")).pack(pady=10)
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()
tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root)
email_entry.pack()
tk.Label(root, text="Mobile Number").pack()
mobile_entry = tk.Entry(root)
mobile_entry.pack()
tk.Button(root, text="Validate",
          command=validate).pack(pady=15)
root.mainloop()