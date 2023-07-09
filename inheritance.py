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

        Developer.num_emps += 1

    def info(self):
        return "{} {}".format(self.age, self.location)

    def apply_raise(self):
        # applying raise amount to employee
        self.pay = self.pay * self.raise_amount


# creating developer class that inherit Employee class
class Developer(Employee):
    # setting different raise amount for developer
    raise_amount = 1.10

    # adding parametre for developer only thats pro_lang
    def __init__(self, first, last, pay, age, location, pro_lang):
        super().__init__(first, last, pay, age, location)
        self.pro_lang = pro_lang


# manager class that also inherit employee but has some priority
class Manager(Employee):
    def __init__(self, first, last, pay, age, location, employees=None):
        super().__init__(first, last, pay, age, location)
        # creating list for employees
        if employees is None:
            self.employees = []
        else:
            self.employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print("-->" + emp.fullname)


# creating the list of developer
dev_1 = Developer("jonh", "marbel", 15000, 28, "Lagos", "python")
dev_2 = Developer("keen", "samuel", 12000, 34, "Abuja", "java")
dev_3 = Developer("machael", "jack", 16000, 28, "Borno", "python")
dev_4 = Developer("mark", "zukack", 18000, 31, "Bauchi", "javaScript")


print(dev_2.pay)
dev_2.apply_raise()
print(dev_2.pay)

# printing language of developer
print(dev_1.pro_lang)

# creating manager to manage employees
mgr = Manager("Abdullahi", "Bappaji", 50000, "Gombe", "Python")
print(mgr.fullname)
print(mgr.email)

# adding employees
mgr.add_emp(dev_1)
mgr.add_emp(dev_2)
mgr.add_emp(dev_3)
mgr.add_emp(dev_4)

# print the list of employees for the manager
mgr.print_emp()

# remove employee and check the list
mgr.remove_emp(dev_2)
mgr.print_emp()
