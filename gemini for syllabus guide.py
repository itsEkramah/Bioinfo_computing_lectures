# Hello, ChatGPT. You are an expert Python programming tutor and exam preparation coach. My goal is to get 100% exam-ready for my Python exam, which is in 2 days.

# I am providing you with my complete, raw collection of class notes, which includes code snippets, comments, and topics. Your task is to use this information to create a structured and intensive 2-day study plan that will make me master these concepts.

# My exam has a very specific four-part paper pattern, and all practice must be tailored to it:

# Question 1: Output Prediction (20 Questions) - I will be given a code snippet and must "dry run" it to predict the exact output.

# Question 2: Error Prediction & Correction (20 Questions) - I will be given code that contains an error (Syntax, Runtime, or Logical). I must identify the error, name it (e.g., TypeError, IndentationError), and provide the corrected code.

# Question 3: Incomplete Code Completion (25 Questions) - I will be given an expected output and a code snippet with missing lines. I must fill in the blanks to produce that exact output.

# Question 4: Scenario-Based Code Writing (Long Questions) - I will be given a problem description (e.g., "Write a program to...") and must write the complete Python script from scratch.

# PHASE 1: ANALYSIS AND PLANNING
# Your first job is to analyze all my notes (provided below the [---START---] marker) and do the following:

# Generate a Syllabus: Read all my notes and extract a clean, structured syllabus. Organize all topics logically (e.g., "1. Python Basics", "2. Control Flow", "3. Data Structures", etc.). IMPORTANT: My notes mention "Biopython" and API usage, but the user explicitly stated to EXCLUDE Biopython. However, any examples using biological data (like DNA/RNA translation or GC content) that use core Python (like dictionaries, re module, string methods) ARE part of the exam and must be included in the syllabus under their respective topics (e.g., "Dictionaries", "String Methods", "Regex Module").

# Confirm the Exam Format: Briefly restate the four-part paper pattern I described above so I know you understand it.

# Propose a 2-Day Study Plan: Based on the syllabus you create, propose a high-level, intensive 2-day study plan. (e.g., "Day 1: Topics 1-4 (Basics, Control Flow, Data Structures, Functions). Day 2: Topics 5-8 (OOP, Modules, File I/O, Error Handling) + Full Review").

# Please present this 3-part analysis first and wait for my confirmation before proceeding to Phase 2.

# PHASE 2: INTERACTIVE PRACTICE SESSION (Do NOT start this until I confirm Phase 1)
# Once I confirm the plan, we will begin an intensive, interactive practice session.

# You will guide me one topic at a time from the syllabus.

# For the first topic (e.g., "1. Python Basics"), you will generate a set of 10 practice questions distributed across my 4 exam formats (e.g., 3 Output Prediction, 3 Error Correction, 2 Code Completion, 2 Scenario Writing).

# You will NOT show the answers.

# I will write my answers to your 10 questions.

# When I am ready, I will ask you for the answers. You will then provide:

# The correct answers.

# A detailed, step-by-step "dry run" for the Output Prediction questions.

# A clear explanation of the error and the fix for the Error Correction questions.

# The correct solutions for the Completion and Scenario Writing questions.

# After I review the answers, you will ask if I want (a) more practice questions on this same topic or (b) to move to the next topic in the syllabus.

# We will repeat this process until we have covered the entire syllabus.

# [---START OF MY NOTES---]"""
#     >   greater than
#     <   less than
#     ==  equal to
#     >=  greater than or equal to
#     <=  less than or equal to
# """

# """
# #Simple addition
# x = 6
# y = 8
# print("Sum of x and y:", x + y)
# """

# """
# #Input and multiplication
# # Note: input() always returns a string, so we need type casting
# x = int(input("Enter value of x: "))
# y = int(input("Enter value of y: "))
# print("Product of x and y:", x * y)

# """

# # Notes: Type Casting

# """
# Type casting = converting one data type into another
#     int()   → convert to integer
#     float() → convert to decimal
#     str()   → convert to string

# Example:
#     age = int(input("Enter age: "))    # converts input (string) to integer
#     marks = float(input("Enter marks: "))  # converts input to float
# """

# """
# # Percentage calculation

# obtained = int(input("Enter obtained marks: "))
# total = int(input("Enter total marks: "))
# percentage = (obtained / total) * 100
# print("Percentage:", percentage)

# """

# #if else age and percentaggggge
# age = int(input("Enter age of student: "))
# percent = float(input("Enter percentage of student: "))

# if age > 10 and percent > 70:
#     print("Student is eligible")
# else:
#     print("Student is not eligible")


# """
#  Learn how to use APIs
# NCBI Entrez API to fetch biological data.
# """


# """
# Lecture 2 – Loops in Python

# Types of loops:
#     1. for loop   → used when you know how many times to repeat
#     2. while loop → used when you want to repeat until a condition is true
# """
# """
# # Example 1: for loop with range
# for x in range(7):   # prints numbers from 0 to 6
#     print(x)


# # while loop
# x = 0
# while x < 7:         # repeats until 1 to  7
#     x += 1
#     print(x)

# x = 0
# while x < 7:         # repeats until 0 to 6
#     print(x)
#     x += 1


# # Multiplication Table of 2

# for i in range(1, 11):
#     print(f"2 x {i} = {2 * i}")

# """
# fruit=["Apple","Orange","Mango"]
# """print(fruit[0])
# print(fruit[1])
# print(fruit[1])
# print(fruit[2])
# """
# for x in fruit:
#     print(x)
#     if(x=="Orange"):
#         print(x)
        
# # Iterating through a list
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit)


# # Percentage Calculator (single student)
# """
# name = input("Enter your name: ")
# obtained = int(input("Enter obtained marks: "))
# total = int(input("Enter total marks: "))
# percentage = (obtained / total) * 100
# print(name, "got", percentage, "%")
# """

# """

# for num in range(2, 20):
#     is_prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             is_prime = False
#             break
#     if is_prime:
#         print(f"{num} is a prime number.")
# #prime

# students = []   

# while True:
#     name = input("Enter student name (or 'q' to quit): ")
#     if name.lower() == "q":
#         break   # exit loop when 'q' is entered
    
#     obtained = int(input("Enter obtained marks: "))
#     total = int(input("Enter total marks: "))
#     percentage = (obtained / total) * 100
    
#     student_result = f"{name} has percentage {percentage:.2f}%"
#     students.append(student_result)

# print("\nAll Results:")
# for result in students:
#     print(result)




# """
# name =1
# data[]
# counter=0
# while(name!= "q")
#     name = input("enter ur name")
#     if name(!="q"):
#         obtained = int(input("Enter obtained marks: "))
#         total = int(input("Enter total marks: "))
#         percentage = (obtained / total) * 100
#         st = name+"has percentage"+str(percentage)
#         data.append(st)
#         counter+=1
# print(data)
# """


# """
# def percentage (marks , total_marks):
#     return (int(marks obtaiined) / int(total_marks) * 100)

# percentage=[]

# for i in range (num_studennts):
#     marks = (int(input("enter marks:")))
# total_marks = (int(input("enter total marks :")))
            
# """
 
# """variable vs datastructure 
# list tuple set dictionat
# list main datatype fix nhihay 

# """

# """"""

# #Tuples
# '''
#     1. Ordered collection of elements
#     2. Round brackets ()
#     3. Can store different data types
#     4. Unmutable
# '''
# """
# tup1=(1, 0.005, True , "AAAA")
# print(type(tup1))
# print(type(tup1 [1]))
# print(type(tup1) [-1])
# print(len(tup1))
# print(tup1[1:4])


# tup2= (2 , "bbb" , False , 60.0005 )
# print(tup1+tup2)

# tup3 = (2,3,4,5,6,7,8)
# print(max(tup3))
# print(min(tup3))
# print(sum(tup3))
# print((tup3)*2) 


# for i in tup3 :
#     print(i*2)  
# """


# #List
# """
#     1. Ordered Collection of elements
#     2. Square brackets []
#     3. Changeable 
#     4. Different data types can be stored
# """
# """
# List1=[1,5.002, True, "aaa"]
# print(type(List1))
# print(len(List1[3]))

# List2=[2,8.05,False,"ABC"]


# print(List1+List2)


# list3 = [2,3,4,5,6,7,8,15,14,7,5,254]
# print(max(list3))
# print(min(list3))
# print(sum(list3))
# list3.sort()
# print(list3) 

# """
# """
# list3.append(List2)
# print(List3)

# List3.extend(List2)
# print(List3) 

# """


# """

# list1 = [[2,3,4],[5,6,7],[8,15,14],[7,5,254]]
# print(list1)

# for i in range(len(list1)):
#     for j in range(len(list1[i])):
#         list1[i][j] = list1[i][j] * 2
# print(list1)

# """
# #biopython basics , list within list,  nested loop

# # # 1. Find the Sum of All Numbers

# # total_sum = 0
# # list1 = [[2, 3, 4], [5, 6999, 7], [8, 15, 14], [7, 5, 254]]
# # print(list1)
# # for row in list1:
# #     for number in row:
# #         total_sum += number
        
# # print("total sum is:", total_sum)



# # Data Type	Ordered?	Changeable? (Mutable)	Allows Duplicates?
# # List              	Yes         	Yes     	Yes
# # Tuple	                Yes	            No      	Yes
# # Set	                No          	Yes     	No
# # Dictionary        	No           	Yes        	No (keys must be unique)



# # #report for project   methodology goal advantage how we will achieve this    week wise division  bioinformatics  ngs relevent pipeline structural prediction  machine learning model    api use 






# # #Dictionary
# # """
# # 1. An unordered , un indexed collection of elements
# # 2. key and values
# # 3. Declared curly brackets {}
# # 4. Mutatable
# # """
# # dict1={"apples":200 , "banana":150 , "peach":250}
# # print(dict1)
# # print(dict1["banana"])
# # dict1["banana"]=100
# # print(dict1)

# # print(len(dict1))
# # print (dict1.keys())
# # print(dict1.values())
# # print(max(dict1.values()))
# # print(min(dict1.values()))

# # # dict1.pop("banana")
# # # print(dict1)

# # # print(dict1["banana"])

# # ##errors type error synrax error index error value error key error identation error

# # # dict1["banana"]=100
# # # print(dict1["banana"])


# # dict2={"onion":50 , "tomato":80 , "potato":30}
# # print(dict2)
# # dict1.update(dict2)
# # print(dict1)

# # t2={"onion":[50,60 , 70 , 80] , "tomato":80 , "potato":[30,40 , 50 ,77 ]}
# # print(t2)

# # for x in dict1:
# #     print(x)



# # gene1={"p1": [1,0,0,1]}
# # gene2={"p2"  : [0,1,0,0]}
# # gene3={" p3": [0,0,1,0]}
# # gene4={"p4  ": [0,0,1,1]}

# # for x in gene1:
# #     if(gene1[x][i]==1):
# #         print(x, "mutated gene")

# genes = {"EGFR": [1, 0, 0, 0], "FGFR": [0, 1, 0, 0], "AKT": [0, 0, 1, 1], "TP53": [0, 0, 1, 1]}
# c = 0
# inputgene = ""
# while inputgene != "q":
#     print("list of genes:", list(genes.keys()))
#     inputgene = input("enter gene (or 'q' to quit): ")
#     if inputgene == "q":
#         break
#     if inputgene in genes:
#         for i in genes[inputgene]:
#             if i == 1:
#                 print(inputgene)
#         c += 1
#         print(inputgene, "is mutated in patient", c)
#     else:
#         print("Gene not found. Please enter a valid gene name.")







# # #Sets
# # """
# # 1. An unordered and unindexed collection of items
# # 2. Declare curly brackets {}
# # 3. Duplicates not allowed
# # """

# # set1={"EGFR","FGFR","AKT","TP53"}
# # set2={"EGFR","CTNNB1","WNT","MAPK"}

# # set3=set1.intersection(set2)
# # print(set3)

# # set4=set1.union(set2)
# # print(set4)

# # set3.remove("EGFR")

# # set3.add("EGFR")


# # GENE ADD PATHWAY SETS GENE 1 TO 6 GENES CANCER GENES USE SET TO MAKE THIS CODE RUN WE WILL GIVE PATHWAY AND IT WILL TELL US HOW MANY GENES ARE THERE IN PATHWAY AND HOW MANY CANCER GENES ARE THERE IN PATHWAY


# # # #loops

# # # i=0
# # # while i<6:
# # #     i+=1  
# # #     if i==2:
# # #         continue
# # #     if i==3:
# # #         break
# # #     print(i-1)
    
    
# # #     # i=1: not 2 or 3, so print(1)
# # #     # i=2: continue, so skip print
# # #     # i=3: break, exit loop before print


# # # i=0
# # # while i<6:
# # #     i+=1  
# # #     if i==3:
# # #         continue
# # #     print(i-1)
# # # else:
# # #     print("loop ended")
    
# # #     # i=1: not 2 or 3, so print(1)
# # #     # i=2: not 3, so print(2)
# # #     # i=3: continue, so skip print
# # #     # i=4: not 3, so print(4)
# # #     # i=5: not 3, so print(5)
# # #     # i=6: not 3, so print(6)
# # #     # loop ends normally, so else block runs





# # fruits=["apple","banana","orange"]
# # for i in fruits:
# #     if i=="banana":
# #         continue
# #     print(i)



# # fruits=["apple","banana","orange"]
# # for i in fruits:
# #     if i=="banana":
# #         break
# #     print(i)
# #     #loop end ho ga  program nhi
# # print(fruits)


# # x=int(input("enter a number:"))
# # y=int(input("enter a number:"))

# # sum=0
# # for i in range(x,y+1):
# #     if x ==0 :
# #          break 
# #     if y ==1:
# #         continue
# #     sum+=i
# # print("sum is:", sum)



# # while True:
# #     x=int(input("enter a number:"))
# #     y=int(input("enter a number:"))
# #     if x==0:
# #         break
# #     elif y==1:
# #         continue
# #     sum=0
# #     for i in range(x,y+1):
# #         sum+=i
# #     print("sum is:", sum)


# # for x in range (3,32 ,3):
# #     print(x)
    
# """ cancer pathway : egfr akt
# metabolic pathway : tp52 ,ctknnb1 
# immune pathway : fgfr , akt , cdb
# """


# # genes = {"EGFR": [1, 0, 0, 0], "FGFR": [0, 1, 0, 0], "AKT": [0, 0, 1, 1], "TP53": [0, 0, 1, 1]}

# # pathways = {
# #     "Cancer": {"EGFR", "AKT"},
# #     "Metabolic": {"TP53", "CTNNB1"},
# #     "Immune": {"FGFR", "AKT", "CDB"}
# # }

# # c = 0
# # inputgene = ""

# # while True:
# #     pw = input("Enter pathway name: ")
    
# #     if pw == "q":
# #         print("Program ended")
# #         break
    
# #     if pw in pathways:
# #         gset = pathways[pw]
# #         print("Pathway:", pw)
# #         print("Total genes:", len(gset))
        
# #         cset = gset & cancer_genes
# #         print("Cancer genes:", len(cset), cset if cset else "None")
        
# #         c += 1
# #         print(inputgene, "is mutated in patient", c)
# #     else:
# #         print("Gene not found. Please enter a valid gene name.")




# genes = {"EGFR": [1, 0, 0, 0], "FGFR": [0, 1, 0, 0], "AKT": [0, 0, 1, 1], "TP53": [0, 0, 1, 1]}

# cancer_pathways = {"EGFR", "AKT"}
# metabolic_pathways = {"TP53", "CTNNB1"}
# immune_pathways = {"FGFR", "AKT", "CDB"}

# c = 0
# inputpathway = ""

# while inputpathway != "q":
#     print("list of genes:", list(genes.keys()))
#     inputpathway = input("enter pathway (or 'q'  to quit): ")
    
# for y in inputpathway:
#     if(y in genes.keys()):
#         c=0
        
# if(input(cancer_pathways)):
#     print("cancer pathway")
# elif(input(metabolic_pathways)):
#     print("metabolic pathway")
# elif(input(immune_pathways)):
#     print("immune pathway")
    
# for i in genes:
#     if inputpathway == "q":
#         break
#     c+=1
#     for x in genes([i]):
#         if x == 1:
#             c+=1
#     print("Pathway:", inputpathway)
    
    
#     if inputpathway == "q":
#         break
#     if inputpathway in genes:
#         for i in genes[inputpathway]:
#             if i == 1:
#                 print(inputpathway)
#         c += 1
#         print(inputgene, "is mutated in patient", c)
#     else:
#         print("Gene not found. Please enter a valid gene name.")
        
# else:
#     print("Pathway not found. Please enter a valid pathway name.")
    
    
    
# # Gene mutations for 4 patients
# # 1 = mutated, 0 = not mutated
# mutations = {
#     "EGFR": [1, 0, 0, 0],
#     "FGFR": [0, 1, 0, 0],
#     "AKT": [0, 0, 1, 1],
#     "TP53": [0, 0, 1, 1],
#     "CTNNB1": [0, 1, 0, 1],
#     "CDB": [0, 0, 0, 0]
# }

# # Pathways with their genes (sets are used because they store unique values)
# pathways = {
#     "Cancer": {"EGFR", "AKT"},
#     "Metabolic": {"TP53", "CTNNB1"},
#     "Immune": {"FGFR", "AKT", "CDB"}
# }

# # number of patients = length of any gene’s mutation list
# num_patients = len(mutations["EGFR"])

# print("Available pathways:", list(pathways.keys()))
# print("Type 'q' to quit.")

# while True:
#     # Ask user for one or more pathways
#     input_pathway = input("\nEnter pathway name(s): ")

#     # If user types q → program ends
#     if input_pathway.lower() == "q":
#         print("Program ended.")
#         break

#     # ---- MULTIPLE PATHWAYS LOGIC ----
#     # split input by comma → creates a list of pathways
#     # Example: "Cancer, Immune" → ["Cancer", " Immune"]
#     chosen_pathways = input_pathway.split(",")

#     # Loop over each pathway entered by user
#     for pathway in chosen_pathways:
#         pathway = pathway.strip()   # remove extra spaces (e.g. " Immune" → "Immune")

#         if pathway in pathways:
#             print("\nPathway:", pathway)
#             genes_in_pathway = pathways[pathway]   # get genes for that pathway
#             print("Genes in pathway:", genes_in_pathway)

#             # Show patient mutations
#             for i in range(num_patients):
#                 mutated = []   # genes mutated in this patient
#                 unmutated = [] # genes not mutated in this patient
#                 for g in genes_in_pathway:
#                     if mutations[g][i] == 1:
#                         mutated.append(g)
#                     else:
#                         unmutated.append(g)
#                 print("Patient", i+1)
#                 print("  Mutated:", mutated if mutated else "None")
#                 print("  Unmutated:", unmutated if unmutated else "None")

#         else:
#             print("\nPathway not found:", pathway)
            
            
#             #dictionary names ki 1 aur dictonary banaa laien compare values input compare with its key 
# #2nd way ask user 1st pathway name 2nd pathway name compare both pathways genes

# # #functions
# # #resuable block of code that perform a specific task
# ##DRY- DONT REPEAT YOURSELF
# # 
# # # def function_name(parameters):
# # #     #function body
# # #     #return statement         
# # #function call
# # # function_name(arguments)
# # #arguments- actual value passed to function
# # #parameters- variable in the function defination that recieves the value passed
# # #return statement- used to exit a function and go back to the place where it was called


# # # def function_1():
# # #     print("this ia oue first function")
    
# # # # function_1()
# # # # function_1()
# # # # function_1()
# # # # function_1()
# # # # function_1()

# # # def function_2(name="adnan"):
# # #     print("this ia oue first function" , "I am ", name,)
# # # function_2("ekramah")
# # # function_2("ali")
# # # function_2()


# # # def function_3(fname = "adnan", lname = "ansari"):
# # #     print("this ia oue first function" , "I am ", fname, lname)
# # # function_3( "ekramah" , "chaudhary")

# # def function_3(fname = "adnan", lname = "ansari"):
# #     print("this ia oue first function" , "I am ", fname, lname)
# # function_3(lname = "ekramah" ,fname= "chaudhary")
# # function_3()

# # #function ask user kid names ## unknown no of arguments
# # def function_4(*kids): ## * is use to pass unknown no of arguments
# #     function_4("ekramah" , "ali" , "umer" , "s")
# #     print(kids)
# #     for i in kids :
# #         print(i)
# #     print(kids[-1])

# # y = len(kids)
# # print(kids[y-1])  ##length use index to print last element if we dont use y-1 it will be index out of range 

# ##user unlimited time input marks le ga  function ho ga perceentage ka terminate loop when i enter q

# # def percentage(marks_obtained, total_marks=100):
# #     return (int(marks_obtained) / int(total_marks)) * 100
# # num_students = int(input("Enter number of students in class: "))
# # percentages = []
# # for _ in range(num_students):
# #     marks = input("Input Marks Obtained: ")
# #     total = input("Input Total Marks: ")

# #     perc = percentage(marks, total)
# #     x = percentage(marks)
# #     if percentage(marks)>50:
# #         print("pass")
# #     else:
# #         print("fail")
# #     print("Percentage:", perc)
# #     percentages.append(perc)
    
    
# # def percentage (mo):
# #     return (int(mo) / 30 * 100)
# # while True:
# #             mo = int(input("Input Marks Obtained: "))
# #             if(mo>30):
# #                 break
# # x= percentage(mo)
# # print("Percentage:", x)    
# # if (x<50):
# #     print("fail")
# # elif (x>50 & x<80):
# #     print("avg")
# # elif (x>=80 & x<=100):
# #     print("exelent")
                



# # # recursive function khud ko call krta
# # def recursive_fun(k):
# #     if(k>0):
# #         result = k + recursive_fun(k-1)# if just added k it will staart infinite call  so we use k-1
# #         print(result)
# #     else:
# #         result = 0
# #     return result

# # recursive_fun(4)


# # Dry run for k=4:
# # recursive_fun(4)
# # 4 > 0: result = 4 + recursive_fun(3)
# #   recursive_fun(3)
# #   3 > 0: result = 3 + recursive_fun(2)
# #     recursive_fun(2)
# #     2 > 0: result = 2 + recursive_fun(1)
# #       recursive_fun(1)
# #       1 > 0: result = 1 + recursive_fun(0)
# #         recursive_fun(0)
# #         0 not > 0: result = 0
# #       returns 0, so result = 1 + 0 = 1, print(1)
# #     returns 1, so result = 2 + 1 = 3, print(3)
# #   returns 3, so result = 3 + 3 = 6, print(6)
# # returns 6, so result = 4 + 6 = 10, print(10)
# #joo sub se pehle call ho ga wo last main print ho ga  q k uski execustion ki values depend on output of next call



# # next class task --> practice funtions and loops combine examples and different logics 
# # #factorial code by using functions and by using loop both ways   try multiple different approaches 



# # ##write fun to calculate factorial of n
# # n=int(input("enter a number:"))
# # def factorial(n):
# #     result = 1
# #     for i in range(1, n + 1):
# #         result *= i
# #     return result

# # print(factorial(n))


# # def factorol(n):
# #     if n == 0 or n==1 :
# #         return 1
# #     else:
# #         return n * factorol(n-1)
    
# # n= int(input("enter number"))
# # print(f"the factorial of {n} is {factorol(n)}" )

# def factorial (num):
#     if num == 0 or num ==1:
#         return 1
#     else:
#         return num* factorial(num-1)

# num=int(input("enter number"))
# print(f"the factorial of{num} is {factorial(num)}") 


# # Object-Oriented Programming (OOP) in Python - Basic Concepts

# # 1. Class: A blueprint for creating objects.
# # 2. Object: An instance of a class.
# # 3. Inheritance: A way to form new classes using classes that have already been defined.
# # 4. Encapsulation: Bundling data and methods that operate on that data within one unit (class).
# # 5. Polymorphism: The ability to use a common interface for multiple forms (data types).

# # Example Syntax:

# # Define a class
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound.")

# # Inheritance
# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} barks.")

# # Create objects
# a = Animal("Generic Animal")
# d = Dog("Buddy")

# a.speak()  # Output: Generic Animal makes a sound.
# d.speak()  # Output: Buddy barks.

# class person:
#     def __init__(self,name,age,id):
#         self.name=name
#         self.age=age
#         self.id=id
    
#     def __str__(self):
#         return f"{self.name} {self.age} {self.id}"
    
#     def Welcome (self):
#         print("Welcome !" + self.name)

# class student(person):
#     def __init__(self, name, age, id, dept, doa):
#         super().__init__(name,age,id)
#         self.dept=dept
#         self.doa=doa
        
#     def Welcome(self):
#         print(self.name + " you are welcome in the department of "+self.dept+". you became our student on"+self.doa+".")
        
# p1=student("Ali",20,12231,"BIF","10/22/2024")

# p1.Welcome()






# ###class is a blueprint for creating objects 
# ##it defines a set of attributes and methods that the created objects will have.


# class Student(Person): #person class se inherit kr rha
    
# # #init method is a constructor that is called when an object is created from the class 
# # # and it allows the class to initialize the attributes of the class.
# ## simple wording main init constructor hai jo object create krte hi call hota hai aur attributes ko initialize krta hai
    
#     def __init__(self, Name, ID, Age, Blood_Group, Department, Semester, GPA): 
#     ## name id age blood_group are objects of parent class person

# #constructor is a special method that is called when an object of a class is created

#         super().__init__(Name, ID, Age, Blood_Group) #calling parent class constructor
# ##super() function is used to call the parent class constructor
#         self.dept = Department  
#         #self.dept ka use kr k 
#         ##hum student class main dept attribute ko define kr rhy hain
#         self.sem = Semester
#         self.gpa = GPA

#     def __str__(self): ##string method to print object details in simple words 
#         ##it is used to return a string representation of the object
#         return (f"Student -> Name: {self.name}, ID: {self.id}, Age: {self.age}, "
#                 f"Blood Group: {self.blood_group}, Dept: {self.dept}, Semester: {self.sem}, GPA: {self.gpa}")
# ##self. ka use kr k hum class ke attributes ko access kr rhy hain 
# ##f string ka use kr k hum string main variables ko directly embed kr skty hain

# class Faculty(Person): #person class se inherit kr rha
# ##inheritence ka matlab hai k ek class doosri class ke attributes aur methods ko use kr skti hai
#     def __init__(self, Name, ID, Age, Blood_Group, Department, Designation, Salary):
#         super().__init__(Name, ID, Age, Blood_Group)
#         self.dept = Department
#         self.designation = Designation

#     def __str__(self):
#         return (f"Faculty -> Name: {self.name}, ID: {self.id}, Age: {self.age}, "
#                 f"Blood Group: {self.blood_group}, Dept: {self.dept}, Designation: {self.designation}")



# p1 = Person("AAAA", 123, 24, "B+")
# p2 = Person("BBBB", 124, 22, "O+")

# s1 = Student("Ekramah", 567, 21, "AB+", "Biochemistry", 5, 3.8)

# f1 = Faculty("SIR Adnan", 789, 45, "A+", "Bioinformatics", "Associate Professor")


# print(p1)
# print(p2)
# print(s1)
# print(f1)


# ## USING OOP AND 
# # INHERITENCE CONCEPTS ASSIGNMENT QAU CMS BY USING INHERITANCE OBJECTS OF FACULTY MEMBERS STAFF AND STUDENTS  INFORMATION 



# # class landanimals:

# #     def feature(self):
# #         print("they can walk on land.")

# # class wateranimals:
# #     def feature(self):
# #         print("they can swim in water.")
        
# # # p1=landanimals()
# # # p2=wateranimals()
# # # p1.feature()
# # # p2.feature()

# # # class amphibians(landanimals,wateranimals):#inherit cherachetr of landanimal and wateranimals 
# # #     def test(self):
# # #         print("they can live both on land and in water.")
# # #         """
# # #         def feature(self):
# # #             retrun .super().feature()#it will call the feature method of the first parent class landanimals
# # # """
# # # p3=amphibians()
# # # p3.feature()#it will call the feature method of the first parent class landanimals
# # # p3.test()



# # #modules : are files containing python code
# # # they can define functions, classes and variables
# # # # they can also include runnable code
# # # multiple classes

# # # import module1 
# # # module1.greeting("ekramah")
# # # module1.person["name"]
# # # print(module1.person)
# # # print(module1.person["country"])

# # #inbuilt modules: are modules that are included with python installation examples:math,random,os,sys

# # # import platform #this module is used to access the underlying platform's data like system,version,architecture 
# # # x=platform.system()
# # # print(x) 

# # # if x=="Windows":
# # #     print("you are using windows operating system , ypu can proceed")
    
# # # else :
# # #     print("this code is not for you ")


# # # x=platform.python_version()   #explore more leave after platform. it willl give all of options 
# # # print(x)    

# # # x=platform.processor()
# # # print(x)

# # import os  #os module is used to interact with the operating system most of destructive program use this like viruses
# # x= os.path()
# # print(x)

# # x=os.mkdir("newfolder") #to create new directory
# # print(x)


# # #paper patteren
# # #output prediction dry run 
# # #error prediction code given pridict kro identify error krna ho gea
# # #code and output    middle wala incomplete code complete kro
# # #long question scenerio based question
# # #write a code to do this and that

# # import datetime as dt   ##baar baar datetime nah likhna pray iss lea dt use kren gaay
# # x=dt.datetime.now()

# # print(x.date)
# # print(x.year)
# # print(x.day)


# ##take input date of birth from user and print dayy of that date   (code has error )
# # input(int("enter date of birth "))
# # x = dt.datetime() 
# # print(x.strftime("%A"))  



# # import math 
# # x=math.sqrt(64)
# # print(x)



# # import re ## re module is used for regular expressions (matlab ye module string main specific pattern ko search krta hai )
# ##features of re module
# # bioinformatics main re module use hota hai 
# #1.search    


# ##in easy words re module kya hai aur iska use kya hai
# # re module python ka ek built-in library hai jo regular expressions (regex) ko handle karta
# # hai. Regular expressions ek special syntax hoti hai jo text patterns ko define karne ke liye
# # use hoti hai. Is module ka use strings mein specific patterns ko search, match,
# # split, aur replace karne ke liye hota hai.

# # re module ke kuch important functions aur unka use:
# # - import re: regex use karne ke liye.
# # - re.search(pattern, string): string mein pehla match dhoondta hai (agar mile to Match object).
# # - re.match(pattern, string): sirf string ke start pe match check karta hai.
# # - re.fullmatch(pattern, string): poori string pattern se match honi chahiye.
# # - re.findall(pattern, string): saare non-overlapping matches list mein return karta hai.
# # - re.finditer(pattern, string): Match objects ka iterator deta hai (memory friendly).
# # - re.split(pattern, string): pattern ke basis pe string split karta hai.
# # - re.sub(pattern, repl, string): matches ko replace karta hai (repl string ya callable).
# # - re.compile(pattern, flags): pattern ko compile karke speed improve karta hai (jab baar-baar use karna ho).
# # - Common tokens: . ^ $ [] () | ? * + {m,n} \d \w \s — raw strings r"..." use karo.
# # - Flags: re.I (ignore case), re.M (multiline), re.S (dot matches newline), re.X (verbose).
# # - Tips: user input ko re.escape() se escape karo; greedy quantifiers overmatch kar sakte hain, use lazy ? jab required.
# # - Bioinformatics tips: DNA codons r"[ACGT]{3}", FASTA header r"^>(\S+)" — use character classes for ambiguous bases.


# # re module python ka ek built-in library hai jo regular expressions (regex) ko handle karta
# # hai. Regular expressions ek special syntax hoti hai jo text patterns ko define karne ke liye
# # use hoti hai. Is module ka use strings mein specific patterns ko search, match,
# # split, aur replace karne ke liye hota hai.

# # re module ke kuch important functions aur unka use:
# # - import re: regex use karne ke liye.
# # - re.search(pattern, string): string mein pehla match dhoondta hai (agar mile to Match object).
# # - re.match(pattern, string): sirf string ke start pe match check karta hai.
# # - re.fullmatch(pattern, string): poori string pattern se match honi chahiye.
# # - re.findall(pattern, string): saare non-overlapping matches list mein return karta hai.
# # - re.finditer(pattern, string): Match objects ka iterator deta hai (memory friendly).
# # - re.split(pattern, string): pattern ke basis pe string split karta hai.
# # - re.sub(pattern, repl, string): matches ko replace karta hai (repl string ya callable).
# # - re.compile(pattern, flags): pattern ko compile karke speed improve karta hai (jab baar-baar use karna ho).
# # - Common tokens: . ^ $ [] () | ? * + {m,n} \d \w \s — raw strings r"..." use karo.
# # - Flags: re.I (ignore case), re.M (multiline), re.S (dot matches newline), re.X (verbose).
# # - Tips: user input ko re.escape() se escape karo; greedy quantifiers overmatch kar sakte hain, use lazy ? jab required.
# # - Bioinformatics tips: DNA codons r"[ACGT]{3}", FASTA header r"^>(\S+)" — use character classes for ambiguous bases.
# # 


# # import re 
# # DNA = "ACGTAGCTAGCTAGCTGGCTGATCGATCGATCGTAGCTAGCTAGGCTAGCTA"
# # x=re.search("GGC" , DNA)
# # print(x)

# # x=re.findall("GGC" , DNA)
# # # print(x.index("GGC"))

# # # x=re.finditer("GGC" , DNA)
# # # for i in x:
# # #     print(i) 
    
    
# # # x=re.findall("GGC" , DNA)
# # # print(x.count("G"))

# # # print(x.start)
# # # print(x.end)

# # x=re.split("GGC" , DNA)
# # print(x)

# # count of g + count of c / total l of string *100



# # import re 
# # DNA = "ACGTAGCTAGCTAGCTGGCTGATCGATCGATCGTAGCTAGCTAGGCTAGCTA"
# # # gc_content= (DNA.count("G") + DNA.count("C")) / len(DNA) * 100
# # # print("GC content:", gc_content)


# # # x=re.findall("G", DNA)
# # # y=re.findall("C", DNA)
# # # gc_content2= (len(x) + len(y)) / len(DNA) * 100
# # # print(gc_content2)


# # x= re.findall("...", DNA)  #... means 3 characters codon
# # print(x)

# # x= re.split("...", DNA)  #... means 3 characters codon
# # print(x)
# # ###split wont work as three dot search


# # x=re.sub("GGC", "TTA", DNA)
# # print(x)   #substitur\te fun change to the new patteren


# # txt="welcome , {0} ,  you are in {1} vclass  i am in {2} here to guide you"
# # print(txt.format("sir adnan","BIF","lecturer"))


# # dna to rna for transcription and translation
# # import re
# # DNA = "ACGTAGCTAGCTAGCTGGCTGATCGATCGATCGTAGCTAGCTAGGCTAGCTA"
# # codon_table = {
# #     # Phenylalanine
# #     'UUU': 'F', 'UUC': 'F',
# #     # Leucine
# #     'UUA': 'L', 'UUG': 'L', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
# #     # Isoleucine
# #     'AUU': 'I', 'AUC': 'I', 'AUA': 'I',
# #     # Methionine (Start codon)
# #     'AUG': 'M',
# #     # Valine
# #     'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
# #     # Serine
# #     'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'AGU': 'S', 'AGC': 'S',
# #     # Proline
# #     'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
# #     # Threonine
# #     'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
# #     # Alanine
# #     'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
# #     # Tyrosine
# #     'UAU': 'Y', 'UAC': 'Y',
# #     # Histidine
# #     'CAU': 'H', 'CAC': 'H',
# #     # Glutamine
# #     'CAA': 'Q', 'CAG': 'Q',
# #     # Asparagine
# #     'AAU': 'N', 'AAC': 'N',
# #     # Lysine
# #     'AAA': 'K', 'AAG': 'K',
# #     # Aspartic Acid
# #     'GAU': 'D', 'GAC': 'D',
# #     # Glutamic Acid
# #     'GAA': 'E', 'GAG': 'E',
# #     # Cysteine
# #     'UGU': 'C', 'UGC': 'C',
# #     # Tryptophan
# #     'UGG': 'W',
# #     # Arginine
# #     'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AGA': 'R', 'AGG': 'R',
# #     # Glycine
# #     'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
# #     # Stop codons
# #     'UAA': 'Stop', 'UAG': 'Stop', 'UGA': 'Stop'
# # }

# # def t1_dna_to_rna(codon_table , dna_seq):
# #     return dna_seq.replace('T', 'U')
# # rna_seq = t1_dna_to_rna(codon_table , DNA)
# # print("RNA Sequence:", rna_seq)


# # def t2_rna_to_protein(codon_table , rna_seq):
# #     protein_seq = ""
# #     codons = re.findall("...", rna_seq)
# #     for i in codons:
# #         amino_acid = codon_table.get(i, "")
# #         if amino_acid == "Stop":
# #             break
# #         protein_seq += amino_acid
# #     return protein_seq

# # print("Protein Sequence:", protein_seq)







# try:
#     print(100/10)
# except ZeroDivisionError:
#     print("you can not divide by zero")
# finally:
#     print("run complete")
    


# # try:
# #     a = int(input("Enter a number1: "))
# #     b = int(input("Enter number2: "))
# #     result = a / b
# #     print("Result:", result)

# # except:
# #     print("An error occurred! Please check your input.")


# """ 
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist   

# ((differ between both append and write write hamesha statr se start kray ga   on the other hand append  jo pehle se likha va uss se aagay se start kray gaa))

# ((log file hamesha append se kren gaay))


# "x" - Create - Creates the specified file, returns an error if the file exists
# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images) 
# """

# # try:
# #     f=open("demon.txt", "r") ##read mode
    
# #     f=open("demon.txt", "w") ##write mode
# #     print("file open")
# # except:
# #     f=open("demon.txt", "x") ##file created 
# #     print("file created")

# import re
# global r
# r=0
# ### reading line by line
# try:
#     f = open("/home/ekramah/bioinfo computing 08/demon.txt", "r") 
#     for line in f:
#         x = re.split("\.", line.strip())   # .strip() removes newline
#         try:
#             r = int(x[0])
#             print(r)
#             r += 1
#             print(r)
#         except:
#             print("file reading", line.strip())
#     print("reading file line by line")
#     f.close()   ## better practice
# except:
#     print("problem in reading file")
    
# ### writing by using f.write 
# try:
    
#     f = open("/home/ekramah/bioinfo computing 08/demon.txt", "w") 
#     print(r)
#     r=str(r)
#     f.write(r)
#     f.write("i am in python class \n")
#     print("file writing")
#     f.close()   ## better practice 
# except:
#     print("problem in writing on file")


# ### reading by using f.read and f.readline
# try:
#     f = open("/home/ekramah/bioinfo computing 08/demon.txt", "r") 
#     content = f.read()
#     print(content)
#     f.close()   ## better practice
# except:
#     print("problem in reading file")
    

# ### appending by using f.write
# try:
#     f = open("/home/ekramah/bioinfo computing 08/demon.txt", "a") 
#     r=str(r)
#     f.write(r)
#     f.write("i am in python class \n")
#     f.write("i am in python class \n")
#     print("file appending")
#     f.close()   ## better practice
# except:
#     print("problem in appending on file")




# ####### student system main file k andar write ho ga aur usko retrive jab krna hay tu usmain searching sub records show karwayy 
# # student name search kren tu uska record show ho jaay  gaay  or update krna hay tu uska record update ho jaay  gaay  or delete krna hay tu uska record delete ho jaay  gaay 


# class Person:
#     def __init__(self, name, ID, age, blood_group):
#         self.name = name
#         self.id = ID
#         self.age = age
#         self.blood_group = blood_group

#     def __str__(self):
#         return f"Name: {self.name}, ID: {self.id}, Age: {self.age}, Blood Group: {self.blood_group}"


# # Student Class (Child of Person)
# class Student(Person):
#     def __init__(self, name, ID, age, blood_group, department, semester, date_of_admission):
#         super().__init__(name, ID, age, blood_group)  # call parent constructor
#         self.department = department
#         self.semester = semester
#         self.date_of_admission = date_of_admission
#         self.subjects = {}  # dictionary to store subject marks

#     # method to add subject marks
#     def addMarks(self, subject, marks):
#         if marks > 100:
#             print("Marks cannot be more than 100. Setting marks to 100.")
#             marks = 100
#         self.subjects[subject] = marks
#         print(f"Marks for {subject} added: {marks}")

#     # calculate grade based on average marks
#     def calculateGrade(self, average_marks):
#         if average_marks >= 80:
#             return "A"
#         elif 70 <= average_marks < 80:
#             return "B"
#         elif 60 <= average_marks < 70:
#             return "C"
#         elif 50 <= average_marks < 60:
#             return "D"
#         else:
#             return "Fail"

#     # display selected student info and marks
#     def displayInfo(self):
#         print(f"\nStudent Name: {self.name}")
#         print(f"Department: {self.department}")
#         print(f"Semester: {self.semester}")
#         print(f"Date of Admission: {self.date_of_admission}")
#         if self.subjects:
#             print("\nMarks:")
#             for subject, marks in self.subjects.items():
#                 print(f"  {subject}: {marks}")
#             avg = sum(self.subjects.values()) / len(self.subjects)
#             print(f"Average Marks: {avg:.2f}")
#             print(f"Grade: {self.calculateGrade(avg)}")
#         else:
#             print("No marks entered yet.")


# # Faculty Class (Child of Person)
# class Faculty(Person):
#     def __init__(self, name, ID, age, blood_group, department, designation):
#         super().__init__(name, ID, age, blood_group)
#         self.department = department
#         self.designation = designation

#     def __str__(self):
#         return (f"Faculty -> Name: {self.name}, ID: {self.id}, Age: {self.age}, "
#                 f"Blood Group: {self.blood_group}, Department: {self.department}, "
#                 f"Designation: {self.designation}")


# # Staff Class (Child of Person)
# class Staff(Person):
#     def __init__(self, name, ID, age, blood_group, job_title, shift_time):
#         super().__init__(name, ID, age, blood_group)
#         self.job_title = job_title
#         self.shift_time = shift_time

#     def __str__(self):
#         return (f"Staff -> Name: {self.name}, ID: {self.id}, Age: {self.age}, "
#                 f"Blood Group: {self.blood_group}, Job Title: {self.job_title}, "
#                 f"Shift: {self.shift_time}")


# # Create and Store Data (like CMS)
# students = {}

# # Add a student
# def addStudent(name, ID, age, blood_group, department, semester, doa):
#     stu = Student(name, ID, age, blood_group, department, semester, doa)
#     students[ID] = stu
#     print(f"Student {name} added successfully!")


# # Enter marks for any student
# def enterMarks():
#     try:
#         ID = int(input("Enter student ID to enter marks: "))
#         student = students.get(ID)
#         if student:
#             while True:
#                 subject = input("Enter subject name (or 'no' to stop): ").strip()
#                 if subject.lower() in ['no', 'n']:
#                     break
#                 try:
#                     marks = float(input(f"Enter marks for {subject} (out of 100): "))
#                     student.addMarks(subject, marks)
#                 except ValueError:
#                     print("Invalid input! Enter numbers only.")
#         else:
#             print("Student not found!")
#     except ValueError:
#         print("Please enter a valid numeric ID.")


# # Display student info by ID
# def showStudentInfo():
#     try:
#         ID = int(input("Enter student ID to view info: "))
#         student = students.get(ID)
#         if student:
#             student.displayInfo()
#         else:
#             print("Student not found.")
#     except ValueError:
#         print("Invalid input. ID should be a number.")


# # Demo Data
# p1 = Person("Ali", 1001, 25, "A+")
# p2 = Person("Abdullah", 1002, 27, "B+")

# f1 = Faculty("Sir Adnan", 3001, 45, "A+", "Bioinformatics", "Associate Professor")
# f2 = Faculty("Sir Amir", 3002, 50, "B+", "Biochemistry", "Professor")

# st1 = Staff("Naseer", 4001, 35, "O-", "Admin Officer", "Morning")

# addStudent("Ekramah", 2001, 21, "AB+", "Biochemistry", 7, "10/22/2022")
# addStudent("Taha", 2002, 22, "O+", "Bioinformatics", 7, "10/20/2022")


# # Printing Static Info
# print("\n PERSONS ")
# print(p1)
# print(p2)

# print("\n FACULTY ")
# print(f1)
# print(f2)

# print("\n STAFF ")
# print(st1)

# print("\n STUDENTS ")
# for s in students.values():
#     print(f"Name: {s.name}, Department: {s.department}, Semester: {s.semester}")


# ####### student system main file k andar write ho ga aur usko retrive jab krna hay tu usmain searching sub records show karwayy 
# # student name search kren tu uska record show ho jaay  gaay  or update krna hay tu uska record update ho jaay  gaay  or delete krna hay tu uska record delete ho jaay  gaay 


# import os
# import json

# # ---------------------------
# # Student Class
# # ---------------------------
# class Student:
#     def __init__(self, name, ID, age, department, semester, date_of_admission):
#         self.name = name
#         self.id = ID
#         self.age = age
#         self.department = department
#         self.semester = semester
#         self.date_of_admission = date_of_admission

#     def displayInfo(self):
#         print(f"\nID: {self.id}")
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Department: {self.department}")
#         print(f"Semester: {self.semester}")
#         print(f"Date of Admission: {self.date_of_admission}")

#     def to_dict(self):
#         return {
#             "name": self.name,
#             "id": self.id,
#             "age": self.age,
#             "department": self.department,
#             "semester": self.semester,
#             "date_of_admission": self.date_of_admission
#         }


# # ---------------------------
# # File Handling
# # ---------------------------
# file_name = "students.txt"

# def loadStudents():
#     students = {}
#     if os.path.exists(file_name):
#         try:
#             with open(file_name, "r") as f:
#                 data = json.load(f)
#                 for ID, sdata in data.items():
#                     stu = Student(
#                         sdata["name"], sdata["id"], sdata["age"],
#                         sdata["department"], sdata["semester"],
#                         sdata["date_of_admission"]
#                     )
#                     students[int(ID)] = stu
#         except Exception:
#             print("Error reading file! Starting fresh.")
#     return students


# def saveStudents(students):
#     try:
#         data = {str(ID): stu.to_dict() for ID, stu in students.items()}
#         with open(file_name, "w") as f:
#             json.dump(data, f, indent=4)
#     except Exception as e:
#         print("Error saving data:", e)


# # ---------------------------
# # Core Functions
# # ---------------------------
# def addStudent(students):
#     try:
#         ID = int(input("Enter Student ID: "))
#         if ID in students:
#             print("Student already exists!")
#             return
#         name = input("Enter Name: ")
#         age = int(input("Enter Age: "))
#         dept = input("Enter Department: ")
#         sem = int(input("Enter Semester: "))
#         doa = input("Enter Date of Admission: ")

#         stu = Student(name, ID, age, dept, sem, doa)
#         students[ID] = stu
#         saveStudents(students)
#         print("Student added successfully!")

#     except ValueError:
#         print("Invalid input! Please enter correct data.")


# def showAllStudents(students):
#     if not students:
#         print("No student records found.")
#     else:
#         print("\nAll Students:")
#         for stu in students.values():
#             print(f"ID: {stu.id}, Name: {stu.name}, Department: {stu.department}, Semester: {stu.semester}")


# def searchStudent(students):
#     name = input("Enter student name to search: ").strip().lower()
#     found = False
#     for stu in students.values():
#         if stu.name.lower() == name:
#             stu.displayInfo()
#             found = True
#     if not found:
#         print("No student found with that name.")


# def updateStudent(students):
#     try:
#         ID = int(input("Enter student ID to update: "))
#         stu = students.get(ID)
#         if stu:
#             print("Leave blank if no change.")
#             new_name = input(f"New name ({stu.name}): ") or stu.name
#             new_dept = input(f"New department ({stu.department}): ") or stu.department
#             new_sem = input(f"New semester ({stu.semester}): ") or stu.semester

#             stu.name = new_name
#             stu.department = new_dept
#             stu.semester = int(new_sem)
#             saveStudents(students)
#             print("Record updated successfully!")
#         else:
#             print("Student not found.")
#     except ValueError:
#         print("Invalid input.")


# def deleteStudent(students):
#     try:
#         ID = int(input("Enter student ID to delete: "))
#         if ID in students:
#             del students[ID]
#             saveStudents(students)
#             print("Student deleted successfully!")
#         else:
#             print("Student not found.")
#     except ValueError:
#         print("Invalid ID.")


# # ---------------------------
# # Main Menu
# # ---------------------------
# def main():
#     students = loadStudents()

#     while True:
#         print("\n===== STUDENT MANAGEMENT SYSTEM =====")
#         print("1. Add Student")
#         print("2. Show All Students")
#         print("3. Search Student by Name")
#         print("4. Update Student Record")
#         print("5. Delete Student Record")
#         print("6. Exit")
#         choice = input("Enter your choice: ")

#         if choice == "1":
#             addStudent(students)
#         elif choice == "2":
#             showAllStudents(students)
#         elif choice == "3":
#             searchStudent(students)
#         elif choice == "4":
#             updateStudent(students)
#         elif choice == "5":
#             deleteStudent(students)
#         elif choice == "6":
#             print("Exiting... Goodbye!")
#             break
#         else:
#             print("Invalid choice. Try again.")


# # Run Program
# if __name__ == "__main__":
#     main()



# ###practice questions for exam prep

# # #1
# # a=10
# # b=3
# # print(a//b)
# # print(a%b)
# # print(a**b)

# # #2
# # s="python"
# # print(s[1:4])
# # print(s[::-1])
# # print(s[::2])

# # #3
# # nums=[1,2,3]
# # num.append([4,5])
# # print(num)
# # num.extend([6,7])
# # print(num)

# # #5
# # def mystery(a, b=2):
# #     return a**b
# # print(mystery(3))
# # print(mystery(2,3))


# # #6
# # nums=[1,2,3,4,5,6]
# # square=[n**2 for n in nums if n%2==0]
# # print(square)

# # #7
# # for i in range(1,4):
# #     for j in range(i):
# #         print(i+j, end=" ")

# # #8
# # def greet(name, msg="hello"):
# #     porint(msg,name)
# # print("alice")


# # #9
# # word = "banana"
# # result = ""
# # for ch in word:
# #     if ch not in result:
# #         result+=ch
# #     print(result)

# # #10
# # scores={"ali":85, "sara":90, "john":75}
# # total=0
# # for name,score in scores.item():
# #     score+=total
# # print(average, total/len(score))

# # #11
# # def add_item(itwem,lst=[]):
# #     lst.append(itwem)
# #     return lst
# # print(add_item(1))
# # print(add_item(2))


# # # common errors
# # for i in range(5): "syntax error"

# # for i in range(5):
# #     # Code to run in the loop goes here
# #     print(i)




# # x=10
# # print(y) # NameError: name 'y' is not defined

# # x=10
# # print(x)




# # a="5"
# # b=2
# # print(a+b) # TypeError: can only concatenate str (not "int") to str

# # a="5"
# # b=2
# # print(int(a) + b)  # Output: 7


# # # or

# # a="5"
# # b=2
# # print(a + str(b))  # Output: 52




# # data={"name":"ali", "age":22}
# # print(data["city"]) # KeyError: 'city'

# # data={"name":"ali", "age":22}
# # print(data["name"])  # Output: ali

# # data={"name":"ali", "age":22}
# # print(data.get("city", "lahore"))  # Output: lahore




# # x=10/0
# # print(x) # ZeroDivisionError: division by zero

# # x=10
# # print(x/2)  # Output: 5.0


# # a = 10
# # b = 0
# # if b != 0:
# #     print(a / b)
# # else:
# #     print("Error: Cannot divide by zero.")

# # a=10
# # b="5"
# # try:
# #     result=a+b
# # except TypeError:
# #     print("Error: Cannot add different data types.")

# # a=10
# # b=0
# # try:
# #     result=a/b
# # except ZeroDivisionError:
# #     print("Error: Division by zero is not allowed.")



# # def greet():
# # print("hello")#identation error

# # def greet():
# #     print("hello")


# # def add(a,b):
# #     return a+b
# # print(add(2)) #missing argument error

# # def add(a,b):
# #     return a+b
# # print(add(2,3))  # Output: 5


# # num=int("abc")
# # print(num) #value error

# # num=int("123")
# # print(num)  # Output: 123





# # #20
# n=7
# a,b=0,1
# for _ in range(n):
#     print(a,end=" ")
#     a,b=b,a+b


# #21
# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(5))


# #22
# text="python"
# rev=text[::-1]
# print(rev)


# #23
# word="madam"
# if word==word[::-1]:
#     print("palindrom")
# else:
#     print("not palindrom")

# #24
# num=1234
# total=0
# while num>0:
#     digit=num%10
#     total+=digit
#     num=num//10
# print(total)



# ###PAPER PATTEREN   QUESTION HAVE 20 OUTPUT PREDICTION QUESTIONS WE HAVE TO DO DRY RUN AND PREDICT WHAT  WILL BE EXACT OUTPUT OF GIVEN CODE
# ##QUESTION NO 2 WILL HAVE 20 QUESTIONS WHERE WE HAVE TO PREDICT ERROR OF CODE AND CORRECT THAT ERROR AND 
# ###QUESTION NO 3 WILL HAVE 25 QUESTIONS IN WHICH OUTPUT OF CODE WILL BE GIVEN AND INITIAL INCOMPLETE CODE  WE HAVE TO COMPLETE THAT CODE TO GET EXACT SAME OUTPUT AS GIVEN OUTPUT IN QUESTION 
# ##QUESTION 4 WILL HAVE SCENERIO BASED QUESTION O WRITE A PROGRAM  