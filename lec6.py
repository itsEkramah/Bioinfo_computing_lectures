# #functions
# #resuable block of code that perform a specific task
# #DRY- DONT REPEAT YOURSELF
# #syntax
# # def function_name(parameters):
# #     #function body
# #     #return statement         
# #function call
# # function_name(arguments)
# #arguments- actual value passed to function
# #parameters- variable in the function defination that recieves the value passed
# #return statement- used to exit a function and go back to the place where it was called


# # def function_1():
# #     print("this ia oue first function")
    
# # # function_1()
# # # function_1()
# # # function_1()
# # # function_1()
# # # function_1()

# # def function_2(name="adnan"):
# #     print("this ia oue first function" , "I am ", name,)
# # function_2("ekramah")
# # function_2("ali")
# # function_2()


# # def function_3(fname = "adnan", lname = "ansari"):
# #     print("this ia oue first function" , "I am ", fname, lname)
# # function_3( "ekramah" , "chaudhary")

# def function_3(fname = "adnan", lname = "ansari"):
#     print("this ia oue first function" , "I am ", fname, lname)
# function_3(lname = "ekramah" ,fname= "chaudhary")
# function_3()

# #function ask user kid names ## unknown no of arguments
# def function_4(*kids): ## * is use to pass unknown no of arguments
#     function_4("ekramah" , "ali" , "umer" , "s")
#     print(kids)
#     for i in kids :
#         print(i)
#     print(kids[-1])

# y = len(kids)
# print(kids[y-1])  ##length use index to print last element if we dont use y-1 it will be index out of range 

##user unlimited time input marks le ga  function ho ga perceentage ka terminate loop when i enter q

# def percentage(marks_obtained, total_marks=100):
#     return (int(marks_obtained) / int(total_marks)) * 100
# num_students = int(input("Enter number of students in class: "))
# percentages = []
# for _ in range(num_students):
#     marks = input("Input Marks Obtained: ")
#     total = input("Input Total Marks: ")

#     perc = percentage(marks, total)
#     x = percentage(marks)
#     if percentage(marks)>50:
#         print("pass")
#     else:
#         print("fail")
#     print("Percentage:", perc)
#     percentages.append(perc)
    
    
# def percentage (mo):
#     return (int(mo) / 30 * 100)
# while True:
#             mo = int(input("Input Marks Obtained: "))
#             if(mo>30):
#                 break
# x= percentage(mo)
# print("Percentage:", x)    
# if (x<50):
#     print("fail")
# elif (x>50 & x<80):
#     print("avg")
# elif (x>=80 & x<=100):
#     print("exelent")
                



# recursive function khud ko call krta
# def recursive_fun(k):
#     if(k>0):
#         result = k + recursive_fun(k-1)# if just added k it will staart infinite call  so we use k-1
#         print(result)
#     else:
#         result = 0
#     return result

# recursive_fun(4)


# Dry run for k=4:
# recursive_fun(4)
# 4 > 0: result = 4 + recursive_fun(3)
#   recursive_fun(3)
#   3 > 0: result = 3 + recursive_fun(2)
#     recursive_fun(2)
#     2 > 0: result = 2 + recursive_fun(1)
#       recursive_fun(1)
#       1 > 0: result = 1 + recursive_fun(0)
#         recursive_fun(0)
#         0 not > 0: result = 0
#       returns 0, so result = 1 + 0 = 1, print(1)
#     returns 1, so result = 2 + 1 = 3, print(3)
#   returns 3, so result = 3 + 3 = 6, print(6)
# returns 6, so result = 4 + 6 = 10, print(10)
#joo sub se pehle call ho ga wo last main print ho ga  q k uski execustion ki values depend on output of next call

# next class task --> practice functions and loops combine examples and different logics
# factorial code by using functions and by using loop both ways   try multiple different approaches
# factorial using recursive function

def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)

n = int(input("Enter a number to calculate its factorial: "))

result = calculate_factorial(n)
print(f"The factorial of {n} is {result}")

#example of function and loop 