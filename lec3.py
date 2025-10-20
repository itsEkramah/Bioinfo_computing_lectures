"""
def percentage (marks , total_marks):
    return (int(marks obtaiined) / int(total_marks) * 100)

percentage=[]

for i in range (num_studennts):
    marks = (int(input("enter marks:")))
total_marks = (int(input("enter total marks :")))
            
"""
 
"""variable vs datastructure 
list tuple set dictionat
list main datatype fix nhihay 

"""

""""""

#Tuples
'''
    1. Ordered collection of elements
    2. Round brackets ()
    3. Can store different data types
    4. Unmutable
'''
"""
tup1=(1, 0.005, True , "AAAA")
print(type(tup1))
print(type(tup1 [1]))
print(type(tup1) [-1])
print(len(tup1))
print(tup1[1:4])


tup2= (2 , "bbb" , False , 60.0005 )
print(tup1+tup2)

tup3 = (2,3,4,5,6,7,8)
print(max(tup3))
print(min(tup3))
print(sum(tup3))
print((tup3)*2) 


for i in tup3 :
    print(i*2)  
"""


#List
"""
    1. Ordered Collection of elements
    2. Square brackets []
    3. Changeable 
    4. Different data types can be stored
"""
"""
List1=[1,5.002, True, "aaa"]
print(type(List1))
print(len(List1[3]))

List2=[2,8.05,False,"ABC"]


print(List1+List2)


list3 = [2,3,4,5,6,7,8,15,14,7,5,254]
print(max(list3))
print(min(list3))
print(sum(list3))
list3.sort()
print(list3) 

"""
"""
list3.append(List2)
print(List3)

List3.extend(List2)
print(List3) 

"""


"""

list1 = [[2,3,4],[5,6,7],[8,15,14],[7,5,254]]
print(list1)

for i in range(len(list1)):
    for j in range(len(list1[i])):
        list1[i][j] = list1[i][j] * 2
print(list1)

"""
#biopython basics , list within list,  nested loop

# # 1. Find the Sum of All Numbers

# total_sum = 0
# list1 = [[2, 3, 4], [5, 6999, 7], [8, 15, 14], [7, 5, 254]]
# print(list1)
# for row in list1:
#     for number in row:
#         total_sum += number
        
# print("total sum is:", total_sum)



# Data Type	Ordered?	Changeable? (Mutable)	Allows Duplicates?
# List              	Yes         	Yes     	Yes
# Tuple	                Yes	            No      	Yes
# Set	                No          	Yes     	No
# Dictionary        	No           	Yes        	No (keys must be unique)
