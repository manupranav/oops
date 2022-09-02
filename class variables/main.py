class Employee: 

    #class based variables
    num_of_emps = 0
    raise_Amount = 1.04
    
    def __init__(self,first, last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last +'@gmail.com'

        Employee.num_of_emps += 1 # class base variable
        
    def fullname(self):
        return f'{self.first} {self.last}'


    #instance based variable
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_Amount) #will not be able to change signle employe raise amount if it is Employee.raise_Amount


emp_1 = Employee('manu', 'pranav', 120000)  
emp_2 = Employee('m', 's', 100000)  


emp_1.raise_Amount = 1.05 #set emp1 raise amount

print(Employee.raise_Amount)
print(emp_1.raise_Amount)
print(emp_2.raise_Amount)


print(Employee.num_of_emps)