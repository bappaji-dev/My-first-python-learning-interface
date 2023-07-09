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

    # class method that use as class variable for all instances
    @classmethod
    def set_rs_amnt(cls, amount):
        # set the raise amount for the class method of class var
        cls.raise_amount = amount

    # Alternative method for creating new employee
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay, age, location = emp_str.split("-")
        return cls(first, last, pay, age, location)

    # static method is a method that if we do not access the class or instaces
    @staticmethod
    def is_workday(day):
        # checking wether the day is week day
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee("jonh", "marbel", 15000, 28, "Lagos")
emp_2 = Employee("keen", "samuel", 12000, 34, "Abuja")


print(emp_1.email)
print(emp_1.fullname.upper())
print(emp_1.pay)

print(emp_2.email)
print(emp_2.fullname.upper())
print(emp_2.pay)

print(emp_1.info())
print(emp_2.info())

print(Employee.info(emp_1))

# set raise amount for the class method
Employee.set_rs_amnt(1.05)
print(Employee.raise_amount)
print(emp_1.raise_amount)

emp_1.apply_raise()
emp_2.apply_raise()
print(emp_1.pay)
print(emp_2.pay)
print(Employee.num_emps)

# creating new employee with our alternative class method
emp_3 = "yakubu-audu-20000-23-Gombe"
new_emp = Employee.from_string(emp_3)
print(new_emp.fullname)
print(new_emp.pay)

# using the datetime method to check the work day
import datetime

my_date = datetime.date(2023, 7, 6)
print(Employee.is_workday(my_date))
