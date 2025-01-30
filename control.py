#control statements : control flow of execution of a code
#control statements there are two types like for loop and while loop
"""
A for loop in Python is used to iterate over a sequence (such as a list, tuple, string, or range).
syntax:
      for variable i in rangeO(start, end, step):
            statements

"""

#print("Pushpa The Rise")
#print("Pushpa The rule")

num = 0
if num == 1:
    print("Pushpa The Rise")
else:
    print("Pushpa The rule")
    print("1500 cr") 

print("end ended")
print("\n\n")
"""
Indentation in Python is the use of spaces or tabs at the beginning of a line of code. It's a fundamental part of Python syntax and is used to indicate a block of code. 

Decision Making Statements:Decision-making statements in Python are also known as conditional statements.
if - statement
if-else -statement
if-elif-else -stetement

"""
#to print a positive or negative or zero
num = int(input("enter the number"))
if num == 0:
    print("Zero")
elif num > 0:
    print("positive")
else:
    print("Negative")

print("\n\n")


# To print a biggest of three numbers
n1 = 10
n2 = 20
n3 = 50
if n1>n2 and n1>n3:
    print("N1 is biggest number")
elif n2>n3:
    print("N2 is biggest number")
else:
    print("N3 is biggest number")
print("\n\n")

#curerent bill
#100 units - per unit 50 rupees
#101 - 200 units - per unit 100 rupees
# 201-300 units -per unit 150 rupees 
current_bill = int(input("Enter units : "))

if current_bill > 0 and current_bill <=100:
    print("per unit 50 rupees = ",current_bill*50)
else:
    if current_bill > 100 and current_bill <=200:
        print("per unit 100 rupees = ",current_bill*100)
    else:
        if current_bill > 200 and current_bill <=300:
            print("per unit 150 rupees = ",current_bill*150)
        else:
            print(current_bill*200)
print("\n\n")

#loops : a loop is a block of statements until the condition is fail then exit and print a block of statements
#for loop
for i in range(10):
    print("hello")
print("\n\n")

""" with range function we can use like start, end, step
    Syntax:
for variable in range(start,step,end):
    statements
"""
# natural numbers
n =int(input("Enter numbers = "))
for i in range(n):
    print(i, end=" ")
    #end=" " we can print a horizantal numbers
print("\n")

# without range 
name = "python"
for i in name:
    print(i)