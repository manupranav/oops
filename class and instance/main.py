class Employee: #Blue print of class
    
    def __init__(self,first, last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@gmail.com'
        
    def fullname(self):
        return f'{self.first} {self.last}'

# Different instance of employee print them to show their instances
emp_1 = Employee('manu', 'pranav', 120000)  # instance 1
emp_2 = Employee('m', 's', 100000)  # instance 2


print(emp_1.fullname())
print(emp_2.__dict__) # prints all the elements in emp2 instances