
# try:
#     a = int(input("Enter a number1: "))
#     b = int(input("Enter number2: "))
#     result = a / b
#     print("Result:", result)

# except:
#     print("An error occurred! Please check your input.")


""" 
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist   

((differ between both append and write write hamesha statr se start kray ga   on the other hand append  jo pehle se likha va uss se aagay se start kray gaa))

((log file hamesha append se kren gaay))


"x" - Create - Creates the specified file, returns an error if the file exists
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images) 
"""

# try:
#     f=open("demon.txt", "r") ##read mode
    
#     f=open("demon.txt", "w") ##write mode
#     print("file open")
# except:
#     f=open("demon.txt", "x") ##file created 
#     print("file created")

import re
global r
r=0
### reading line by line
try:
    f = open("/home/ekramah/bioinfo computing 08/demon.txt", "r") 
    for line in f:
        x = re.split("\.", line.strip())   # .strip() removes newline
        try:
            r = int(x[0])
            print(r)
            r += 1
            print(r)
        except:
            print("file reading", line.strip())
    print("reading file line by line")
    f.close()   ## better practice
except:
    print("problem in reading file")
    
### writing by using f.write 
try:
    
    f = open("/home/ekramah/bioinfo computing 08/demon.txt", "w") 
    print(r)
    r=str(r)
    f.write(r)
    f.write("i am in python class \n")
    print("file writing")
    f.close()   ## better practice 
except:
    print("problem in writing on file")


### reading by using f.read and f.readline
try:
    f = open("/home/ekramah/bioinfo computing 08/demon.txt", "r") 
    content = f.read()
    print(content)
    f.close()   ## better practice
except:
    print("problem in reading file")
    

### appending by using f.write
try:
    f = open("/home/ekramah/bioinfo computing 08/demon.txt", "a") 
    r=str(r)
    f.write(r)
    f.write("i am in python class \n")
    f.write("i am in python class \n")
    print("file appending")
    f.close()   ## better practice
except:
    print("problem in appending on file")




####### student system main file k andar write ho ga aur usko retrive jab krna hay tu usmain searching sub records show karwayy 
# student name search kren tu uska record show ho jaay  gaay  or update krna hay tu uska record update ho jaay  gaay  or delete krna hay tu uska record delete ho jaay  gaay 