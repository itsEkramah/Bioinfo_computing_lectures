#easy mode questions for warmup 

# x = 15
# y = 4
# print(x / y)
# print(x // y)
# print(x % y)
# print(y ** 3)

# ##3,75 
# ##3
# ##3
# ##16

# a = 10
# b = 20
# print((a > 5) and (b < 30))  
# print((a == 10) or (b == 10)) 
# print(not (a > b)) 

# ##TRUE
# ##TRUE
# ##TRUE


# ###PRACTICE SOME MORE QUESTIONS ON TRUE AND FALSE 

# val1 = "25"
# val2 = "50"
# val3 = 100

# print(val1 + val2)
# print(int(val1) + int(val2))
# print(str(val3) + val1)

# ##2550
# ##75
# ##10025

# # Code with error:
# # age = 22
# # print("Your age is: " + age)

# ##type error
# age=22
# print("your age is:",age)


# # Code with error:
# # dna_sequence = "ATGC"
# # dna_sequence = "CGTA"
# # print(dna-sequence)
# ##name error no variable named dna-sequence
# dna_seq="ATGC"
# dna_seq="CGTA"
# print(dna_seq)


# # Code with error:

# num_str = input("Enter a number: ")

# num_int = int(num_str)

# print(num_int * 2)     
# ##no error its correct code

# Code:
# val1 = input("Enter first number: ")
# val2 = input("Enter second number: ")
# total = int(val1) + int(val2)
# print("The sum is:", total)

# Expected Output (assuming user enters 10 and 20):
# Enter first number: 10
# Enter second number: 20
# The sum is: 30


# # Code:
# obtained_marks = 1200
# total_marks = 1500
# percentage = (obtained_marks / total_marks) * 100
# print(f"Percentage: {percentage}%")

# # Expected Output:
# # Percentage: 80.0%


# Q9: Scenario-Based Code Writing
# Write a complete Python script for the following scenario:

# "Ask a user for their age. If their age is 18 or older, print 'Eligible to vote'. If it is less than 18, print 'Not eligible to vote'."

# Q10: Scenario-Based Code Writing
# Write a complete Python script for the following scenario:

# "Ask a user to input a total number of seconds (e.g., 150). Your program must calculate and print the number of full minutes and the remaining seconds. For example, 150 seconds is 2 minutes and 30 seconds."
# age=int(input("enter your age :"))
# if age >= 18:
#     print("you are eligible to vote")
# else :
#     print("you are not eligible to vote")

# seconds=int(input("enter total number of seconds "))   
# minutes=seconds/60 
# remaining_seconds=seconds%60
# print(minutes ,"minutes" , remaining_seconds)

#warmup end here now topic by topic questions start from here









### TOPIC 1: PYTHON BASICS
# 1. Variables & Data Types

# Variables containors hoty hain  jo store krty values inside memory.
# ve don’t need to declare their type; Python infers it automatically.

# Example
#x = 10        # integer
# y = 2.5       # float
# name = "Ali"  # string

# You can check their types:

# print(type(x))   # <class 'int'>
# print(type(y))   # <class 'float'>

###"25" + 5 ❌ causes TypeError because you can’t add string + int.

# ###Input and Output
# name= input("enter name")
# print("hello" , name)

### input() — Always returns a string

"""5. Operators
Arithmetic Operators
Operator	Meaning	Example
+	Addition	3 + 5 → 8
-	Subtraction	10 - 4 → 6
*	Multiplication	2 * 3 → 6
/	Division (float)	15 / 4 → 3.75
//	Floor division	15 // 4 → 3
%	Modulus (remainder)	18 % 4 → 2
**	Exponentiation	4 ** 3 → 64   exponentiation operator raises the number to the power of another number."""

# Comparison Operators

# Return True or False
# a=10
# b=20
# print(a>b)  
# print(a==10)

# Logical Operators

# Used to combine conditions:
# a=10
# b=20
# print(a<15 or b>19)
# print(a<15 and b>25)
# print(not(a>b))


# Comments and Indentation

# Comments: # single line or triple quotes for multi-line.

# Indentation defines blocks (4 spaces typical).

# if True:
#     print("Inside block")  # Indented → inside block
# print("Outside block")     # Not indented → outside block

##always be careful about scope and indentation

# Quick Summary

# All inputs are strings → convert using int() or float() when needed.

# Learn to “dry run” arithmetic + logical operator code.

# Indentation and type mismatches cause most beginner errors.

# print() can combine text and variables with commas or f-strings.

# PRACTICE SET 1 — PYTHON BASICS (Exam Simulation)
# 🧩 SECTION 1: OUTPUT PREDICTION (15 Questions)

##1.
# x = 25
# y = 4
# print(x / y)
# print(x // y)
# print(x % y)
# print(y ** 3)


# 6.25 
# 6
# 1
# 64

# ##2.
# a, b, c = 5, 10, 15
# a = b + c
# b = a - c
# c = a + b
# print(a, b, c)

# # a=25 , b =10 , c35  


# ###3
# text = "BioPython"
# print(text[0:3] + text[-3:])

# slicing main 2 type ki indexing hoti hay positive aur negetive[0:3] iss main start 0 index B se ho ga but end 2 index o pr ho jaay ga q k end 3 exclusive hay so 1st part se BIO print ho ga
##slicing k 2nd part main -3 negetive slicing ho rhi jis main hon include ho ga  so total + operater k stah biohon bann jaay ga

#Biohon

# # 4.
# num = 7
# num += 3
# num //= 2
# num **= 2
# print(num)

##25


# ##5.
# a = 10
# b = 20
# print((a > 5) and (b < 30))
# print((a == 10) or (b == 10))
# print(not (a > b))
# ## true true true

# ##6.
# val1 = "25"
# val2 = "50"
# val3 = 100
# print(val1 + val2)
# print(int(val1) + int(val2))
# print(str(val3) + val1)

##2550   ,   75   , 10025

#q.7
# ####in these type of questions always give first priority to bracket bracket , exponent  ,all type of compraision operators then  not  then and in laast or 
# ##must keep in mind this order 
# print("Result:", 10 > 5 and not 3 > 8 or 4 == 4)
# ##true and    not false or true  = true and rue or true = true 

# print( 5 < 3 or 10 == 10 and 1 != 2 )       
# ##false or true and true  = false or true = true 


# print( (5 < 3 or 10 == 10) and (1 != 2 and 4 < 2) )
# ##(false or true) and (true and false)  = true and false = false

# print( not 7 > 2 or ( 10 == 5 and not 3 == 3 ) )
# ####not true or (false and not true ) = not true or (false and false ) =false or false =false


##q.8
# a = 10
# b = a * 2
# c = b / 5
# print(int(c) + b)

##24

# q.9

# dna = "ATGCGC"
# gc = dna.count("G") + dna.count("C")
# print(gc / len(dna) * 100)

# #66.67

# #q.10
# x = 2
# y = 3
# z = x ** y + y ** x
# print(z)

# #17

# #q.11
# print("5" + "5" * 2)
# ##BODMAS    multiply then addition as "5" + "5" is string  it replicate not multiply with  3 so it make "5" + "55"  so in result it will become 555 


# # q.12
# print("Result:", 10//3 + 10%3)

# # #4
# a, b = 2, 5
# a = a + b
# b = a - b
# a = a - b
# print(a, b)
# #5 2

# num = 8
# print(num > 5 and num < 10 or num == 12)
# # true and true or false = true or false = true

# #q.15
# a = 2
# b = 3
# a = a * (b + a)
# print(a)
# # a= 10

#error detection 


####ERROR HANDLING BASICS IN PYTHON

# Syntax Error
# NameError(You try to use a variable or function name that hasn’t been defined yet.)
# TypeError   You try to use incompatible data types together (e.g., adding int + str).
# ValueError You convert a valid type but with an invalid value inside it.
# ZeroDivisionError  You divide by zero — Python can’t handle that.
# IndentationError Python uses indentation instead of braces to define code blocks.  Missing or inconsistent indentation triggers this error.
# IndexError  You try to access a list/string index that doesn’t exist.
# KeyError  You try to access a dictionary key that isn’t present.
# AttributeError You try to use a method or attribute that doesn’t exist for that type.

##16
# x = "10"
# y = 5
# print(x + y)

# # #type error 
# x= "10"
# y = 5
# print(int(x) + y)

##17

# if 5 > 2
#     print("Five is greater")
##syntax error : is missing 

# if 5 > 2 :
#     print("Five is greater")
    
##18
# for i in range(5):
#     print(i)

##syntax error : missing  + indentation error
    
# val = int("twenty")
# print(val)


##19 
# a = 10
# b = 0
# print(a / b)

##zerodividion error 

# ##20 
# age = 22
# print("Your age is: " + age)
##type error 
# age = 22
# print("Your age is: " , age)

##21
# dna-sequence = "ATGC"
# print(dna-sequence)
# name error dna-sequence cant be a variable
# dna_sequence = "ATGC"
# print(dna_sequence)

# ##22
# val = int("twenty")
# print(val)
###value error 
# val = int("20")
# print(val)

# ##23
# if True:
#     print("Bioinformatics")
# indentation error

##24
# name = "Ali"
# print(Name)
#name error no variable named  name not  Name 

# ###25
# number = 10
# if number % 2 = 0:
#     print("Even")

# # syntax errrror it should be ==

# number = 10
# # if number % 2 == 0:
# #     print("Even")

# ##26
# # print("Hello" + 5)
# # type error only same types can be added 
# # print("Hello" + "5")


# ######expected output and complete code 

##27
# val1 = "10"
# val2 = "20"
# #Fill in missing line
# total = int(val1)+int(val2)
# print("Sum:", total)

# ##output should be Sum: 30

# #28
# word1 = "Bio"
# word2 = "informatics"
# # 🔹 Write a line to print both words joined together
# print(word1 + word2)

# 10 20 30   # 🔹 Write a line to unpack tuple (10, 20, 30) into variables a, b, c
# # 🔹 Then print all three variables in one line

# a, b , c = (10 , 20  , 30 )
# print(a, b , c)



# 🟡 Q31

# Expected Output:

# GC Percentage: 66.6


# # Code:

# dna = "ATGCGC"
# # # 🔹 Calculate GC percentage and store in gc_percent
# # # 🔹 Print it as shown in expected output (rounded to 1 decimal)
# # # 🔹 Calculate GC percentage and store in gc_percent
# gc_percent= (dna.count("G") + dna.count("C") ) / len(dna)*100
# print("GC Percentage : " , gc_percent)


##q.33
# a = "Python"
# b = "Basics"
# # 🔹 Join both words with a space and print
# print(a + "" + b)

# ##q.34

num = 5
# 🔹 Write a while loop to print numbers from 5 down to 3
while num >= 5: 
    print(num)
num-=1