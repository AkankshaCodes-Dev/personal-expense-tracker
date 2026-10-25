# Personal Expense Tracker using Python

## 📌 Project Overview

The Personal Expense Tracker is a beginner-friendly, console-based Python application that helps users record, view, and calculate their expenses.

It uses CSV file storage to save expense records and load them again when the application is restarted.

## ✨ Features

- **Add Expenses:** Record an expense name, amount, and category.
- **Expense Categories:** Choose from Food, Travel, Shopping, Bills, and Other.
- **View Expenses:** Display all valid saved expense records.
- **Calculate Total Spending:** Calculate the total amount spent.
- **CSV File Storage:** Store expenses in `expenses.csv`.
- **Persistent Data:** Load previously saved expenses when the application starts.
- **Input Validation:** Handle invalid menu choices, blank names, invalid categories, and non-numeric amounts.
- **Amount Validation:** Reject zero, negative, NaN, and infinite amounts.
- **Error Handling:** Handle common file reading and writing errors.

## 🛠️ Technologies Used

- Python 3
- `csv` module
- `math` module
- File handling
- Exception handling
- Lists and loops
- Conditional statements

## 📂 Expense Categories

1. Food
2. Travel
3. Shopping
4. Bills
5. Other

## 🚀 How to Run the Project

### Prerequisites

- Python 3 installed on your computer.

### Steps

1. Clone or download this repository.
2. Open the project folder in your terminal or code editor.
3. Run the Python file:

   ```bash
   python expense_tracker.py
   ```

4. Follow the on-screen menu to add expenses, view expenses, calculate total spending, or exit.

**Note:** The `expenses.csv` file is created when an expense is successfully saved. Run the program from the directory where you want this file to be stored.

## 🖥️ Application Menu

```text
==========================
 PERSONAL EXPENSE TRACKER
==========================

1. Add Expense
2. View Expenses
3. Show Total Spending
4. Exit
```

## 📚 What I Learned

While developing this project, I practised:

- Using variables, lists, and loops.
- Taking user input and converting data types.
- Applying conditional statements.
- Handling exceptions with `try` and `except`.
- Validating numeric input with the `math` module.
- Reading and writing CSV files.
- Loading and processing structured data.
- Calculating totals from stored records.
- Building a menu-driven Python application.

## 🔮 Future Improvements

- Add dates to expenses.
- Generate monthly spending summaries.
- Filter expenses by category.
- Create category-wise reports and charts.
- Add a graphical user interface.
- Export summaries for further data analysis.

## 👨‍💻 Author

Created as a Python learning project to practise programming fundamentals, data validation, and file handling.
