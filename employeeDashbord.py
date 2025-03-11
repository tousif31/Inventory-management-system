from tkinter import *
import subprocess
import os

#os environment
os.environ['TCL_LIBRARY'] = r"C:\Users\Mohammed Tousif\AppData\Local\Programs\Python\Python313\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Mohammed Tousif\AppData\Local\Programs\Python\Python313\tcl\tk8.6"

class Dashboard:
    def __init__(self, master, username):
        self.master = master
        self.master.title("Inventory Management Dashboard")
        self.master.geometry("500x400")
        self.master.configure(bg='#A3D1C6')  # Background color

        self.username = username  # Store username for welcome message

        # Top Frame for Welcome Message & Logout Button
        self.top_frame = Frame(self.master, bg='#A3D1C6')
        self.top_frame.pack(fill=X, padx=10, pady=5, anchor=E)

        # Welcome Label (Left Side)
        self.welcome_label = Label(self.top_frame, text=f"Welcome 🟢", font=('Arial', 12, 'bold'),
                                   bg='#A3D1C6', fg='#3D8D7A')
        self.welcome_label.pack(side=LEFT, padx=10)

        # Logout Button (Right Side)
        self.logout_btn = Button(self.top_frame, text="🔓 Logout", font=('Arial', 10, 'bold'),
                                 fg='white', bg='red', padx=10, pady=5, command=self.logout)
        self.logout_btn.pack(side=RIGHT)

        # Title
        self.heading = Label(self.master, text="Employee Dashboard", font=('Arial', 20, 'bold'),
                             fg='black', bg='#A3D1C6')
        self.heading.pack(pady=20)

        # Buttons to Open Different Scripts
        self.display_stock_btn = Button(self.master, text="📦 Display Stock", font=('Arial', 14, 'bold'),
                                        width=20, height=2, bg='#3D8D7A', fg='white',
                                        command=lambda: self.open_script("display.py"))
        self.display_stock_btn.pack(pady=10)

        self.main_btn = Button(self.master, text="🏠 Main Menu", font=('Arial', 14, 'bold'),
                               width=20, height=2, bg='#B3D8A8', fg='black',
                               command=lambda: self.open_script("main.py"))
        self.main_btn.pack(pady=10)

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

# Run the Dashboard (Pass username dynamically)
if __name__ == "__main__":
    root = Tk()
    app = Dashboard(root, username="JohnDoe")  # Change username dynamically
    root.mainloop()
