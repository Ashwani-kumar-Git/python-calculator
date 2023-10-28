print("\n----------------CALCULATOR----------------\n")

n1 = float(input("Enter First Number\n"))
n2 = float(input("Enter Second Number\n"))

print("""
Enter 1 for addition 
Enter 2 for subtraction
Enter 3 for multiplication
Enter 4 for division""")

choice = int(input("enter a number between 1-4: "))

if choice == 1:
    sum = n1+n2
    print ("the addition of the given two numbers is\n",sum)
elif choice == 2:
    print ("The subtraction of the given two numbers is\n",n1-n2)
elif choice == 3:
    print ("The multiplication of the given two numbers is\n",n1*n2)
elif choice == 4:
    print ("The division of the given two numbers is\n",n1/n2)
else:
    print ("Invalid Input from the User")

