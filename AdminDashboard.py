from tkinter import *
import subprocess
import sys
import os

#os environment
os.environ['TCL_LIBRARY'] = r"C:\Users\Mohammed Tousif\AppData\Local\Programs\Python\Python313\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Mohammed Tousif\AppData\Local\Programs\Python\Python313\tcl\tk8.6"

class Dashboard:
    def __init__(self, master, username):
        self.master = master
        self.master.title("Admin Dashboard")
        self.master.geometry("500x450")
        self.master.configure(bg='#A3D1C6')  # Background color

        self.username = username  # Store username for welcome message

        # Top Frame (Welcome + Logout)
        self.top_frame = Frame(self.master, bg='#A3D1C6')
        self.top_frame.pack(fill=X, padx=10, pady=5, anchor=E)

        # Welcome Label (Left)
        self.welcome_label = Label(self.top_frame, text=f"Welcome, {self.username} 🟢", font=('Arial', 12, 'bold'),
                                   bg='#A3D1C6', fg='#3D8D7A')
        self.welcome_label.pack(side=LEFT, padx=10)

        # Logout Button (Right)
        self.logout_btn = Button(self.top_frame, text="🔓 Logout", font=('Arial', 10, 'bold'),
                                 fg='white', bg='red', padx=10, pady=5, command=self.logout)
        self.logout_btn.pack(side=RIGHT)

        # Title
        self.heading = Label(self.master, text="Admin Dashboard", font=('Arial', 20, 'bold'),
                             fg='black', bg='#A3D1C6')
        self.heading.pack(pady=20)

        # Buttons
        self.display_stock_btn = Button(self.master, text="📦 Display Stock", font=('Arial', 14, 'bold'),
                                        width=20, height=2, bg='#3D8D7A', fg='white',
                                        command=lambda: self.open_script("display.py"))
        self.display_stock_btn.pack(pady=10)

        self.update_db_btn = Button(self.master, text="🛠 Update Database", font=('Arial', 14, 'bold'),
                                    width=20, height=2, bg='#B3D8A8', fg='black',
                                    command=lambda: self.open_script("update.py"))
        self.update_db_btn.pack(pady=10)

        self.add_product_btn = Button(self.master, text="➕ Add Product", font=('Arial', 14, 'bold'),
                                      width=20, height=2, bg='#FBFFE4', fg='black',
                                      command=lambda: self.open_script("add_to_db.py"))
        self.add_product_btn.pack(pady=10)

        self.add_product_btn = Button(self.master, text="🗑 Delete Product", font=('Arial', 14, 'bold'),
                                      width=20, height=2, bg='red', fg='black',
                                      command=lambda: self.open_script("deleteproduct.py"))
        self.add_product_btn.pack(pady=10)

    def open_script(self, script_name):
        """Open another Python script in a new process."""
        try:
            subprocess.Popen(["python", script_name])
        except FileNotFoundError:
            print(f"Error: {script_name} not found. Make sure the file exists.")

    def logout(self):
        """Logs out the user by closing the dashboard and opening the login window."""
        self.master.destroy()  # Close the dashboard window
        subprocess.Popen(["python", "login.py"])  # Open the login window

# Run the Dashboard
if __name__ == "__main__":
    username = sys.argv[1] if len(sys.argv) > 1 else "Admin"
    root = Tk()
    app = Dashboard(root, username)
    root.mainloop()
