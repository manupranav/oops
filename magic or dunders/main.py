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

    #magic methods
    # suitable for normal developers
    def __repr__(self):
        return f'Employee({self.first},{self.last},{self.pay})'

    # suitable for normal users
    def __str__(self):
        return f'{self.fullname()} - {self.email}'

    #dunder method to add two employees salaries
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())





emp_1 = Employee('manu', 'pranav', 120000)  
emp_2 = Employee('mike', 'shaw', 100000)  


print(emp_1)
print(repr(emp_1))

#dunder
print(emp_1 + emp_2)

print(len(emp_1))




