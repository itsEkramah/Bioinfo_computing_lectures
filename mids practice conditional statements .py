# CONDITIONAL STATEMENTS
# 🩵 1️⃣ The if, elif, else Structure

# Conditional statements help your program make decisions based on conditions (True/False). Nested if Statements

# You can put an if inside another if.
# Used when decisions depend on multiple layers of logic.

# 🔹 Example
# age = 20
# citizen = True

# if age >= 18:
#     if citizen:
#         print("Eligible to vote")
#     else:
#         print("Not eligible - not a citizen")
# else:
#     print("Not eligible - underage")


# marks=int(input("enter marks:"))
# if marks >=80 :
#     print(" your grade is A")
# elif marks>=60:
#     print ("ur grade is B")
# elif marks>=50:
#     print(" your grade is C")
# else:
#     print("you are fail")


"""Nested if Statements

You can put an if inside another if.
Used when decisions depend on multiple layers of logic."""


# SECTION 1 — OUTPUT PREDICTION (10 Questions)

# Predict the exact output after dry-running the code mentally.

# 1.
age = 20
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
##Eligible

##2
marks = 82
if marks >= 90:
    print("A+")
elif marks >= 80:
    print("A")
else:
    print("Fail")
#A+



x = 5
if x > 10:
    print("Big")
elif x == 5:
    print("Equal")
else:
    print("Small")
##Equal


a = 10
b = 5
if a > b and b > 2:
    print("Valid")
##Valid



temp = 25
humidity = 70
if temp > 20 and humidity < 80:
    print("Weather is good")
else:
    print("Weather is bad")
# Weather is good



num = 12
if num % 2 == 0:
    print("Even")
    if num % 3 == 0:
        print("Divisible by 3")
else:
    print("Odd")
##Even


x = 10
if x > 5:
    if x < 15:
        print("In range")
    else:
        print("Out of range")
#3#in range