class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self): #this is a method
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return f"Employee({self.first}, {self.last}, {self.pay})" 

    def __str__(self):
        return f"{self.fullname()} - {self.email}"

emp_1 = Employee("Yiannis", "Konstantinou", 200000)
emp_2 = Employee("Test", "User", 50000)

print(emp_1)

print(repr(emp_1))
print(str(emp_1))

print(emp_1.__repr__())
print(emp_1.__str__())