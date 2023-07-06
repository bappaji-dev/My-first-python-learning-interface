class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.fullname = first + " " + last
        self.email = first + "." + last + "@gmail.com"

    


emp_1 = Employee("jonh", "marbel", 15000)
emp_2 = Employee("keen", "samuel", 12000)


print(emp_1.email)
print(emp_1.fullname.upper())
print(emp_1.pay)

print(emp_2.email)
print(emp_2.fullname.upper())
print(emp_2.pay)
