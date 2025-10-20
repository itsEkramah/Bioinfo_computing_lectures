##print from 1 to 100

# i = 1
# while i <= 100 :
#     print(i)
#     i +=1



##print reverse 1 to 100

# i = 100
# while i >= 1:
#     print (i)
#     i -= 1



##print even numbers from 1 to 100

# i=2
# while i<=100:
#     print(i)
#     i += 2
                    #(i =+ 2) wrong it will only print 2 ,2 ,2



##print odd number 1 to 100

# i=1
# while i <= 100:
#     if i%2 !=0:
#         print(i)
#     i += 1
        #(always take care of increment scope should be in loop scope not inside if statement)



##print sum of 1 to 100

# i=1
# sum=0
# while i <= 100 :
#     sum = sum +i
#     i += 1
# print(sum)



##multiplication table of n

# n =int(input("enter number:"))
# i=1
# while i <11 :
#     print (n , "x" , i , "=" , n*i)
#     i += 1



##print the elements of this list [12, 75, 150, 180, 145, 525, 50] by using loop

# list1 = [12, 75, 150, 180, 145, 525, 50]
# i = 0
# while i < len (list1) :
#     print (list1[i])
#     i += 1



##print the elements of this list [12, 75, 150, 180, 145, 525, 50] which are greater than 150

# list1 = [12, 75, 150, 180, 145, 525, 50]
# i = 0
# while i< len(list1):
#     if list1[i] > 150:     ##(condition always compare int number  with list1[i] not just with list1 it will cause type error)
#         print(list1[i])
#     i +=1



##print the elements of this list [12, 75, 150, 180, 145, 525, 50] which are even

# list1 = [12, 75, 150, 180, 145, 525, 50]
# i = 0 
# while i<len(list1):
#     if list1[i] %2 ==0:
#         print(list1[i])
#     i =+1
    
    
    
# #print the elements of this list [12, 75, 150, 180, 145, 525, 50] which are odd

# list1 = [12, 75, 150, 180, 145, 525, 50]
# i= 0
# while i < len(list1):
#     if list1[i] % 2 != 0:
#         print(list1[i])
#     i+= 1    



##print the elements of this list [12, 75, 150, 180, 145, 525, 50] which are multiple of 5

# list1= [12, 75, 150, 180, 145, 525, 50]
# i= 0 
# while i < len (list1):
#     if list1[i] % 5 ==0:
#         print(list1[i] , "is divisible of 5 ")
#     i+= 1




##search for number x in list [12, 75, 150, 180, 145, 525, 50]

# list1= [12, 75, 150, 180, 145, 525, 50 ]
# x = int(input("enter number x:"))
# i=0
# while i < len (list1):
#     if list1[i] == x :
#         print("x found at index" , i)
#         break
#     else :
#         print("number not found in list")
#     i+=1





### for loop practics



##print veg in list

# veg = ["carrot" , "potato" , "cabbage" , "onion"]
# for i in veg:
#     print(i)



##search char in string

# str = "abcdefghijklmnop"
# for char in str :
#     if (char == 'e'):
#         print( char , "chr found")



##print list by using for loop

# list1 = [12, 75, 150, 180, 145, 525, 50 ]
# for i in list1:
#     print(i)



# #search for number in list

# list1 = [12, 75, 150, 180, 145, 525, 50 ]
# x = int(input("enter number to search:"))
# for i in range(len(list1)):
#     if x == list1[i]:
#         print("num found at index:" , i)
#         break
#     else:
#         print("num not fffouund")


##range function     
# for el in range(5):
#     print(el)

# for el in range(1,11):
#     print(el)

# for el in range( 1 , 18 , 5):
#     print(el)

##print num from 1 - 100

# for i in range (1,101):
#     print(i)

##print num from 100 to 1

# for i in range (100, 0 , -1):
#     print(i)




# #print multiplication table of n

# n = int(input("enter number n:"))
# for i in range(1 , 11):
#     print(n ,"x" ,i  ,"=" , n*i)


##find the sum of first n nubers

# n=int(input("enter   number n:"))
# sum=0
# i=1
# for i in range (i , n+1):
#     sum +=i
# print("sum of n numbers is" , sum)
# #same with while loop
# n=int(input("enter   number n:"))
# sum=0
# i=1
# while i <=n:
#     sum+=i
#     i+=1
# print("sum of n numbers is" , sum)




###factorial of n numbers
# n=int(input("enter number n:"))
# factorial=1
# for i in range(1 ,n+1):
#     factorial = factorial*i
# print("factorial of", n  ,"is:" , factorial)


###print patterens
##print square shape

# n=int(input("enter number n:"))
# for i in range(n):
#                 for j in range(n):
#                         print('*' , end='' )
#                 print()


# #print decreasing triangle
# n=int(input("enter n:"))
# for i in range (n):
#         for j in range(i,n):
#                 print('*', end='')
#         print()
        
# #print increasing triangle
# n=int(input("enter value for n:"))
# for i in range(n):
#         for j in range(i+1):
#                 print('*' , end='')
#         print()

##
# n=int(input("enter value of n:"))
# for i in range(n):
#         for j in range(i+1):
#                 print('' ,end='')
#         for j in range( i + 1):
#                 print('*' ,end='')
#         print()


# n = int(input("Enter value of n: "))
# for i in range(n):
#     # This loop prints the leading spaces for each row.
#     # The number of spaces increases with each new line.
#     for j in range(i):
#         print(" ", end="")
    
#     # This loop prints the stars.
#     # The number of stars decreases with each new line.
#     for k in range(n - i):
#         print("*", end="")
        
#     # This prints a new line to start the next row.
#     print()


num= int (input("enter number:"))
for i in range (n):
        for j in range(i+1):
                print('', end='')
        for j in range(n-i):
                print('*' , end='')
        print()