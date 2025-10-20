# def calc_sum(a,b):
#     return a + b

# sum =  calc_sum(3,5)
# print(sum)

# ##print length of list
# list1=["islamabad","lahore","karachi"]
# list2=["ironman","spiderman","hulk"]

# def print_length(list):
#     return len(list)

# print(print_length(list1))
# print(print_length(list2))



# ##print elements of list in single line

# list1=["islamabad","lahore","karachi"]

# def print_elements(list1):
#     for x in list1:
#         print(x , end=" ")
# print_elements(list1)



# ##write fun to calculate factorial of n
# n=int(input("enter a number:"))
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# print(factorial(n))

# def percentage(marks_obtained, total_marks):
#     """Calculate percentage = (marks / total) * 100"""
#     return (int(marks_obtained) / int(total_marks)) * 100


# num_students = int(input("Enter number of students in class: "))

# percentages = []

# for _ in range(num_students):
#     marks = input("Input Marks Obtained: ")
#     total = input("Input Total Marks: ")

#     perc = percentage(marks, total)
#     print("Percentage:", perc)
#     percentages.append(perc)

# average = sum(percentages) / num_students
# print("The average percentage of class is", average)

# ##
# def show (n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1) 
    
    
    
    
##BASIC FUN SYNTAX
#WRITE A FUN TO CALCULATE AND RETURN THE SQ OF A NUMBER

# def square(num):
#     print(num ** 2)
# square(5)
    

# def square(num):
#     print(num ** 2)
# result= square(6)
# print(result) #it print none because it print directly 1st print statement     print(num ** 2)

# def square(num):
#     return num ** 2
# result= square(7)
# print(result)



###fun with multiple perameters
###create a fun that takes 2 num as parameter and return their products
# def product(num1 , num2):
#     return num1*num2
# print(product(5 , 7))

##polymorphism in functions
##write a fuun that multiply that multiples two numbers but can also accept and multiply strings

# def multiple(p1 , p2):
#     return p1 * p2

# print(multiple('a' , 5))
# print(multiple(6 , 5))
# print(multiple('a' , 7))


# ##fun return multiple values  area and circumference of circle given its radious
# import math
# def circle(radius):
#     area= math.pi * radius ** 2
#     circumference= 2* math.pi *radius
#     return area , circumference
# a,c = circle(3)
# print("area:" , a, "circumference:" , c )
    
    
###default  parameter
