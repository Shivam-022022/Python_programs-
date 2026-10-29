import tkinter as tk
root=tk.Tk()
root.title("Student Registration")
root.geometry("600x400")
tk.Label(root, text="Student Registration",
         font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root,text="Name").pack()
name=tk.Entry(root)
name.pack()
tk.Label(root,text="Roll No").pack()
rollno=tk.Entry(root)
rollno.pack()
tk.Label(root,text="Course").pack()
course=tk.Entry(root)
course.pack()
tk.Label(root, text="Email").pack()
email = tk.Entry(root)
email.pack()
def register():
    result.config(text="Registration submitted")
tk.Button(root, text="Register",
          command=register).pack(pady=10)
result = tk.Label(root, text="")
result.pack()
root.mainloop()


