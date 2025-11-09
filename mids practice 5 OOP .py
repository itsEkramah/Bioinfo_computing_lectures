Topic 5: Object-Oriented Programming (OOP)
🎯 Learning Goals

By the end of this topic, you should confidently handle:

Class and Object creation

__init__() constructor and self

Instance vs Class variables

Methods (normal, classmethod, staticmethod)

Inheritance (single, multiple, multilevel)

Method overriding

The super() function

__str__() (string representation)

Real-world examples (student info, DNA sequence class, etc.)

🧠 1️⃣ What is OOP?

OOP = Object-Oriented Programming — organizes code using classes and objects.

Class → Blueprint
Object → Instance of that blueprint

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Creating object
s1 = Student("Ekramah", 22)
s1.show()



The __init__() Constructor

Automatically runs when an object is created.
Used to initialize attributes.

class Gene:
    def __init__(self, name, length):
        self.name = name
        self.length = length


The self Keyword

self represents the current object.
All instance variables must use self. prefix.

name = name  Wrong
self.name = name  Correct

Instance vs Class Variables


class Protein:
    species = "Human"       # class variable
    def __init__(self, name):
        self.name = name    # instance variable
Class variable → Shared by all objects

Instance variable → Unique per object

Instance Methods

Operate on instance data. Always have self as first parameter.

def display(self):
    print(self.name)


Class Methods & Static Methods
🔹 @classmethod

Works with class, not instance.

class Example:
    count = 0
    @classmethod
    def show_count(cls):
        print(cls.count)


@staticmethod

Independent of both class and instance.

class Math:
    @staticmethod
    def add(a, b):
        return a + b



Inheritance (Reusability of Code)
🔹 Single Inheritance

class Parent:
    def speak(self):
        print("Parent speaking")

class Child(Parent):
    def play(self):
        print("Child playing")

obj = Child()
obj.speak()
obj.play()


🔹 Multi-Level Inheritance

class A:
    def f1(self):
        print("A")

class B(A):
    def f2(self):
        print("B")

class C(B):
    def f3(self):
        print("C")

C().f1()


🔹 Multiple Inheritance

class A:
    def show(self):
        print("From A")

class B:
    def show(self):
        print("From B")

class C(A, B):
    pass

C().show()


The super() Function

Used to call parent methods or constructors.

class Parent:
    def __init__(self):
        print("Parent init")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child init")

Child()


The __str__() Method

Used for readable string representation of objects.


class Gene:
    def __init__(self, name, length):
        self.name = name
        self.length = length

    def __str__(self):
        return f"Gene: {self.name}, Length: {self.length}"

print(Gene("TP53", 1500))


Gene Class

class DNA:
    def __init__(self, seq):
        self.seq = seq

    def gc_content(self):
        g = self.seq.count("G")
        c = self.seq.count("C")
        return (g + c) / len(self.seq) * 100

    def reverse(self):
        return self.seq[::-1]
