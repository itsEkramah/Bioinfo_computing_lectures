# """Topic 3: Loops in Python
# 🎯 Learning Goals

# By the end of this topic, you should confidently handle:

# for and while loops

# range() function

# break, continue, and pass

# Nested loops

# The while...else and for...else blocks

# Common loop-based logic (factorial, sum, reverse number, pattern printing, etc.)"""


# # for i in range(3):
# #     print( "Python" ,  end="  " )
# #     ###end" "  ka use krnay se same line main print hota warna  hrr row main 1 baar 


# # for i in range(2, 10, 3):
# #     print(i)

# # fruits = ["apple", "banana", "cherry"]
# # for fruit in fruits:
# #     print(fruit)
# # ###print  apple banana cherry in seperate rows 

# # i = 1
# # while i <= 5:
# #     print(i)
# #     # i =+ 1   infinite loop of printing 1
# #     i +=1     ##   print 1-5 in rows 


# # break

# # # Stops loop immediately.
# # for i in range(5):
# #     if i == 3:
# #         break
# #     print(i)
# # ## 0 1 2 print ho gaa seperate rows main hio
# # q k loop jese hi 3 k equalhoa brak ho gea aur 3 ki value i main aai hi nahii


# # continue

# # Skips current iteration and moves to next.
# # for i in range(5):
# #     if i == 2:
# #         continue
# #     print(i)


# # pass

# # # Does nothing (placeholder for future logic).
# # for i in range(3):
# #     pass


# # Nested Loops

# # A loop inside another loop.

# # # 🔹 Sum of all Numbers
# # sum=0
# # for i in range(1,6):
# #     sum += i
# #     print(sum)

# n=5
# factorial=1 
# for i in range(1 , n+1):
#     factorial  *= i
# print(factorial) ##PRINT STATEMENT OUTSIDE LOOP SCOPE SO ONLY PRINT LAST VALUE 120

# n=5
# factorial=1 
# for i in range(1 , n+1):
#     factorial  *= i
#     print(factorial) ##PRINT STATEMENT INSIDE LOOP SCOPE SO ALL  1, 2 , 6 , 24  120 WILL BE PRINTED

##REVERSE A NUMBER'
# num = 7643864343
# rev = 0
# while num > 0:
#     rev = rev * 10 + num % 10
#     num //= 10
# print(rev)



# # DNA Base Counting
# dna = "ATCGCTACG"

# count_G = 0
# for i in dna:
#     if i == "G":
#         count_G += 1
# print(f"Count of G is: {count_G}")

# count_A = 0
# for i in dna:
#     if i == "A":
#         count_A += 1
# print(f"Count of A is: {count_A}")

# count_C = 0
# for i in dna:
#     if i == "C":
#         count_C += 1
# print(f"Count of C iD: {count_C}")

# count_T = 0
# for i in dna:
#     if i == "T":
#         count_T += 1
# print(f"Count of T is: {count_T}")

# dna="ATCGCTTCGATC"
# count={"A" :0, "T" : 0 , "G" : 0 , "C" : 0}

# for i in dna:
#     count[i] +=1
# for i , value in count.items():
#     print(f"count of {i} :{ value}")




# dna= "ATCGCTAGCAATCGA"
# count= {"A": 0 , "T" : 0 , "C" : 0 , "G" : 0 }
# for i in dna:
#     count[i] += 1 
# for i , value in count.items():
#     print(f" count of base {i} : {value}")







# SECTION 1 — OUTPUT PREDICTION (10 Questions)

# Predict the exact output after dry-running the code mentally.



# for i in range(3):
#     print(i)
# # 0
# # 1
# # 2


# for i in range(1, 5):
#     print(i * 2, end=" ")

#   2  4  6  8


# x = 0
# for i in range(3):
#     x += i
# print(x)

# # range 0-2   0+0 =0 +1=1 +2   =3



# for ch in "ATGC":
#     if ch == "G":
#         break
#     print(ch, end="")
# # A T



# for i in range(2, 10, 3):
#     print(i, end=",")

# # 2  5  8 

# i = 1
# while i <= 5:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     i += 1

# # i=1   1 , 2 , 4  ,5

# dna = "ATGCG"
# count = 0
# for base in dna:
#     if base == "G":
#         count += 1
#     print(count)
# """
# 0
# 0
# 1
# 1
# 2"""

# dna = "ATGCG"
# count = 0
# for base in dna:
#     if base == "G":
#         count += 1
# print(count)
# #2


# for i in range(3):
#     for j in range(2):
#         print(i + j, end=" ")

# # i=0
# # j=0 

# # 0 + 0 =0
# # 0 + 1 =1 
# # 1 + 0 =1
# # 1 + 1 =2
# # 2 + 0 =2
# # 2 + 1 =3

# # final op   0 1 1 2 2 3


# for i in range(5):
#     for j in range(i):
#         print("*", end="")
#     print() ##this help printing in seperate line to make it patteren 
#     # otherwise all * will be printed in single line 

# # i=0 
# # j=0 
# # *
# # * * 
# # * * *
# # * * * *

# total = 0
# for i in range(1, 4):
#     for j in range(1, i+1):
#         total += j
# print(total)

# dryrunn
# total = 0 
# i = 1 
# j = 1 
# total +j =1

# total = 1
# i = 2 
# j = 2 
# total +j =3

# total = 3 
# i = 3 
# j = 3 
# total +j =6

# total = 6
# i = 3 
# j = 4 
# total +j = 10

# SECTION 2 — ERROR DETECTION & CORRECTION (10 Questions)

# for i in range(5)
#     print(i)

# syntax error missing : 

# for i in range(5) :
#     print(i)
"""
0
1
2
3
4
"""

# i = 0
# while i < 3
# print(i)
# i += 1

##syntax error missing : after while line end
## logical error increment after print that will make it infinite loop 
# indentation error tab space print so it will print all 1 , 2  , 3 in seperate lne  now it will just print 3 aftter correctig upper error 
# i = 0
# while i < 3 :
#     i += 1
#     print(i)


# for i in range(3):
# print("Bioinformatics")

# indentation error tab space before print
# for i in range(3):
    # print("Bioinformatics")

# for i in range(1, 5, 0):
#     print(i)
##VALUE  ERROR  STEP SHOULD NOT BE  0 

# for i in range(1, 5, 2):
#     print(i)


# while True
#     print("Infinite")
# ##SYNTAX ERROR : MISSING
# while True:
#     print("Infinite")


# for i in [1, 2, 3]
#     print(i)
# else
#     print("Done")

# # syntax errormissing : after for and else
# for i in [1, 2, 3]:
#     print(i)
# else:
#     print("Done")


# for i in range(3):
#     if i = 2:
#         print(i)

##syntax error ==

# for i in range(3):
#     if i == 2:
#         print(i)


# count = 0
# while count < 5:
#     print(count)
#     count += 1
#   print("Done")
# ###indentation error 

# count = 0
# while count < 5:
#     print(count)
#     count += 1
# print("Done")

# for i in range(2):
#     for j in range(3):
#         print(i, j)

# syntax error missing : 
# SECTION 3 — CODE COMPLETION (10 Questions)

# Fill in the missing lines to make the output exactly as shown.
# Expected Output:
# 1
# 2
# # 3
# for i in range (1 , 4):
#     print(i)

# i=0
# while i<3 :
#     i+=1
#     print(i)

# expected output 0 1 2 3 4

# for i in range (0 , 5):
#     print (i , end=" ")

##expected output :  PythonPythonPython

# for i in range (3):
#     print("python" , end ="" )

# expected out put : 0 2 4 6 8
# for i in range (0 , 10 , 2):
#     print(i , end=" ")

# Expected Output: 1 3 5 7 9

# for i in range (1 , 10 , 2):
#     print(i , end = " ")

# Expected Output:Sum: 15 # 🔹 Use a loop to calculate the sum of 1 to 5
# sum=0
# for i in range (6):
#     sum += i
# print("sum:" ,sum )

# expected output this patteren 
# * * * 
# * * 
# * 

# n=4
# for i in range (n):
#     for j in range(i , n -1):
#         print ("*" , end=" ")
#     print()

# # Expected Output: Even number found: 4# 🔹 Use for loop and if to find first even number then break 
# num = [1 , 7, 3 , 4, 5 , 6 ]
# for i in num:
#     if i % 2 == 0:
#                 break
# print("first even no found:", i)
    

# # Expected Output: 0 1 1 2 3 5 8       first 7 no of fibbionachi series
# a=0
# b=1
# num=5
# print(a , b , end=" ")

# for _ in range( num ):
#     next_term = a+b
#     print(next_term , end = " ")
#     a , b = b , next_term 

# Expected Output: Factorial: 120
# num = 5 
# factorial = 1
# for i in range(1 , num +1):
#     factorial *= i
# print(f"factorial: , {factorial}")



# SECTION 4 — SCENARIO-BASED CODING (3 Questions)

# Write a Python program to calculate the GC content of a given DNA string using a for loop.
# Output → percentage GC.

# dna="ATCGGGGGCCCCTATAACCACACGCACCTCTGAGACG"
# G_count=0
# for i in dna :
#     if i == "G":
#         G_count += 1
# print("G_count :" ,G_count)

# C_count=0
# for j in dna :
#     if j == 'C':
#         C_count += 1
# print("C_count :" ,C_count)

# Perecentage_GC= G_count + C_count / len(dna) *100
# print (f"GC PERCENTAGE IN DNA STRING IS :{Perecentage_GC}")


# Scenario:
# Write a program that asks a user for a number and prints whether it is prime or not using a loop.


# num= int(input("enter number:"))
# if num<2:
#     print("not prime no")
# else:
# is_prime = True
# for i in range(2, int(num ** 0.5) + 1): ###num ** 0.5 use to take sqroot of num and then add 1 
#     if num % i == 0:  ##check if its divvisible by i 
#         is_prime = False
#         break
# if is_prime:
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")



# Write a program using nested loops to print:
# 1
# 12
# 123
# 1234
# 12345

# num=5
# for i in range (1 , 6 ):
#     for j in range ( 1 , i +1):
#         print(j , end=" ")
#     print()