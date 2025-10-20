# ###class is a blueprint for creating objects 
# ##it defines a set of attributes and methods that the created objects will have.


# class Student(Person): #person class se inherit kr rha
    
# # #init method is a constructor that is called when an object is created from the class 
# # # and it allows the class to initialize the attributes of the class.
# ## simple wording main init constructor hai jo object create krte hi call hota hai aur attributes ko initialize krta hai
    
#     def __init__(self, Name, ID, Age, Blood_Group, Department, Semester, GPA): #s
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
#         self.salary = Salary

#     def __str__(self):
#         return (f"Faculty -> Name: {self.name}, ID: {self.id}, Age: {self.age}, "
#                 f"Blood Group: {self.blood_group}, Dept: {self.dept}, Designation: {self.designation}, Salary: {self.salary}")



# p1 = Person("AAAA", 123, 24, "B+")
# p2 = Person("BBBB", 124, 22, "O+")

# s1 = Student("Ekramah", 567, 21, "AB+", "Biochemistry", 5, 3.8)

# f1 = Faculty("SIR Adnan", 789, 45, "A+", "Biochemistry", "Associate Professor", 120000)


# print(p1)
# print(p2)
# print(s1)
# print(f1)

#
## USING OOP AND INHERITENCE CONCEPTS ASSIGNMENT QAU CMS BY USING INHERITANCE OBJECTS OF FACULTY MEMBERS STAFF AND STUDENTS  INFORMATION 