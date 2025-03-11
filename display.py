from tkinter import *
import sqlite3
from tkinter import ttk
import os

#os environment
os.environ['TCL_LIBRARY'] = r"C:\Users\Mohammed Tousif\AppData\Local\Programs\Python\Python313\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Mohammed Tousif\AppData\Local\Programs\Python\Python313\tcl\tk8.6"

# Database Connection
conn = sqlite3.connect('inventory_system.db')
mycursor = conn.cursor()


class DisplayStock:
    def __init__(self, master):
        self.master = master
        self.master.title("Stock Availability")
        self.master.geometry("650x450")
        self.master.configure(bg='#FBFFE4')  # Background color

        # Title
        self.heading = Label(self.master, text="Available Stock", font=('Arial', 20, 'bold'),
                             fg='#3D8D7A', bg='#FBFFE4')
        self.heading.pack(pady=10)

        # Create a table using Treeview with colors
        self.tree_frame = Frame(self.master, bg='#A3D1C6', bd=2, relief=RIDGE)
        self.tree_frame.pack(pady=10, padx=20, fill=BOTH, expand=True)

        self.tree = ttk.Treeview(self.tree_frame, columns=("ID", "Product Name", "Stock", "Price"), show="headings")

        self.tree.heading("ID", text="ID")
        self.tree.heading("Product Name", text="Product Name")
        self.tree.heading("Stock", text="Stock")
        self.tree.heading("Price", text="Price (Rs.)")

        self.tree.column("ID", width=50, anchor=CENTER)
        self.tree.column("Product Name", width=220, anchor=W)
        self.tree.column("Stock", width=100, anchor=CENTER)
        self.tree.column("Price", width=100, anchor=CENTER)

        self.tree.pack(padx=10, pady=10, fill=BOTH, expand=True)

        # Scrollbar
        self.scrollbar = Scrollbar(self.tree_frame, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        # Refresh Button
        self.refresh_btn = Button(self.master, text="🔄 Refresh Stock", font=('Arial', 14, 'bold'),
                                  bg='#3D8D7A', fg='white', padx=10, pady=5, command=self.display_stock)
        self.refresh_btn.pack(pady=10)

        self.display_stock()  # Initial display

    def display_stock(self):
        # Clear previous data
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Fetch stock data from database
        mycursor.execute("SELECT * FROM inventory")
        rows = mycursor.fetchall()

        # Insert data into table
        for row in rows:
            self.tree.insert("", "end", values=row)


# Run the GUI
root = Tk()
app = DisplayStock(root)
root.mainloop()
