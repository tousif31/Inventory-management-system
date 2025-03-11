import sqlite3
from tkinter import *
from tkinter import ttk
import os

# os environment
os.environ['TCL_LIBRARY'] = r"C:\Users\Mohammed Tousif\AppData\Local\Programs\Python\Python313\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Mohammed Tousif\AppData\Local\Programs\Python\Python313\tcl\tk8.6"


class DisplayUsers:
    def __init__(self, master):
        self.master = master
        self.master.title("User Database")
        self.master.geometry("600x400")
        self.master.configure(bg="#A3D1C6")  # Beige Background

        # Frame for UI
        frame = Frame(self.master, bg="#B3D8A8", padx=20, pady=20, relief=GROOVE, bd=3)
        frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Title Label
        Label(frame, text="👤 Users Database", font=("Arial", 18, "bold"), fg="white", bg="#3D8D7A").pack(pady=10, fill=X)

        # Treeview (Table)
        self.tree = ttk.Treeview(frame, columns=("ID", "Username", "Password", "Role"), show="headings", height=8)
        self.tree.heading("ID", text="ID")
        self.tree.heading("Username", text="Username")
        self.tree.heading("Password", text="Password")
        self.tree.heading("Role", text="Role")

        self.tree.column("ID", width=50, anchor=CENTER)
        self.tree.column("Username", width=150, anchor=CENTER)
        self.tree.column("Password", width=150, anchor=CENTER)
        self.tree.column("Role", width=100, anchor=CENTER)

        self.tree.pack(pady=10, fill=BOTH, expand=True)

        # Scrollbar
        scrollbar = Scrollbar(frame, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Refresh Button
        self.refresh_btn = Button(frame, text="🔄 Refresh", font=('Arial', 12, 'bold'),
                                  bg="#3D8D7A", fg="white", width=15, height=1, cursor="hand2",
                                  command=self.load_users)
        self.refresh_btn.pack(pady=10)

        self.refresh_btn.bind("<Enter>", lambda e: self.refresh_btn.config(bg="#FBFFE4", fg="black"))
        self.refresh_btn.bind("<Leave>", lambda e: self.refresh_btn.config(bg="#3D8D7A", fg="white"))

        self.load_users()

    def load_users(self):
        """Fetches and displays users from the database."""
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")  # Fetch all users
        rows = cursor.fetchall()

        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)

        # Insert new data
        for row in rows:
            self.tree.insert("", END, values=row)

        conn.close()


# Run the Application
root = Tk()
app = DisplayUsers(root)
root.mainloop()
