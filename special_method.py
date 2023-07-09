class Employee:
    raise_amount = 1.04
    num_emps = 0

    def __init__(self, first, last, pay, age, location):
        self.first = first
        self.last = last
        self.pay = pay
        self.fullname = first + " " + last
        self.email = first + "." + last + "@gmail.com"
        self.age = age
        self.location = location

        Employee.num_emps += 1

    def info(self):
        return "{} {}".format(self.age, self.location)

    def apply_raise(self):
        # applying raise amount to employee
        self.pay = self.pay * self.raise_amount

    # dundar method for representation
    def __repr__(self):
        return "Employee('{} , {}' , {})".format(self.first, self.last, self.pay)

    # dundar method for display output string
    def __str__(self):
        return "{} - {}".format(self.fullname, self.email)
    
    #checking dundar addition for salary of empoyees
    def __add__(self, other):
        return self.pay + other.pay
    
    #dunder method for lentgh of fullname
    def __len__(self):
        return len(self.fullname)


emp_1 = Employee("jonh", "marbel", 15000, 28, "Lagos")
emp_2 = Employee("keen", "samuel", 12000, 34, "Abuja")

# printing the representation and string of employee
print(repr(emp_1))
print(str(emp_1))

# All the same as above
print(emp_1.__repr__())
print(emp_1.__str__())

#using dundar method to add employees salary
print(emp_1 + emp_2)

#checking dunder len method
print(len(emp_1))