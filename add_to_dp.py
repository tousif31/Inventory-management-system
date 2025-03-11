import sqlite3
from tkinter import *
import tkinter.messagebox
import os

#os environment
os.environ['TCL_LIBRARY'] = r"C:\Users\Mohammed Tousif\AppData\Local\Programs\Python\Python313\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Mohammed Tousif\AppData\Local\Programs\Python\Python313\tcl\tk8.6"

# Connect to SQLite database
conn = sqlite3.connect('inventory_system.db')
mycursor = conn.cursor()

# Create table if not exists
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        stock INTEGER NOT NULL,
        price REAL NOT NULL
    )
""")
conn.commit()


class Database:
    def __init__(self, master):
        self.master = master

        # Colors from ColorHunt
        bg_left = "#3D8D7A"  # Dark Green
        btn_color = "#B3D8A8"  # Soft Green
        text_color = "#FBFFE4"  # Off White
        bg_right = "#A3D1C6"  # Light Green

        # Configure root window to remove gaps
        self.master.configure(bg=bg_left)

        # Left Frame (Input Section)
        self.left_frame = Frame(master, width=700, height=768, bg=bg_left)
        self.left_frame.pack(side=LEFT, fill=Y)

        # Right Frame (Log Section)
        self.right_frame = Frame(master, width=666, height=768, bg=bg_right)
        self.right_frame.pack(side=RIGHT, fill=Y)

        # Remove the white gap between frames
        self.left_frame.pack_propagate(False)
        self.right_frame.pack_propagate(False)

        # Heading
        self.heading = Label(self.left_frame, text="Add to Database", font=('arial 40 bold'), fg=text_color, bg=bg_left)
        self.heading.place(x=150, y=10)

        # Labels
        Label(self.left_frame, text="Enter Product ID", font=('arial 18 bold'), fg=text_color, bg=bg_left).place(x=20, y=80)
        Label(self.left_frame, text="Enter Product Name", font=('arial 18 bold'), fg=text_color, bg=bg_left).place(x=20, y=140)
        Label(self.left_frame, text="Enter Stock Quantity", font=('arial 18 bold'), fg=text_color, bg=bg_left).place(x=20, y=200)
        Label(self.left_frame, text="Enter Cost Price", font=('arial 18 bold'), fg=text_color, bg=bg_left).place(x=20, y=260)

        # Entry fields
        self.id_e = Entry(self.left_frame, width=25, font=('arial 18 bold'), bg="lightblue")
        self.id_e.place(x=320, y=80)

        self.name_e = Entry(self.left_frame, width=25, font=('arial 18 bold'), bg="lightblue")
        self.name_e.place(x=320, y=140)

        self.stock_e = Entry(self.left_frame, width=25, font=('arial 18 bold'), bg="lightblue")
        self.stock_e.place(x=320, y=200)

        self.cp_e = Entry(self.left_frame, width=25, font=('arial 18 bold'), bg="lightblue")
        self.cp_e.place(x=320, y=260)

        # Buttons
        self.btn_clear = Button(self.left_frame, text="Clear Fields", width=15, height=2, bg='red', fg='white',
                                font=('arial 12 bold'), command=self.clear_all)
        self.btn_clear.place(x=180, y=350)

        self.btn_add = Button(self.left_frame, text='Add to Database', width=20, height=2, bg=btn_color, fg='black',
                              font=('arial 12 bold'), command=self.get_items)
        self.btn_add.place(x=380, y=350)

        # Log Section Title
        Label(self.right_frame, text="Log", font=('arial 22 bold'), bg=bg_right, fg='black').place(x=280, y=20)

        # Log Textbox
        self.tbBox = Text(self.right_frame, width=60, height=20, font=('arial 14'))
        self.tbBox.place(x=50, y=70)

        # Keyboard Shortcuts
        self.master.bind('<Return>', self.get_items)
        self.master.bind('<Up>', self.clear_all)

    def get_items(self, *args):
        # Get data from input fields
        product_id = self.id_e.get().strip()
        name = self.name_e.get().strip()
        stock = self.stock_e.get().strip()
        cp = self.cp_e.get().strip()

        # Validate inputs
        if not product_id or not name or not stock or not cp:
            tkinter.messagebox.showinfo("Error", "All fields are required!")
            return

        try:
            product_id = int(product_id)
            stock = int(stock)
            cp = float(cp)

            # Check if Product ID already exists
            mycursor.execute("SELECT id FROM inventory WHERE id=?", (product_id,))
            if mycursor.fetchone():
                tkinter.messagebox.showerror("Error", f"Product ID {product_id} already exists!")
                return

            # Insert into the database
            mycursor.execute("INSERT INTO inventory (id, name, stock, price) VALUES (?, ?, ?, ?)", (product_id, name, stock, cp))
            conn.commit()

            # Update log
            self.tbBox.insert(END, f"\nInserted {name} (ID: {product_id}) into the database with stock {stock}")
            tkinter.messagebox.showinfo("Success", "Successfully added to the database")

        except ValueError:
            tkinter.messagebox.showerror("Error", "Product ID & Stock must be integers, and Price must be a number.")
        except Exception as e:
            tkinter.messagebox.showerror("Database Error", str(e))

    def clear_all(self, *args):
        self.id_e.delete(0, END)
        self.name_e.delete(0, END)
        self.stock_e.delete(0, END)
        self.cp_e.delete(0, END)


# Initialize Tkinter
root = Tk()
b = Database(root)
root.geometry("1366x768")
root.title("Add to Database")
root.mainloop()
