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

personal_expense_tracker/ # Project root folder
│── expense_tracker/ # Main program file
│ │── init.py # Marks folder as a Python package
│ │── cli.py # 
│ │── tracker.py # Holds the core logic
│
│── README.md # Project documentation
│── setup.py # Makes project installable as a Python package
│── requirements.txt # Lists dependencies needed to run the project
│── expenses.txt # Saved expenses (auto-created if missing)


---


## ⚡ Installation

1. Clone this repository:

```bash
git clone https://github.com/Laju-okoro/personal_expense_tracker.git
cd personal_expense_tracker


2. Install dependencies:

pip install -r requirements.txt


or install manually:

pip install colorama


---


##▶️ Usage

Run the CLI program with:

python -m expense_tracker.cli


You’ll see a menu like this:

=== Personal Expense Tracker ===
1. ➕ Add Expense
2. 📜 View All Expenses
3. 📊 View Summary by Category
4. 🔍 Search Expenses by Category
5. 🗑️ Delete an Expense
6. ❌ Exit


---


## 📝 Example

Adding an expense:

Enter amount: 12.50
Enter category (e.g., Food, Transport): Food
Enter description: Lunch
✅ Expense added successfully!


Viewing all expenses:

--- All Expenses ---
#   Date & Time          Category     Amount       Description
1   2025-09-01 10:30:00  Food         $12.50       Lunch


---



## 📦Installation as a Package

You can also install it locally as a package:

pip install .


Then run it with:

expense-tracker


---

## 📦 Requirements

Python 3.6+

colorama


---


## 🤝 Contributing

Contributions are welcome!


---


##👩‍💻 Author

Created with ❤️ by Laju Okoro