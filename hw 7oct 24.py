#author:chris isaac
#date:07/10/24
#homework:tasks1/5

#task 1:
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num2 % num1 == 0:
    print("goodjob.")
else:
    print("try again.")
# Task 2: 
age = int(input("Enter your age: "))
if age >= 17:
    print("You are ready for an irish driving license.")
else:
    print("You are not ready for an irish driving license.")
#Task 3: 
cost = float(input("Enter the cost of the item: €"))
if cost > 10000:
    print("Go to tender.")
elif  500 <= cost <= 10000:
    print("Get quotes from three suppliers.")
else:
    print("Go ahead and order.")
#task 4
#Print introductory message
print("Welcome! You can win a free LUAS ticket for a weekend trip.")
print("Please choose a destination:")
print("A: Dundrum Shopping Centre")
print("B: Tallaght")
print("C: Broombridge")
#users input
choice = input("Enter A, B, or C: ")
if choice == 'A':
    print("Congratulations! You won a ticket to Dundrum Shopping Centre!")
elif choice == 'B':
    print("Congratulations! You won a ticket to Tallaght!")
elif choice == 'C':
    print("Congratulations! You won a ticket to Broombridge!")
else:
    print("Invalid entry. Please enter A, B, or C.")
    
    
    
#task 5
percentage = int(input("Enter your percentage as a whole number: "))
# Determine the grade based on percentage
if 90 <= percentage <= 100:
    print("Your grade is H1")
elif 80 <= percentage <= 89:
    print("Your grade is H2")
elif 70 <= percentage <= 79:
    print("Your grade is H3")
elif 60 <= percentage <= 69:
    print("Your grade is H4")
elif 50 <= percentage <= 59:
    print("Your grade is H5")
elif 40 <= percentage <= 49:
    print("Your grade is H6")
elif 30 <= percentage <= 39:
    print("Your grade is H7")
elif 0 <= percentage <= 29:
    print("Your grade is H8")
else:
    print("Invalid percentage. Please enter a number between 0 and 100.")




