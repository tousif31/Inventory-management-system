from tkinter import *
from tkinter import messagebox
import sqlite3
import datetime
import os

#os environment
os.environ['TCL_LIBRARY'] = r"C:\Users\Mohammed Tousif\AppData\Local\Programs\Python\Python313\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Mohammed Tousif\AppData\Local\Programs\Python\Python313\tcl\tk8.6"

# Get today's date
date = datetime.datetime.now().date()

# Temporary lists for cart session
products_list = []
product_price = []
product_quantity = []
product_id = []

# Connect to SQLite database
conn = sqlite3.connect('inventory_system.db')
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        stock INTEGER NOT NULL CHECK(stock >= 0),
        price REAL NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        amount REAL NOT NULL,
        date TEXT NOT NULL
    )
''')

conn.commit()


class Application():
    def __init__(self, master):
        self.master = master

        # Color Palette
        bg_left = "#3D8D7A"   # Dark Green
        bg_right = "#A3D1C6"  # Light Green
        btn_color = "#B3D8A8" # Soft Green
        text_color = "#FBFFE4" # Off White

        # Left frame
        self.left = Frame(master, width=700, height=768, bg=bg_left)
        self.left.pack(side=LEFT)

        # Right frame
        self.right = Frame(master, width=666, height=768, bg=bg_right)
        self.right.pack(side=RIGHT)

        # Components
        self.heading = Label(self.left, text="Inventory System", font=('arial 40 bold'), fg=text_color, bg=bg_left)
        self.heading.place(x=10, y=10)

        self.date_l = Label(self.right, text="Today's Date: " + str(date), font=('arial 16 bold'), bg=bg_right,
                            fg='black')
        self.date_l.place(x=10, y=10)

        # Table invoice
        self.tproduct = Label(self.right, text="Products", font=('arial 18 bold'), bg=bg_right, fg='black')
        self.tproduct.place(x=10, y=60)

        self.tquantity = Label(self.right, text="Quantity", font=('arial 18 bold'), bg=bg_right, fg='black')
        self.tquantity.place(x=300, y=60)

        self.tamount = Label(self.right, text="Amount", font=('arial 18 bold'), bg=bg_right, fg='black')
        self.tamount.place(x=500, y=60)

        # Product ID entry
        self.enterid = Label(self.left, text="Enter Product ID", font=('arial 18 bold'), fg=text_color, bg=bg_left)
        self.enterid.place(x=10, y=80)

        self.enteride = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
        self.enteride.place(x=220, y=80)
        self.enteride.focus()

        # Search button
        self.search_btn = Button(self.left, text="Search", width=22, height=2, bg='orange', command=self.ajax)
        self.search_btn.place(x=380, y=120)

        # Generate Bill Button
        self.bill_btn = Button(self.right, text="Generate Bill", width=22, height=2, bg='green', fg='white',
                               command=self.generate_bill)
        self.bill_btn.place(x=250, y=500)

        # Total label
        self.total_l = Label(self.right, text="", font=('arial 30 bold'), bg=bg_right, fg='black')
        self.total_l.place(x=10, y=600)

    def ajax(self):
        self.get_id = self.enteride.get()

        # Fetch product info
        cursor.execute("SELECT * FROM inventory WHERE id=?", (self.get_id,))
        product = cursor.fetchone()

        if product:
            self.get_id, self.get_name, self.get_stock, self.get_price = product

            # Display product details
            self.productname = Label(self.left, text="Product Name: " + str(self.get_name), font=('arial 20 bold'),
                                     bg='lightgray', fg='black')
            self.productname.place(x=10, y=250)

            self.pprice = Label(self.left, text="Price: Rs. " + str(self.get_price), font=('arial 20 bold'), bg='lightgray',
                                fg='black')
            self.pprice.place(x=10, y=290)

            # Quantity label
            self.quantityl = Label(self.left, text="Enter Quantity", font=('arial 18 bold'), fg='white', bg='#3D8D7A')
            self.quantityl.place(x=10, y=350)

            self.quantity_e = Entry(self.left, width=25, font=('arial 18 bold'), bg='lightblue')
            self.quantity_e.place(x=190, y=350)
            self.quantity_e.focus()

            # Add to Cart button (FIXED)
            self.add_to_cart_btn = Button(self.left, text="Add to Cart", width=22, height=2, bg='#B3D8A8', fg='black',
                                          command=self.add_to_cart)
            self.add_to_cart_btn.place(x=350, y=400)
        else:
            messagebox.showinfo("Error", "Product not found!")

    def add_to_cart(self):
        try:
            quantity_value = int(self.quantity_e.get())

            # Check how much of this product is already in the cart
            existing_quantity = 0
            if self.get_name in products_list:
                index = products_list.index(self.get_name)
                existing_quantity = product_quantity[index]

            # Total quantity after adding new request
            total_requested = existing_quantity + quantity_value

            if total_requested > int(self.get_stock):
                messagebox.showinfo("Error",
                                    f"Not enough stock available! You already have {existing_quantity} in cart.")
            else:
                new_stock = int(self.get_stock) - quantity_value

                if new_stock < 5:
                    messagebox.showwarning("Stock Alert",
                                           f"Stock for {self.get_name} is critically low: {new_stock} left!")

                # Update stock in the database
                cursor.execute("UPDATE inventory SET stock=? WHERE id=?", (new_stock, self.get_id))
                conn.commit()

                final_price = float(quantity_value) * float(self.get_price)

                # If product is already in the cart, update its quantity and price
                if self.get_name in products_list:
                    index = products_list.index(self.get_name)
                    product_quantity[index] += quantity_value
                    product_price[index] += final_price
                else:
                    products_list.append(self.get_name)
                    product_price.append(final_price)
                    product_quantity.append(quantity_value)
                    product_id.append(self.get_id)

                # Display added products
                y_index = 100
                for i, p in enumerate(products_list):
                    Label(self.right, text=str(p), font=('arial 18 bold'), bg='#A3D1C6', fg='black').place(x=10, y=y_index)
                    Label(self.right, text=str(product_quantity[i]), font=('arial 18 bold'), bg='#A3D1C6',
                          fg='black').place(x=300, y=y_index)
                    Label(self.right, text="Rs. " + str(product_price[i]), font=('arial 18 bold'), bg='#A3D1C6',
                          fg='black').place(x=500, y=y_index)
                    y_index += 40

                # Update total
                self.total_l.configure(text="Total: Rs. " + str(sum(product_price)), bg='#A3D1C6', fg='black')

                # Reset input fields
                self.enteride.delete(0, END)

        except ValueError:
            messagebox.showinfo("Error", "Please enter a valid quantity.")

    def generate_bill(self):
        messagebox.showinfo("Success", "Transaction Completed!")
        self.master.destroy()


# Run the application
root = Tk()
Application(root)
root.geometry("1366x768+0+0")
root.title("Inventory Management System (SQLite)")
root.mainloop()
