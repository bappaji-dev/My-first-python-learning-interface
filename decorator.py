class Employee:
    raise_amount = 1.04
    num_emps = 0

    def __init__(self, first, last, pay, age, location):
        self.first = first
        self.last = last
        self.pay = pay
        self.age = age
        self.location = location

        Employee.num_emps += 1

    def info(self):
        return "{} {}".format(self.age, self.location)

    def apply_raise(self):
        # applying raise amount to employee
        self.pay = self.pay * self.raise_amount

    # creating fullname for employees with decorator
    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    # creating decoration for email,i.e defining it as method and accessing it as attribute
    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.first, self.last)
    
    #applying setter to our method so that we ca change the value of the fullname(method)
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    #setting deleter for fullname
    @fullname.deleter
    def fullname(self):
        print("Deleted name!")
        self.first = None
        self.last = None


emp_1 = Employee("jonh", "marbel", 15000, 28, "Lagos")
emp_2 = Employee("keen", "samuel", 12000, 34, "Abuja")

# changing first for employee, i.e changing value for attribute
emp_1.first = "harold"

#setting name for method fuulname
emp_2.fullname = "Abdullahi Bappaji"

# printing employee after changing the first name
print(emp_1.fullname)
print(emp_1.email)

#printing employee after changing fullname through fullname(method)
print(emp_2.fullname)
print(emp_2.email)

#checking deleter
del emp_1.fullname