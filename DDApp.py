import os
import csv
import shutil

print()
print("Direct debits App")
print()

file = open("../DirectDebits.csv", "w+")


DDs = []
rows = []

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
        date = input("Enter date: ")
        bank_name = input("Enter bank name: ")
        statement_date = input("Enter statement date: ")
        bill_period = input("Enter bill period: ")
        days_to_pay = input("Enter days to pay: ")
        total = input("Enter the Credit Limit or the Total amount to pay to the company: ")

        with open("../DirectDebits.csv", "a") as file:
            file.write(f"{name},{amount},{date},{bank_name},{statement_date},{bill_period},{days_to_pay},{total}\n")
            print("Direct debit added")

    elif choice == "2":

        for name, amount in DDs.items():
            print(f"{name}: {amount}")

    elif choice == "3":

        with open("../DirectDebits.csv", "r") as file:
            print(file.read())
            
    elif choice == "4":

        print("Goodbye!")  
        print()      
        break