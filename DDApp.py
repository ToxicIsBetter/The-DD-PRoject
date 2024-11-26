print()
print("Direct debits App")
print()

file = open("DirectDebits.csv", "a")


DDs = {}
row = []

while True:
    print()
    print("1. Add a new direct debit")
    print("2. View all direct debits")
    print("3. Print all direct debits")
    print("4. Exit")
    
    print()
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")        
        amount = float(input("Enter amount: "))
        DDs[name] = amount
        file.write(f"{name},{amount}\n")

    elif choice == "2":
        for name, amount in DDs.items():
            print(f"{name}: {amount}")

    elif choice == "3":
        for name in DDs.items():
            row.append()
            
    elif choice == "4":
        print("Goodbye!")  
        print()      
        break