# 💰 Personal Expense Tracker (CLI)

A simple **command-line expense tracker** built with Python.  
It allows you to **add, view, summarize, search, and delete expenses** stored in a text file.  
Colored outputs make the CLI more user-friendly (thanks to [Colorama](https://pypi.org/project/colorama/)).

---

## ✨ Features

- ➕ **Add Expense** — record an expense with amount, category, and description.  
- 📜 **View All Expenses** — display all expenses in a neat table.  
- 📊 **Summary by Category** — see total expenses grouped by category.  
- 🔍 **Search by Category** — quickly find expenses in a given category.  
- 🗑️ **Delete Expense** — remove an expense by its number.  
- 💾 Data saved persistently in `expenses.txt`.

---

## 📂 Project Structure

personal_expense_tracker/
│── expense_tracker.py # Main program file
│── expenses.txt # Saved expenses (auto-created if missing)
│── README.md # Project documentation


---

## ⚡ Installation

1. Clone this repository:

```bash
git clone https://github.com/your-username/personal-expense-tracker.git
cd personal-expense-tracker


Install dependencies:

pip install -r requirements.txt


or install manually:

pip install colorama

▶️ Usage

Run the tracker with:

python expense_tracker.py


You’ll see a menu like this:

=== Personal Expense Tracker ===
1. ➕ Add Expense
2. 📜 View All Expenses
3. 📊 View Summary by Category
4. 🔍 Search Expenses by Category
5. 🗑️ Delete an Expense
6. ❌ Exit

📝 Example

Adding an expense:

Enter amount: 12.50
Enter category (e.g., Food, Transport): Food
Enter description: Lunch
✅ Expense added successfully!


Viewing all expenses:

--- All Expenses ---
#   Date & Time          Category     Amount       Description
1   2025-09-01 10:30:00  Food         $12.50       Lunch

📦 Requirements

Python 3.6+

colorama

🤝 Contributing

Contributions are welcome!
Feel free to fork this project and submit a pull request.

📜 License

This project is licensed under the MIT License.