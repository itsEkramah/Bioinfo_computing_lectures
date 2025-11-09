"""# Topic 5: Object-Oriented Programming (OOP)
# 🎯 Learning Goals

# By the end of this topic, you should confidently handle:

# Class and Object creation

# __init__() constructor and self

# Instance vs Class variables

# Methods (normal, classmethod, staticmethod)

# Inheritance (single, multiple, multilevel)

# Method overriding

# The super() function

# __str__() (string representation)

# Real-world examples (student info, DNA sequence class, etc.)

# 🧠 1️⃣ What is OOP?

# OOP = Object-Oriented Programming — organizes code using classes and objects.

# Class → Blueprint
# Object → Instance of that blueprint

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show(self):
#         print(f"Name: {self.name}, Age: {self.age}")

# # Creating object
# s1 = Student("Ekramah", 22)
# s1.show()



# The __init__() Constructor

# Automatically runs when an object is created.
# Used to initialize attributes.

# class Gene:
#     def __init__(self, name, length):
#         self.name = name
#         self.length = length


# The self Keyword

# self represents the current object.
# All instance variables must use self. prefix.

# name = name  Wrong
# self.name = name  Correct

# Instance vs Class Variables


# class Protein:
#     species = "Human"       # class variable
#     def __init__(self, name):
#         self.name = name    # instance variable
# Class variable → Shared by all objects

# Instance variable → Unique per object

# Instance Methods

# Operate on instance data. Always have self as first parameter.

# def display(self):
#     print(self.name)


# Class Methods & Static Methods
# 🔹 @classmethod

# Works with class, not instance.

# class Example:
#     count = 0
#     @classmethod
#     def show_count(cls):
#         print(cls.count)


# @staticmethod

# Independent of both class and instance.

# class Math:
#     @staticmethod
#     def add(a, b):
#         return a + b



# Inheritance (Reusability of Code)
# 🔹 Single Inheritance

# class Parent:
#     def speak(self):
#         print("Parent speaking")

# class Child(Parent):
#     def play(self):
#         print("Child playing")

# obj = Child()
# obj.speak()
# obj.play()


# 🔹 Multi-Level Inheritance

# class A:
#     def f1(self):
#         print("A")

# class B(A):
#     def f2(self):
#         print("B")

# class C(B):
#     def f3(self):
#         print("C")

# C().f1()


# 🔹 Multiple Inheritance

# class A:
#     def show(self):
#         print("From A")

# class B:
#     def show(self):
#         print("From B")

# class C(A, B):
#     pass

# C().show()


# The super() Function

# Used to call parent methods or constructors.

# class Parent:
#     def __init__(self):
#         print("Parent init")

# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         print("Child init")

# Child()


# The __str__() Method

# Used for readable string representation of objects.


# class Gene:
#     def __init__(self, name, length):
#         self.name = name
#         self.length = length

#     def __str__(self):
#         return f"Gene: {self.name}, Length: {self.length}"

# print(Gene("TP53", 1500))


# Gene Class

# class DNA:
#     def __init__(self, seq):
#         self.seq = seq

#     def gc_content(self):
#         g = self.seq.count("G")
#         c = self.seq.count("C")
#         return (g + c) / len(self.seq) * 100

#     def reverse(self):
#         return self.seq[::-1]
"""


# PYTHON OOP — FULL EXAM SIMULATION (33 QUESTIONS)
# 🧮 SECTION 1 — OUTPUT PREDICTION (10 Questions)

# Dry-run each program and predict exact output.


# class Student:
#     def __init__(self, name):
#         self.name = name

# s = Student("Ekramah")
# print(s.name)
# ##Ekramah

# class A:
#     def greet(self):
#         print("Hello")

# obj = A()
# obj.greet()

# ##Hello

# class A:
#     def __init__(self):
#         print("A init")

# class B(A):
#     def __init__(self):
#         super().__init__()
#         print("B init")

# B()
# ##A init
# ##B init




# class Gene:
#     def __init__(self, name, length):
#         self.name = name
#         self.length = length

#     def __str__(self):
#         return f"{self.name} ({self.length}bp)"

# g = Gene("TP53", 1500)
# print(g)

# ##TP53 1500bp


# class A:
#     def f1(self):
#         print("A")

# class B(A):
#     def f1(self):
#         print("B")

# b = B()
# b.f1()

# ##B



# class X:
#     def __init__(self):
#         self.value = 10

#     def double(self):
#         self.value *= 2

# x1 = X()
# x1.double()
# print(x1.value)


# ##20



# class A:
#     def show(self):
#         print("From A")

# class B(A):
#     pass

# class C(B):
#     pass

# C().show()

# ##Form A 

class A:
    species = "Human"

    def __init__(self, name):
        self.name = name

a1 = A("Ali")
a2 = A("Zara")

A.species = "Homo sapiens"
print(a1.species, a2.species)

# Homo sapiens Homo sapiens



class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

a = Counter()
b = Counter()
print(Counter.count)
