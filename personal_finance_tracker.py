budget = float(input("Enter your monthly budget limit: "))

while True:
    print("--- PERSONAL FINANCE TRACKER ---")
    print("1. Add an Expense")
    print("2. View All Expenses")
    print("3. Track Total Spend & Budget")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        item = input("What did you buy? ")
        price = float(input("How much did it cost? "))
        
        with open("expenses.txt", "a") as file:
            file.write(item + "," + str(price) + "\n")
            
        print("Expense saved successfully!")
        
    elif choice == "2":
        print("\n--- YOUR SAVED EXPENSES ---")
        try:
            with open("expenses.txt", "r") as file:
                for line in file:
                    print(line.strip())
        except FileNotFoundError:
            print("No expenses recorded yet. Try adding one first.")
            
    elif choice == "3":
        try:
            total_spend = 0.0
            
            with open("expenses.txt", "r") as file:
                for line in file:
                    cleaned_line = line.strip()
                    if "," in cleaned_line:
                        parts = cleaned_line.split(",")
                        price_string = parts[1]
                        total_spend += float(price_string)
            
            print(f"\nTotal amount spent so far: £{total_spend:.2f}")
            print(f"Your budget limit is: £{budget:.2f}")
            
            if total_spend > budget:
                over_by = total_spend - budget
                print(f"WARNING: You are OVER budget by £{over_by:.2f}!")
            else:
                remaining = budget - total_spend
                print(f" You have £{remaining:.2f} left in your budget.")
                
        except FileNotFoundError:
            print("No expenses recorded yet. Try adding an expense.")
            
    elif choice == "4":
        print("Goodbye!")
        break  
        
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")
