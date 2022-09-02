class Employee: 


    def __init__(self,first, last):
        self.first = first
        self.last = last

    #property sets whole thing to same
    @property
    def email(self):
        return f'{self.first}.{self.last}@gmail.com'

    @property   
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Deleting...')
        self.first = None
        self.last = None

 



emp_1 = Employee('manu', 'pranav')    
emp_1.first = "test"
emp_1.fullname='spider man'

del emp_1.fullname #set value of fullname to none

print(emp_1.first)
print(emp_1.email) #it is a property no need to use email() --> email
print(emp_1.fullname)







