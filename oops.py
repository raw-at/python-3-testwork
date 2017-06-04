''' class '''

class Employee:
    #class variable
    raise_amount = 1.04
    no_of_employee = 0

    def __init__(self,first,last,pay):
       self.first = first
       self.last = last
       self.pay = pay
       self.email = first+'.'+last+'@company.com'
       Employee.no_of_employee += 1
    def fullname(self):
        print('{}{}'.format(self.first,self.last))

    ''' Class Variables '''

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)
    
emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee('Test','User',60000)
'''
print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname());
print(emp_2.fullname());

# run using class name
Employee.fullname(emp_1)  ;
'''

print(emp_1.raise_amount); #able to get that from instance as it first search for that variable in instance
print(Employee.raise_amount);#and then run into the class for the variable
print(emp_2.raise_amount);

'''
print(emp_1.__dict__)
print(Employee.__dict__); #namespace
'''
Employee.raise_amount = 1.05

print(emp_1.raise_amount); #able to get that from instance as it first search for that variable in instance
print(Employee.raise_amount);#and then run into the class for the variable
print(emp_2.raise_amount);

emp_1.raise_amount = 1.05 #this create a raise_amount variable in the instances of class  
print(emp_1.raise_amount)
print(emp_1.__dict__)


print('NUmber of Employee '+str(Employee.no_of_employee));














