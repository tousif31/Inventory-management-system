from tkinter import *
import sqlite3
import tkinter.messagebox
import subprocess
import os

#os environment
os.environ['TCL_LIBRARY'] = r"C:\Users\Mohammed Tousif\AppData\Local\Programs\Python\Python313\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Mohammed Tousif\AppData\Local\Programs\Python\Python313\tcl\tk8.6"

# Database Connection
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

# Create Users Table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password TEXT,
                    role TEXT)''')
conn.commit()

class Signup:
    def __init__(self, master):
        self.master = master
        self.master.title("Sign Up")
        self.master.geometry("400x400")
        self.master.config(bg="#A3D1C6")  # Background color

        Label(master, text="Sign Up", font=("Arial", 20, "bold"), bg="#A3D1C6", fg="#3D8D7A").pack(pady=20)

        Label(master, text="Username:", font=("Arial", 12), bg="#A3D1C6", fg="#3D8D7A").pack()
        self.username_entry = Entry(master, font=("Arial", 12))
        self.username_entry.pack(pady=5)

        Label(master, text="Password:", font=("Arial", 12), bg="#A3D1C6", fg="#3D8D7A").pack()
        self.password_entry = Entry(master, show="*", font=("Arial", 12))
        self.password_entry.pack(pady=5)

        Label(master, text="Select Role:", font=("Arial", 12), bg="#A3D1C6", fg="#3D8D7A").pack()

        # Dropdown for Role Selection
        self.role_var = StringVar()
        self.role_var.set("Select Role")  # Default text
        self.role_dropdown = OptionMenu(master, self.role_var, "admin", "employee")
        self.role_dropdown.config(font=("Arial", 12), bg="#B3D8A8", fg="black")
        self.role_dropdown.pack(pady=5)

        Button(master, text="Sign Up", command=self.signup, font=("Arial", 12), bg="#3D8D7A", fg="white", width=15).pack(pady=20)

    def signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = self.role_var.get()

        if role not in ["admin", "employee"]:
            tkinter.messagebox.showerror("Error", "Please select a valid role.")
            return

        try:
            cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
            conn.commit()
            tkinter.messagebox.showinfo("Success", "Account Created! Redirecting to Login...")

            self.master.destroy()  # Close Sign-Up Window
            subprocess.Popen(["python", "login.py"])  # Redirect to Login Page
        except sqlite3.IntegrityError:
            tkinter.messagebox.showerror("Error", "Username already exists.")

root = Tk()
app = Signup(root)
root.mainloop()
