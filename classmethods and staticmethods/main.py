class Employee: 

    num_of_emps = 0
    raise_amt = 1.04
    
    def __init__(self,first, last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@gmail.com'

        Employee.num_of_emps += 1
        
    def fullname(self):
        return f'{self.first} {self.last}'
    #regular method
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_Amount)

    #class method
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    #class method used as alternative constructor
    @classmethod 
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    #static method is used when when we dont call the instance or class variables
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False

        return True

      


emp_1 = Employee('manu', 'pranav', 120000)  
emp_2 = Employee('mike', 'shaw', 100000)  


import datetime
my_date = datetime.date(2022, 1, 9)

print(Employee.is_workday(my_date))

emp_1.set_raise_amt(1.05) #set raise amount to 1.05 to all instance and also in class

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)


emp_str_1 = 'Mike-hawk-560000'

new_emp_1 = Employee.from_string(emp_str_1)


print(new_emp_1.first)
