from tkinter import *
import sqlite3
import subprocess
import tkinter.messagebox
import os

#os environment
os.environ['TCL_LIBRARY'] = r"C:\Users\Mohammed Tousif\AppData\Local\Programs\Python\Python313\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Mohammed Tousif\AppData\Local\Programs\Python\Python313\tcl\tk8.6"

# Database Connection
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

class Login:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")
        self.master.geometry("400x350")
        self.master.config(bg="#A3D1C6")  # Background color

        Label(master, text="Login", font=("Arial", 20, "bold"), bg="#A3D1C6", fg="#3D8D7A").pack(pady=20)

        Label(master, text="Username:", font=("Arial", 12), bg="#A3D1C6", fg="#3D8D7A").pack()
        self.username_entry = Entry(master, font=("Arial", 12))
        self.username_entry.pack(pady=5)

        Label(master, text="Password:", font=("Arial", 12), bg="#A3D1C6", fg="#3D8D7A").pack()
        self.password_entry = Entry(master, show="*", font=("Arial", 12))
        self.password_entry.pack(pady=5)

        Button(master, text="Login", command=self.login, font=("Arial", 12), bg="#3D8D7A", fg="white", width=15).pack(pady=10)

        Label(master, text="New User? Sign up below!", font=("Arial", 10), bg="#A3D1C6", fg="#3D8D7A").pack(pady=5)
        Button(master, text="Sign Up", command=self.open_signup, font=("Arial", 12), bg="#B3D8A8", fg="black", width=10).pack(pady=5)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        cursor.execute("SELECT role FROM users WHERE username=? AND password=?", (username, password))
        result = cursor.fetchone()

        if result:
            role = result[0]
            if role == "admin":
                tkinter.messagebox.showinfo("Login Success", "Redirecting to Admin Dashboard...")
                self.master.destroy()
                subprocess.Popen(["python", "AdminDashboard.py"])
            elif role == "employee":
                tkinter.messagebox.showinfo("Login Success", "Redirecting to Employee Dashboard...")
                self.master.destroy()
                subprocess.Popen(["python", "employeeDashbord.py"])
        else:
            tkinter.messagebox.showerror("Login Failed", "Invalid Username or Password.")

    def open_signup(self):
        self.master.destroy()  # Close Login Window
        subprocess.Popen(["python", "signup.py"])  # Open Sign-Up Page

root = Tk()
app = Login(root)
root.mainloop()
