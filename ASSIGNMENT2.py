class Person:
    def __init__(self, name, ID, age, blood_group):
        self.name = name
        self.id = ID
        self.age = age
        self.blood_group = blood_group

    def __str__(self):
        return f"Name: {self.name}, ID: {self.id}, Age: {self.age}, Blood Group: {self.blood_group}"


# Student Class (Child of Person)
class Student(Person):
    def __init__(self, name, ID, age, blood_group, department, semester, date_of_admission):
        super().__init__(name, ID, age, blood_group)  # call parent constructor
        self.department = department
        self.semester = semester
        self.date_of_admission = date_of_admission
        self.subjects = {}  # dictionary to store subject marks

    # method to add subject marks
    def addMarks(self, subject, marks):
        if marks > 100:
            print("Marks cannot be more than 100. Setting marks to 100.")
            marks = 100
        self.subjects[subject] = marks
        print(f"Marks for {subject} added: {marks}")

    # calculate grade based on average marks
    def calculateGrade(self, average_marks):
        if average_marks >= 80:
            return "A"
        elif 70 <= average_marks < 80:
            return "B"
        elif 60 <= average_marks < 70:
            return "C"
        elif 50 <= average_marks < 60:
            return "D"
        else:
            return "Fail"

    # display selected student info and marks
    def displayInfo(self):
        print(f"\nStudent Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Semester: {self.semester}")
        print(f"Date of Admission: {self.date_of_admission}")
        if self.subjects:
            print("\nMarks:")
            for subject, marks in self.subjects.items():
                print(f"  {subject}: {marks}")
            avg = sum(self.subjects.values()) / len(self.subjects)
            print(f"Average Marks: {avg:.2f}")
            print(f"Grade: {self.calculateGrade(avg)}")
        else:
            print("No marks entered yet.")


# Faculty Class (Child of Person)
class Faculty(Person):
    def __init__(self, name, ID, age, blood_group, department, designation):
        super().__init__(name, ID, age, blood_group)
        self.department = department
        self.designation = designation

    def __str__(self):
        return (f"Faculty -> Name: {self.name}, ID: {self.id}, Age: {self.age}, "
                f"Blood Group: {self.blood_group}, Department: {self.department}, "
                f"Designation: {self.designation}")


# Staff Class (Child of Person)
class Staff(Person):
    def __init__(self, name, ID, age, blood_group, job_title, shift_time):
        super().__init__(name, ID, age, blood_group)
        self.job_title = job_title
        self.shift_time = shift_time

    def __str__(self):
        return (f"Staff -> Name: {self.name}, ID: {self.id}, Age: {self.age}, "
                f"Blood Group: {self.blood_group}, Job Title: {self.job_title}, "
                f"Shift: {self.shift_time}")


# Create and Store Data (like CMS)
students = {}

# Add a student
def addStudent(name, ID, age, blood_group, department, semester, doa):
    stu = Student(name, ID, age, blood_group, department, semester, doa)
    students[ID] = stu
    print(f"Student {name} added successfully!")


# Enter marks for any student
def enterMarks():
    try:
        ID = int(input("Enter student ID to enter marks: "))
        student = students.get(ID)
        if student:
            while True:
                subject = input("Enter subject name (or 'no' to stop): ").strip()
                if subject.lower() in ['no', 'n']:
                    break
                try:
                    marks = float(input(f"Enter marks for {subject} (out of 100): "))
                    student.addMarks(subject, marks)
                except ValueError:
                    print("Invalid input! Enter numbers only.")
        else:
            print("Student not found!")
    except ValueError:
        print("Please enter a valid numeric ID.")


# Display student info by ID
def showStudentInfo():
    try:
        ID = int(input("Enter student ID to view info: "))
        student = students.get(ID)
        if student:
            student.displayInfo()
        else:
            print("Student not found.")
    except ValueError:
        print("Invalid input. ID should be a number.")


# Demo Data
p1 = Person("Ali", 1001, 25, "A+")
p2 = Person("Abdullah", 1002, 27, "B+")

f1 = Faculty("Sir Adnan", 3001, 45, "A+", "Bioinformatics", "Associate Professor")
f2 = Faculty("Sir Amir", 3002, 50, "B+", "Biochemistry", "Professor")

st1 = Staff("Naseer", 4001, 35, "O-", "Admin Officer", "Morning")

addStudent("Ekramah", 2001, 21, "AB+", "Biochemistry", 7, "10/22/2022")
addStudent("Taha", 2002, 22, "O+", "Bioinformatics", 7, "10/20/2022")


# Printing Static Info
print("\n PERSONS ")
print(p1)
print(p2)

print("\n FACULTY ")
print(f1)
print(f2)

print("\n STAFF ")
print(st1)

print("\n STUDENTS ")
for s in students.values():
    print(f"Name: {s.name}, Department: {s.department}, Semester: {s.semester}")

