# try:
#     # Code that may raise an exception
# except:
#     # Code that runs if an exception occurs



# try:
#     a = int(input("Enter a number1: "))
#     b = int(input("Enter number2: "))
#     result = a / b
#     print("Result:", result)

# except:
#     print("An error occurred! Please check your input.")




# try:
#     x = int(input("Enter 1st number : "))
#     y = int(input("Enter 2nd number: "))
#     print("Result:", x / y)

# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed.")

# except ValueError:
#     print("Error: Please enter valid integers.")

# try:
#     num = int(input("Enter a number: "))
#     print("Reciprocal is:", 1 / num)

# except ZeroDivisionError:
#     print("Cannot divide by zero!")

# except ValueError:
#     print("That’s not a valid number.")

# else:
#     print("No exceptions occurred!")   # Runs only if no error

# finally:
#     print("Execution complete.")       # Runs always (even if an error)





# try:
#     with open("data.txt", "r") as file:
#         content = file.read()
#         print(content)

# except FileNotFoundError:
#     print("Error: File not found. Please check the filename.")
# ##Use Case: In bioinformatics pipelines (e.g., reading FASTA or CSV files), 
# # #this prevents crashes if a file path is missing or misnamed.





""" 
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images) 
"""


try:
    f=open(" /home/ekramah/bioinfo computing 08/demo.txt","r")
except FileNotFoundError:
    f=open(" /home/ekramah/bioinfo computing 08/demo.txt","x")
    f=open(" /home/ekramah/bioinfo computing 08/demo.txt","r")
except:
    print("Permission's error.")

import os
os.remove("  /home/ekramah/bioinfo computing 08/demo.txt")
try:
    f=open("  /home/ekramah/bioinfo computing 08/demo.txt","a")
except:
    print("Permission's error.")
    
f.write("File handling in python.\n")
f.close()

try:
    f=open(" /home/ekramah/bioinfo computing 08/demo.txt","r")
except FileNotFoundError:
    f=open("/home/ekramah/bioinfo computing 08/demo.txt","x")
    f=open("/home/ekramah/bioinfo computing 08/demo.txt","r")
except:
    print("Permission's error.")
#print(f.read())
for x in f.readlines():
    print(x)
f.close()