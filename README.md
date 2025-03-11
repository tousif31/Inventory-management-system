📌 Overview


The Inventory Management System is a desktop application built using Python (Tkinter for GUI) and SQLite for database management. This system allows businesses to efficiently track and manage their inventory, search for products, update stock levels, process transactions, and generate bills.

🔹 Key Features

✅ Product Management:

Add and update product details (name, stock, price).
Search for products using product ID.

✅ Stock Management:

Displays current stock levels.
Prevents adding items to the cart if stock is insufficient.
Alerts when stock falls below a critical level (e.g., less than 5).

✅ Cart System:

Add products to the cart.
Update quantity dynamically.
Calculate total cost in real-time.

✅ Transaction Processing:

Generate invoices when the customer purchases items.
Deduct purchased quantity from stock.
Save transactions in a database for future reference.

✅ User-Friendly Interface:

Two-panel UI (left for product search & input, right for invoice display).
Color-coded interface for better visibility.

✅ Data Persistence (SQLite Database):

inventory Table: Stores product details.
transactions Table: Stores purchase records with date, product name, quantity, and total amount.

🔹 Technologies Used

Python: Core programming language.
Tkinter: GUI framework for the desktop application.
SQLite: Lightweight database for storing product and transaction details.
OS Module: Configures environment paths for Tcl/Tk.
Datetime Module: Fetches current date for transactions.

🔹 Workflow

1️⃣ User enters a product ID → Searches the product in the database. 

2️⃣ Product details are displayed → User enters the quantity.

3️⃣ Stock validation occurs → Ensures stock availability.

4️⃣ Product is added to the cart → Updates the total price dynamically.

5️⃣ User confirms the purchase → Updates stock and saves transaction history.

6️⃣ Bill is generated → Clears UI for the next transaction.


🔹 Future Enhancements (Optional Upgrades)

🚀 Generate PDF invoices for billing.

🚀 Add Admin Panel for adding/removing products.

🚀 Implement Barcode Scanning for faster product search.

🚀 Connect to an Online Database (MySQL/PostgreSQL) for remote access.

![1](https://github.com/user-attachments/assets/3651b862-6497-4797-a1db-3b0524d409e7)

![2](https://github.com/user-attachments/assets/e788aa61-6f6a-433f-b1cb-6db3bf0474d5)

![3](https://github.com/user-attachments/assets/e1a6354e-25f2-43f5-9dca-bf6b181851bf)

![4](https://github.com/user-attachments/assets/fba33fbd-52bc-4bfd-a13e-de218b1f14d4)

![5](https://github.com/user-attachments/assets/ade2e84a-b311-40ca-ba8c-ddf6e71eb87f)

![6](https://github.com/user-attachments/assets/eaeb37c1-bacf-46f3-b96d-a61abd1cae9f)





💻 Installation & Setup
Follow these steps to run the project locally:

📥 1. Clone the Repository

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

2️⃣ Install Dependencies

pip install tkinter sqlite3

3️⃣ Run the Application

python login.py



📞 Contact

📧 Email: mohammedtousif3709@gmail.com
