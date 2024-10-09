#aurhor:chris
#date:08/10/24
#workbook q1/5 onenote
#task1
name = input("enter your name:")

if len(name) <7:
    print("hello (name)! your name is short!")
elif 7 <= len(name) <= 10:
    print("hello (name)! your name is long!")
else:
    print("hello (name)! your name is very long!")
    
#task2
def menu():
    print("Menu")
    print("1. Music")
    print("2. History")
    print("3. Science and Technology")
    print("4. Exit")
menu()
choice = input("Please enter your choice: ")
if choice == "1":
    print("You chose Music.")
elif choice == "2":
    print("You chose History.")
elif choice == "3":
    print("You chose Science and Technology.")
elif choice == "4":
    print("Exiting... Goodbye!")
else:
    print("Invalid choice.")

#task3
import random
def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print("You rolled (dice1) and (dice2)")
    if dice1 == dice2:
        print("You rolled a double! Your score is (2 * (dice1 + dice2))")
    else:
        print("Your score is (dice1 + dice2)")
roll_dice()
    
#task4
amount = float(input("Enter the total amount spent: "))
if amount >= 200:
    discount = 0.10
elif 100 <= amount < 200:
    discount = 0.05
else:
    discount = 0.0
discount_amount = amount * discount
final_amount = amount - discount_amount
print("Discount given: $(discount_amount:.2f)")
print("Final amount owed: $(final_amount:.2f)")
    
    
    
    
    
    
    
    