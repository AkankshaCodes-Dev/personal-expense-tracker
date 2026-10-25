import csv
import math
print("==========================")
print(" PERSONAL EXPENSE TRACKER ")  
print("==========================")
expenses = []
valid_categories = ["Food", "Travel", "Shopping", "Bills", "Other"]
try:
      with open("expenses.csv","r",newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                  try:
                      if len(row) != 3:
                        continue
                      expense_name = row[0].strip()
                      amount = float(row[1])
                      category = row[2].strip()
                  
                      if(
                            expense_name
                            and math.isfinite(amount)
                            and amount > 0
                            and category in valid_categories
                      ):
                        expenses.append([expense_name,amount,category])
                  except ValueError:
                        continue
                    
except FileNotFoundError:
      pass    
except OSError as error:
      print("Could not read expenses file:", error)                    

while True:
         print("\n1. Add Expense")
         print("2. View Expenses")
         print("3. Show Total Spending")
         print("4. Exit")
         try:
             choice = int(input("Enter Your Choice: "))
         except ValueError:
               print("Invalid input. Please enter a number.") 
               continue   
         if choice == 1:
              expense_name = input("Enter expense name:").strip()
              if expense_name == "":
                    print("Expense name cannot be empty.")
                    continue
              print("\n=== EXPENSE CATEGORIES ===")
              print("1. Food")
              print("2. Travel")
              print("3. Shopping")
              print("4. Bills")
              print("5. Other")
              try:
                  category_choice = int(input("Choose a category (1-5): ")) 
              except ValueError:
                    print("Invalid input. Please enter a number from 1 to 5.")
                    continue    
              if category_choice == 1:
                    category = "Food"
              elif category_choice == 2:
                    category = "Travel"
              elif category_choice == 3:
                    category = "Shopping"
              elif category_choice == 4:
                    category = "Bills"
              elif category_choice == 5:
                    category = "Other"
              else:
                    print("Invalid Category choice.")
                    continue                                   
  
              try:
                  amount = float(input("Enter amount:"))
                  if not math.isfinite(amount) or amount <= 0:
                        print("Amount must be greater than zero.")
                  else:      
                        expense = [expense_name,amount,category]
                        try:
                            with open("expenses.csv", "a",newline="") as file:
                                writer = csv.writer(file)
                                writer.writerow(expense)
                            expenses.append(expense)    
                            print("Expense added successfully!")
                        except OSError as error:
                             print("Could not save expense:", error) 
              except  ValueError:
                    print("Invalid amount. Please enter a number")                   
         elif choice == 2:
                 print("\n=== YOUR EXPENSES ===")
                 if len(expenses) == 0:
                         print("No expenses recorded yet.")
                 else:
                        for expense in expenses:
                             print("Expense:",expense[0], "| Amount:  ₹",expense[1], "| Category:",expense[2])
         elif choice == 3:            
                total = 0
                for expense in expenses:
                    total = total + expense[1]
                print("Total Spending:  ₹",total ) 
         elif choice == 4:
                print("Thank you using Expense Tracker!")
                break
         else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")              