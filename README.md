# 💰 Personal Expense Tracker using Python

A beginner-friendly, console-based Python application to record, view, and calculate personal expenses using CSV file storage.

## 📌 Project Overview

The Personal Expense Tracker helps users manage expense records through a simple menu-driven application. It stores expense data in a CSV file so that saved expenses can be loaded again when the program restarts.

## ✨ Features

- ➕ Add expenses with a name, amount, and category.
- 📂 Choose from five categories: Food, Travel, Shopping, Bills, and Other.
- 📋 View saved expense records.
- 💵 Calculate total spending.
- 💾 Store expenses in a CSV file.
- 🔄 Load previously saved expenses when the application starts.
- ✅ Validate expense names, categories, and amounts.
- 🛡️ Handle invalid inputs and common file errors.

## 🛠️ Technologies Used

- **Python 3**
- `csv` module — reading and writing expense records.
- `math` module — validating finite numeric amounts.
- File handling and exception handling.
- Lists, loops, and conditional statements.

## 📂 Project Structure

```text
personal-expense-tracker/
├── expense_tracker.py
├── README.md
└── expenses.csv  # Generated when expenses are saved
```

The CSV file is generated at runtime and is not required to be uploaded with the source code.

## 🚀 How to Run

### Prerequisite

Install Python 3 on your computer.

### Instructions

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run the application:

   ```bash
   python expense_tracker.py
   ```

4. Follow the menu to add expenses, view expenses, calculate total spending, or exit.


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

Through this project, I practised:

- Python fundamentals and data types.
- Lists and loops.
- Conditional statements.
- User input and type conversion.
- Input validation and exception handling.
- Reading and writing CSV files.
- Loading and processing structured data.
- Calculating totals from stored records.
- Building a menu-driven console application.

## 🔮 Future Improvements

- Add dates to expenses.
- Generate monthly spending summaries.
- Filter expenses by category.
- Create category-wise reports and charts.
- Develop a graphical user interface.
- Export data for further analysis.

## 👩‍💻 Author

**AkankshaCodes-Dev**

GitHub: [@AkankshaCodes-Dev](https://github.com/AkankshaCodes-Dev)

---

*Created as a Python learning project to practise programming fundamentals and data handling.*
