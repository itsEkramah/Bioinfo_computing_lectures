###class is a blueprint for creating objects 
##it defines a set of attributes and methods that the created objects will have.

class computer :

##this is a method(function inside class)   

    def config(self): #self is used to refer to the current object
        print("i5 , 16gb , 1TB")
        
#create objects c1 and c2
c1=computer() 
c2=computer()

#use methods using objects
computer.config(c1)
computer.config(c2)

# ##another way to call method
c1.config()
c2.config()






##objet is a instance of a class 
##c1 and c2 are objects of class computer

class computer :
    def __init__(self, cpu, ram): #constructor to initialize attributes (cpu and ram are objects)
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("Config is", self.cpu, self.ram) ##jab bhi object ko acess krna ho tu self use krna hota hai

c1 = computer('i5', "16GB")
c2 = computer('Ryzen 5', '8GB')

c1.config()
c2.config()


# #init method is a constructor that is called when an object is created from the class 
# # and it allows the class to initialize the attributes of the class.
## simple wording main init constructor hai jo object create krte hi call hota hai aur attributes ko initialize krta hai


###create a class named car with 2 attributes and 1 method to display the attributes
class car :
    wheels = 4  #class attribute
    
    def __init__(self, make, model): #instance attributes
        self.make = make
        self.model = model
    def display(self):
        print("Car make:", self.make)
        print("Car model:", self.model)
        print("Number of wheels:", car.wheels)
c1 = car("Toyota", "Camry")
c1.display()


