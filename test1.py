# find odd and even usig functions

n = int(input("enter a number: "))
def odd_num(n):
    if n % 2 != 0:
        return f"{n} is odd number"
    else:
        return f"{n} is even number"
print(odd_num(n))

##calculator having 4 functions
class calculator:
    def __init__(self):
        self.n1 = float(input("enter first number: "))
        self.n2 = float(input("enter second number: "))
    def add(self):
        return self.n1 + self.n2
    def subs(self):
        return self.n1 - self.n2
    def multi(self):
        return self.n1 * self.n2
    def div(self):
        return self.n1 / self.n2

calc = calculator()
print("addition:", calc.add())
print("subtraction:", calc.subs())
print("multiplication:", calc.multi())
print("division:", calc.div())