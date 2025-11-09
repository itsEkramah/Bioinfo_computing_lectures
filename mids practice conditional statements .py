# # CONDITIONAL STATEMENTS
# # 🩵 1️⃣ The if, elif, else Structure

# # Conditional statements help your program make decisions based on conditions (True/False). Nested if Statements

# # You can put an if inside another if.
# # Used when decisions depend on multiple layers of logic.

# # 🔹 Example
# # age = 20
# # citizen = True

# # if age >= 18:
# #     if citizen:
# #         print("Eligible to vote")
# #     else:
# #         print("Not eligible - not a citizen")
# # else:
# #     print("Not eligible - underage")


# # marks=int(input("enter marks:"))
# # if marks >=80 :
# #     print(" your grade is A")
# # elif marks>=60:
# #     print ("ur grade is B")
# # elif marks>=50:
# #     print(" your grade is C")
# # else:
# #     print("you are fail")


# """Nested if Statements

# You can put an if inside another if.
# Used when decisions depend on multiple layers of logic."""


# # SECTION 1 — OUTPUT PREDICTION (10 Questions)

# # Predict the exact output after dry-running the code mentally.

# # 1.
# age = 20
# if age >= 18:
#     print("Eligible")
# else:
#     print("Not Eligible")
# ##Eligible

# ##2
# marks = 82
# if marks >= 90:
#     print("A+")
# elif marks >= 80:
#     print("A")
# else:
#     print("Fail")
# #A+



# x = 5
# if x > 10:
#     print("Big")
# elif x == 5:
#     print("Equal")
# else:
#     print("Small")
# ##Equal


# a = 10
# b = 5
# if a > b and b > 2:
#     print("Valid")
# ##Valid



# temp = 25
# humidity = 70
# if temp > 20 and humidity < 80:
#     print("Weather is good")
# else:
#     print("Weather is bad")
# # Weather is good



# num = 12
# if num % 2 == 0:
#     print("Even")
#     if num % 3 == 0:
#         print("Divisible by 3")
# else:
#     print("Odd")
# ##Even


# x = 10
# if x > 5:
#     if x < 15:
#         print("In range")
#     else:
#         print("Out of range")
# #in range


# a, b = 15, 25
# if not a > b:
#     print("True branch")
# else:
#     print("False branch")
# ##  False Branch


# marks = 65
# if marks >= 80:
#     print("Distinction")
# elif marks >= 60:
#     print("Pass")
# else:
#     print("Fail")

# ##Pass


# x = 7
# if x % 2 == 0:
#     print("Even")
# else:
#     if x > 5:
#         print("Odd and greater than 5")
#     else:
#         print("Odd and small")

# # odd and greater than 5





# SECTION 2 — ERROR DETECTION & CORRECTION (10 Questions)

# Identify the error type (SyntaxError, IndentationError, etc.) and write the corrected code.
#11

# if 10 > 5
#     print("Yes")
# # ## syntex error : missing
# if 10 > 5:
#     print("Yes")


# ##12
# if age >= 18
# print("Adult")

##syntax error missing : and indentation error print should be after  tabspace 
# if age >= 18:
#     print("Adult")


# marks = 90
# if marks = 90:
#     print("Excellent")
# ##syntax error == 


# marks = 90
# if marks == 90:
#     print("Excellent")

# if True
#     print("Always true")
# ##syntax error : missing 

# if True:
#     print("Always true")


# x = 10
# if x > 5:
# print("Greater")
##indentation error 
# x = 10
# if x > 5:
#     print("Greater")


# score = 85
# if score > 80
#     print("A")
# else
#     print("Fail")

##syntax error : missing

# score = 85
# if score > 80:
#     print("A")
# else:
#     print("Fail")


# if a > 10 or b < 5:
#     print("Condition met")

# IMPORTANT NAME ERROR name a Is not defined 
# a=11
# b=6
# if a > 10 or b < 5:
#     print("Condition met")


# if not True:
# print("False branch")

# # indentation error 
# if not True:
#     print("False branch")


# if x > 5 and y < 10:
#     print("OK")
# else
#     print("Not OK")
# ##SYNTAX ERROR :
# ###NAME NOT DEFINED  X AND Y 

# x=6
# y=11
# if x > 5 and y < 10:
#     print("OK")
# else:
#     print("Not OK")





# if 5 > 10:
#     print("A")
# elif 10 < 5:
#     print("B")
# else
# print("C")


# if 5 > 10:
#     print("A")
# elif 10 < 5:
#     print("B")
# else:
#     print("C")

##syntax error : missing
##indentation error tab space befor last print statement



# SECTION 3 — CODE COMPLETION (10 Questions)

# Fill in the missing line(s) to make the output exactly as shown.

# 21.

# Expected Output:  You are eligible to vote
# age = 19
# # 🔹 Complete the if condition
# if age>=18:
#     print("You are eligible to vote")



# 22.

# # Expected Output:  Fail
# marks = 45
# # 🔹 Write if–else structure to print "Pass" if marks >= 50 else "Fail"
# if marks >= 50:
#     print("pass")
# else:
#     print("Fail")


# 23.

# Expected Output: Positive

# num = 5
# # 🔹 Check if number is > 0 and print "Positive"
# if num>0 :
#     print ("positive")
# else:
#     print("negetive")

# 24.

# # Expected Output:   Even number
# x = 10
# # 🔹 Write condition using % operator to print "Even number"
# # if x %2 == 0 :
# #     print(" Even Number ")
# # else:
# #     print("odd number")


# # # 25.

# # # Expected Output:Number is in range


# # x = 8
# # # 🔹 Write condition: number between 5 and 10 inclusive
# # if x in range(5, 11 ):
# #     print("number is in range")
# # else: 
# #     print("num out of range")


# # 26.

# # Expected Output:Fail
# marks = 38
# # 🔹 Use if–elif–else structure for grading:
# # 50–59: Pass, 60–79: Good, 80+: Excellent
# if marks>=80:
#     print ("excelent")
# elif marks >=60 and marks < 80 :
#     print("good")
# elif marks >= 50 and marks <60 :
#     print("pass")
# else:
#     print("fail")


# # 27.

# # Expected Output:  Odd number and greater than 5

# num = 7
# # 🔹 Combine two conditions with 'and' and print message
# if num > 5 and num %2 == 0:
#     print("num is greater than five and even ")
# else:
#     print("num is greater than five and odd ")
    


# 28.

# Expected Output:x is 10
# x = 10
# # 🔹 Use if–else block to print "x is 10" only if condition true
# if x==10 :
#     print (x is 10)
# else :
#     print("x is not equal to 10 ")




# SECTION 4 — SCENARIO-BASED CODING (3 Questions)

# Write complete Python programs as per given description.

# ##31.

# # Scenario:
# # Write a program that takes marks from the user and prints the grade as:


# marks= int(input("enter marks :"))
# if marks>=80:
#     print ("excelent")
# elif marks >=60 and marks < 80 :
#     print("good")
# elif marks >= 50 and marks <60 :
#     print("pass")
# else:
#     print("fail")


# 32.

# Scenario:
# Ask the user for their age and nationality.
# If age >= 18 and nationality == "Pakistani", print "Eligible to vote", otherwise "Not eligible".


# age=int(input("enter your age"))
# nationality=input("enter nationality :")

# if age>=18 and nationality == "pakistani" :
#     print("you are eligible to vote ") 
# else :
#     print(" you are not eligible to vote ")



# 33.

# Scenario:
# Write a program that checks if a number is divisible by both 3 and 5.
# If yes → print "FizzBuzz", if only 3 → "Fizz", if only 5 → "Buzz", otherwise "Not divisible".


# num= int(input("enter number:"))
# if num % 3 ==0 and num % 5 == 0:
#     print("FizzBuzz")
# elif num % 3 == 0 :
#     print("Fizz")
# elif num % 5 == 0:
#     print("BUzz")
# else :
#     print("not divisible by 3 or 5 ")


