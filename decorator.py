class Employee:

    def __init__(self,first,last):
        self.first = first
        self.last = last
    
    @property    #written as function access as attribute
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    @fullname.setter
    def fullname(self,fullname):    
        first,last = fullname.split(' ');
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.first = None
        self.last = None


    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first,self.last)


emp_1 = Employee('John','SMith')

emp_1.first = 'Jim'
emp_1.fullname = 'John Lenon'

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname
print(emp_1.fullname)