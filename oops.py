''' class '''

class Employee:

    def __init__(self,first,last,pay):
       self.first = first
       self.last = last
       self.pay = pay
       self.email = first+'.'+last+'@company.com'
    
    def fullname(self):
        print('{}{}'.format(self.first,self.last))


emp_1 = Employee('Corey','Schafer',50000)
emp_2 = Employee('Test','User',60000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname());
print(emp_2.fullname());


# run using class name
Employee.fullname(emp_1)  ;