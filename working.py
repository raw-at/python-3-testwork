class Employee:

    def __init__(self,first,last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    #using getter
    
    @fullname.setter
    def fullname(self,name):
        first,last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Deleted')
        self.first = None
        self.last = None

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first,self.last)

emp_1 = Employee('Abhinav','Rawat')

print(emp_1.first)
#print(emp_1.email())

print(emp_1.email)  #using getter
 
print(emp_1.fullname)

emp_1.first = ' John'
print('-------------------------------------------------')
print(emp_1.first)
print(emp_1.email) 
print(emp_1.fullname)

emp_1.fullname = 'Lll wayne'
print('-------------------------------------------------')
print(emp_1.first)
print(emp_1.email) 
print(emp_1.fullname)

del emp_1.fullname

print('-------------------------------------------------')
print(emp_1.first)
print(emp_1.email) 
print(emp_1.fullname)