from tkinter import *
import sqlite3
import tkinter.messagebox
import os


#os environment
os.environ['TCL_LIBRARY'] = r"C:\Users\Mohammed Tousif\AppData\Local\Programs\Python\Python313\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Mohammed Tousif\AppData\Local\Programs\Python\Python313\tcl\tk8.6"

# Connect to SQLite database
conn = sqlite3.connect('inventory_system.db')  # SQLite uses a file-based database
mycursor = conn.cursor()

# Create table if not exists
mycursor.execute('''CREATE TABLE IF NOT EXISTS inventory (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        stock INTEGER,
                        price REAL)''')
conn.commit()

# Get the maximum ID
mycursor.execute("SELECT MAX(id) FROM inventory")
result = mycursor.fetchone()
id = result[0] if result[0] else 0  # Ensure ID is not None


class Database:
    def __init__(self, master):
        self.master = master
        self.master.configure(bg='#FBFFE4')  # Light Beige Background

        # Heading Label
        self.heading = Label(master, text="Update to the database", font=('Arial', 30, 'bold'), fg='#3D8D7A',
                             bg='#FBFFE4')
        self.heading.place(x=350, y=10)

        # Labels
        Label(master, text="Product ID", font=('Arial', 18, 'bold'), bg='#FBFFE4', fg='#3D8D7A').place(x=50, y=80)
        Label(master, text="Product Name", font=('Arial', 18, 'bold'), bg='#FBFFE4', fg='#3D8D7A').place(x=50, y=140)
        Label(master, text="Stock", font=('Arial', 18, 'bold'), bg='#FBFFE4', fg='#3D8D7A').place(x=50, y=190)
        Label(master, text="Cost Price", font=('Arial', 18, 'bold'), bg='#FBFFE4', fg='#3D8D7A').place(x=50, y=240)

        # Entry Fields with Equal Width
        entry_width = 25
        self.id_leb = Entry(master, font=('Arial', 18), width=entry_width, bg='#A3D1C6', fg='black')
        self.id_leb.place(x=250, y=80)

        self.name_e = Entry(master, font=('Arial', 18), width=entry_width, bg='#A3D1C6', fg='black')
        self.name_e.place(x=250, y=140)

        self.stock_e = Entry(master, font=('Arial', 18), width=entry_width, bg='#A3D1C6', fg='black')
        self.stock_e.place(x=250, y=190)

        self.cp_e = Entry(master, font=('Arial', 18), width=entry_width, bg='#A3D1C6', fg='black')
        self.cp_e.place(x=250, y=240)

        # Search Button
        self.btn_search = Button(master, text="🔍 Search", font=('Arial', 12, 'bold'), width=12, bg='#3D8D7A',
                                 fg='white', command=self.search)
        self.btn_search.place(x=600, y=75)

        # Update Button
        self.btn_update = Button(master, text='✅ Update Database', font=('Arial', 14, 'bold'), width=20, height=2,
                                 bg='#3D8D7A', fg='white', command=self.update)
        self.btn_update.place(x=150, y=300)

        # Log Text Box
        self.tbBox = Text(master, width=60, height=10, font=('Arial', 12), bg='#A3D1C6', fg='black')
        self.tbBox.place(x=600, y=120)

        self.tbBox.insert(END, f"🔹 ID has reached up to: {id}")

    def search(self):
        mycursor.execute("SELECT * FROM inventory WHERE id=?", (self.id_leb.get(),))
        result = mycursor.fetchone()
        if result:
            self.name_e.delete(0, END)
            self.name_e.insert(0, result[1])

            self.stock_e.delete(0, END)
            self.stock_e.insert(0, result[2])

            self.cp_e.delete(0, END)
            self.cp_e.insert(0, result[3])
        else:
            tkinter.messagebox.showerror("Error", "No record found with this ID")

    def update(self):
        name, stock, price = self.name_e.get(), self.stock_e.get(), self.cp_e.get()
        mycursor.execute("UPDATE inventory SET name=?, stock=?, price=? WHERE id=?",
                         (name, stock, price, self.id_leb.get()))
        conn.commit()
        tkinter.messagebox.showinfo("Success", "Database updated successfully!")
        self.tbBox.insert(END, f"\n✅ Updated: {name} | Stock: {stock} | Price: {price}")


root = Tk()
app = Database(root)
root.geometry("1000x500")
root.title("Inventory Management")
root.mainloop()
