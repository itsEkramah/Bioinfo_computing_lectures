"""
Lecture 2 – Loops in Python

Types of loops:
    1. for loop   → used when you know how many times to repeat
    2. while loop → used when you want to repeat until a condition is true
"""
"""
# Example 1: for loop with range
for x in range(7):   # prints numbers from 0 to 6
    print(x)


# while loop
x = 0
while x < 7:         # repeats until 1 to  7
    x += 1
    print(x)

x = 0
while x < 7:         # repeats until 0 to 6
    print(x)
    x += 1


# Multiplication Table of 2

for i in range(1, 11):
    print(f"2 x {i} = {2 * i}")

"""
fruit=["Apple","Orange","Mango"]
"""print(fruit[0])
print(fruit[1])
print(fruit[1])
print(fruit[2])
"""
for x in fruit:
    print(x)
    if(x=="Orange"):
        print(x)
        
# Iterating through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)


# Percentage Calculator (single student)
"""
name = input("Enter your name: ")
obtained = int(input("Enter obtained marks: "))
total = int(input("Enter total marks: "))
percentage = (obtained / total) * 100
print(name, "got", percentage, "%")
"""

"""

for num in range(2, 20):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{num} is a prime number.")
#prime

students = []   

while True:
    name = input("Enter student name (or 'q' to quit): ")
    if name.lower() == "q":
        break   # exit loop when 'q' is entered
    
    obtained = int(input("Enter obtained marks: "))
    total = int(input("Enter total marks: "))
    percentage = (obtained / total) * 100
    
    student_result = f"{name} has percentage {percentage:.2f}%"
    students.append(student_result)

print("\nAll Results:")
for result in students:
    print(result)




"""
name =1
data[]
counter=0
while(name!= "q")
    name = input("enter ur name")
    if name(!="q"):
        obtained = int(input("Enter obtained marks: "))
        total = int(input("Enter total marks: "))
        percentage = (obtained / total) * 100
        st = name+"has percentage"+str(percentage)
        data.append(st)
        counter+=1
print(data)
"""