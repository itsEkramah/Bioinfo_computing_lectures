# Topic 4: Functions in Python
# 🎯 Learning Goals

# By the end of this topic, you should be able to:

# Define and call functions

# Use parameters, arguments, and return values

# Understand default, keyword, and arbitrary arguments

# Return multiple values

# Write recursive functions

# Recognize common function-based exam errors

# Apply functions in mini bioinformatics use-cases (GC%, translation, etc.)

# 🧠 1️⃣ Function Basics

# Functions let you organize code into reusable blocks.

# 🔹 Syntax:
# def function_name(parameters):
#     # function body
#     return value


# def greet():
#     print("Hello, Bioinformatician!")

# greet()


# """Parameters vs. Arguments
# Term	Meaning	Example
# Parameter	Variable in function definition	def add(a, b):
# Argument	Actual value passed when calling	add(2, 3)"""

# def add(a, b):
#     return a + b

# print(add(5, 3))


# """Return Statement

# The return keyword sends back a value to the caller."""

# def multiply(x, y):
#     result = x * y
#     return result

# ans = multiply(4, 3)
# print(ans)


# Default Arguments

# When a parameter has a default value.


# def greet(name="Student"):
#     print(f"Hello, {name}!")

# greet("Ekramah")
# greet()


# Keyword Arguments

# You can specify arguments by name.


# def info(name, age):
#     print(f"{name} is {age} years old")

# info(age=21, name="Ali")

# """Returning Multiple Values"""

# def calc(a, b):
#     return a+b, a-b, a*b

# x, y, z = calc(5, 2)
# print(x, y, z)


# """Recursion (Function Calling Itself)

# Used for repetitive tasks that can be broken into sub-problems."""

# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n-1)

# print(factorial(5))



# # GC Content Function

# def gc_content(dna):
#     gc=0
#     for i in dna:
#         if i in ['G' , 'C']:
#             gc += 1
#     return gc / len(dna) *100
# print(gc_content("ATCGCGCGCGCTGTCTCTCTACACAACACGCGCGCTGTATATAG") )







# # SECTION 1 — OUTPUT PREDICTION (10 Questions)

# # Predict the exact output by mentally dry-running the code.


# def greet():
#     print("Hello")
# greet()
# ##Hello

# def add(a, b):
#     return a + b
# print(add(2, 3))
# ##5

# def bio():
#     x = "DNA"
#     return x
# print(bio())
# ##DNA

# def square(n):
#     return n * n
# print(square(3) + square(2))
# ##9+4 =13

# def outer():
#     x = 5
#     def inner():
#         return x + 2
#     return inner()
# print(outer())
# ##7  OUT CALLED BUT RETURENED INNER FUNCTION 

# def f(x, y=3):
#     return x * y
# print(f(4))
# ##12


# def f(a, b):
#     return a if a > b else b
# print(f(10, 20))
# ##20

# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
# print(factorial(4))
# ## 4*3=12*2=24*1+24



# def test(n):
#     if n == 0:
#         return 0
#     else:
#         return n + test(n - 1)
# print(test(4))
# ### 4+3=7+2=9+1=10

# def add(x):
#     def double(y):
#         return y * 2
#     return double(x) + x
# print(add(5))

# ###DRY RUN  X= 5 RETURN DOUBLE(X=5) +X def double(y):the parameter y is just a placeholder.


# # When add(5) runs, it sets x = 5.
# # Inside add, you call double(x). This means you are calling double(5).
# # Now y is set to 5 in this function call.

# # SO 

# #     double(5) returns 5 * 2 = 10.
# #     So this becomes 10 + 5.
# # add(x) now returns 15.





# SECTION 2 — ERROR DETECTION & CORRECTION (10 Questions)

# Identify the error type and provide corrected code.

# def greet()
#     print("Hello")
# ##syntax error : missing and logical error not ckalled function greet()
# def greet():
#     print("Hello")
# greet()

# def sum(a, b)
# return a + b
##syntax error missing: 
##indentation error for return statement 
##not function aclling or print 

# def sum(a, b):
#     return a + b
# print(sum(2 , 4))



# def f(a, b):
# print(a + b)
# indentation error for print statement 
# not calling funtion
# def f(a, b):
#     print(a + b)
# f(1 ,3)


# def func(x, y):
#     return x + y
# print(func(5))
##type error missing aurgument for y 
# def func(x, y):
#     return x + y
# print(func(5 , 6))


# def bio_data(name, age):
#     print("Name:", name, "Age:", age)
# bio_data("Ali", )

# type error missing aurgument for age
# def bio_data(name, age):
#     print("Name:", name, "Age:", age)
# bio_data("Ali", 23 )



# def add(a, b, c=2, d):
#     return a + b + c + d
# ###syntax error   as in Python, all parameters with default values must come after any parameters without defaults.

# def add(a, b, d, c=2):
#     return a + b + d +c 
# print(add(1,2,3))

# def fun(x, y):
#     print(result)
#     result = x + y
# fun(3, 4)
##cant acess variable result it print result first and calculate after
# def fun(x, y):
#     result = x + y
#     print(result)
# fun(3, 4)


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n)
# print(factorial(4))
###recursionerrorld be n-1 instead of factorial (n)
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(4))



# def calc(a, b):
#     return a + b
# print(calc(a=2, 3))

# # syntax error keyword come befor potential aurgument
# print(calc(2, 3))         # positional only
# print(calc(a=2, b=3))     # keyword only
# print(calc(2, b=3))       # mix: positional, then keyword
# # In function calls, "keywords come last


# def calc(a, b):
#     return a + b
# print(calc(a=2,b=3))



# def f(x, y):
#     return x + y
# f(x=2, x=3)
##syntax error aurgumentynot passed key aurgument x repeated

# def f(x, y):
#     return x + y
# print (f(x=2, y=3))


# SECTION 3 — CODE COMPLETION (10 Questions)

# Expected Output:Hello, Ekramah
# 🔹 Define a function greet(name) that prints "Hello, <name>"
# 🔹 Call the function with your name

# def greet (name):
#     print("Hello, ",name )
# greet("Ekramah")

# Expected Output: 25
# 🔹 Write function square(n) that returns n squared and call it with 5

# def square(n):
#     return n ** 2
# print(square(5))

# Expected Output:A+ grade
# 🔹 Define function grade(marks) → if marks>=90 print("A+ grade")
# otherwise print("Other")

# def grade(marks):
#     if marks >= 90 :
#         print("A+ Grade")
#     else :
#         print("other")
# grade(92)


# Expected Output: 10
# 🔹 Define add(a,b) → return their sum
# 🔹 Call it with 4,6 and print result


# def sum(a , b) :
#     return a+ b
# print(sum(4,6))



# # Expected Output: DNA: 3 # 🔹 Define count_dna(seq, base) that counts a base in given DNA string
# def count_dna(dna_seq, base):
#     count = dna_seq.count(base)
#     print("DNA:", count)
#     return count
# # Example usage:
# count_dna("ATGCAAGCGT", "A")


# def count_dna(dnaseq , base ):
#     count=dnaseq.count(base)
#     print("DNA: " , count )
#     return count
# count_dna("ATCGCGCGCGCATA" , "A")




# Expected Output: 1 4 9 16 25
# # 🔹 Write function squares_up_to(n) → prints all squares from 1^2 to n^2
# def squares_up_to(n):
#     for i in range (1 , n+1):
#         print(i**2 , end=" ")
# squares_up_to(5)

# Expected Output: Sum = 15
# # 🔹 Define sum_to_n(n) → use loop to sum 1 to n, then return total

# def sum_to_n (n):
#     total_sum=0
#     for i in range (1 , n+1):
#         total_sum += i
#     print("Sum:" ,total_sum )
# sum_to_n(5)


# Expected Output:8
# 🔹 Define a function power(base, exp) that returns base ** exp
# 🔹 Call with 2, 3

# def power(base , exponent):
#     return base ** exponent 
# print(power(2 , 3))

Expected Output: Factorial = 120
# 🔹 Define recursive function factorial(n) that returns factorial of n
# 🔹 Print result for n=5


def factorial (n):
    if n == 0 or n ==1 :
        return 1
    else:
        return n * factorial
result = factorial(5)
print(f"factorial of {n} is: {result }")