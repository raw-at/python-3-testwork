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

''' Class Methods ,Regular Methods and statics Methods '''


class Student:
    no_of_students = 0 #class variable
    raise_marks = 1.04

    def __init__(self,name,last,marks):
        self.first = name
        self.last = last
        self.email = name+'.'+last+'@school.com'
        self.marks = marks
        Student.no_of_students += 1;

    def fullname(self):
        print('{} {}'.format(self.first,self.last))
    
    #class method


    @classmethod
    def set_raise_marks(cls,marks):
        cls.raise_marks = marks

    #Alternative constructor using classmethod
 
    @classmethod
    def from_string(cls,emp_str):
        first,last,marks = emp_str.split('-')
        return cls(first,last,marks)
    
    #staticmethods pass nothing
    @staticmethod
    
    def is_workeday(day):

        if(day.weekday() == 5 or day.weekday() == 6 ):
            return False
        return True

stud_1 = Student('Abhinav','Rawat',50000);
stud_2 = Student('Bhanu','Madan',60000);
    
Student.set_raise_marks(1.05);

print(Student.raise_marks)
print(stud_1.raise_marks)
print(stud_2.raise_marks)

 
new_emp_1 = Student.from_string('Abhinav-rawat-25000');
print(new_emp_1.fullname());

import datetime
my_date = datetime.date(2016,12,25)
print(my_date);
print(Student.is_workeday(my_date));























