# #1
# a=10
# b=3
# print(a//b)
# print(a%b)
# print(a**b)

# #2
# s="python"
# print(s[1:4])
# print(s[::-1])
# print(s[::2])

# #3
# nums=[1,2,3]
# num.append([4,5])
# print(num)
# num.extend([6,7])
# print(num)

# #5
# def mystery(a, b=2):
#     return a**b
# print(mystery(3))
# print(mystery(2,3))


# #6
# nums=[1,2,3,4,5,6]
# square=[n**2 for n in nums if n%2==0]
# print(square)

# #7
# for i in range(1,4):
#     for j in range(i):
#         print(i+j, end=" ")

# #8
# def greet(name, msg="hello"):
#     porint(msg,name)
# print("alice")


# #9
# word = "banana"
# result = ""
# for ch in word:
#     if ch not in result:
#         result+=ch
#     print(result)

# #10
# scores={"ali":85, "sara":90, "john":75}
# total=0
# for name,score in scores.item():
#     score+=total
# print(average, total/len(score))

# #11
# def add_item(itwem,lst=[]):
#     lst.append(itwem)
#     return lst
# print(add_item(1))
# print(add_item(2))


# # common errors
# for i in range(5): "syntax error"

# for i in range(5):
#     # Code to run in the loop goes here
#     print(i)




# x=10
# print(y) # NameError: name 'y' is not defined

# x=10
# print(x)




# a="5"
# b=2
# print(a+b) # TypeError: can only concatenate str (not "int") to str

# a="5"
# b=2
# print(int(a) + b)  # Output: 7


# # or

# a="5"
# b=2
# print(a + str(b))  # Output: 52




# data={"name":"ali", "age":22}
# print(data["city"]) # KeyError: 'city'

# data={"name":"ali", "age":22}
# print(data["name"])  # Output: ali

# data={"name":"ali", "age":22}
# print(data.get("city", "lahore"))  # Output: lahore




# x=10/0
# print(x) # ZeroDivisionError: division by zero

# x=10
# print(x/2)  # Output: 5.0


# a = 10
# b = 0
# if b != 0:
#     print(a / b)
# else:
#     print("Error: Cannot divide by zero.")

# a=10
# b="5"
# try:
#     result=a+b
# except TypeError:
#     print("Error: Cannot add different data types.")

# a=10
# b=0
# try:
#     result=a/b
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")



# def greet():
# print("hello")#identation error

# def greet():
#     print("hello")


# def add(a,b):
#     return a+b
# print(add(2)) #missing argument error

# def add(a,b):
#     return a+b
# print(add(2,3))  # Output: 5


# num=int("abc")
# print(num) #value error

# num=int("123")
# print(num)  # Output: 123





# # #20
# n=7
# a,b=0,1
# for _ in range(n):
#     print(a,end=" ")
#     a,b=b,a+b



# # 21
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(5))

# # 22
# text = "python"
# rev = text[::-1]
# print(rev)

# # 23
# word = "madam"
# if word == word[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")

# 24
num = 1234
total = 0
while num > 0:
    digit = num % 10
    total += digit
    num = num // 10
print(total)