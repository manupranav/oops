class Employee: 

    raise_amt = 1.04
    
    def __init__(self,first, last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@gmail.com'

        
    def fullname(self):
        return f'{self.first} {self.last}'
 
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_Amount)


#inherited class
class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prgm_lang):
        super().__init__(first, last, pay)
        self.prgm_lang = prgm_lang

#inherited class with different methods
class Manager(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []

        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print(emp.fullname())
          



dev_1 = Developer('manu', 'pranav', 120000, 'Python')  
dev_2 = Developer('mike', 'shaw', 100000, 'Java')  


mgr_1 = Manager('Helly', 'kelly', 90000,[dev_1])

mgr_1.add_emp(dev_2)
mgr_1.print_emps()

# isinstance check weather it is an instance of a class
print(isinstance(mgr_1, Manager))

# issubclass check weather it is an subclass of a class
print(issubclass(Developer, Employee))

print(dev_1.prgm_lang)



