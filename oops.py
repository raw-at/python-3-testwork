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

    def __repr__(self):
        return "Employee({},{},{})".format(self.first,self.last,self.pay)

    def __str__(self):
        return "{}-{}".format(self.fullname(),self.email)
    
    def __add__(self,other):
        return self.pay + other.pay


    def fullname(self):
        return '{}{}'.format(self.first,self.last)

    def __len__(self):
        return len(self.fullname())
    
    def __mul__(self,other):
        return self.pay * other.pay

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



''' Inheritance '''

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay) #call init of parent
        #Employee.__init__(first,last,pay) -->Another method
        self.prog_lang = prog_lang


dev_1 = Developer('Corey','Schafer',50000,'Python');
dev_2 = Developer('Test','User',70000,'JS');

print(dev_1.email);
print(dev_1.prog_lang);

#print(dev_1.pay)
#dev_1.apply_raise()
#print(dev_1.pay)


class Manager(Employee):
    def __init__(self,first,last,pay,empolyees=None):
        super().__init__(first,last,pay)
        if empolyees is None:
            self.empolyees = []
        else:
            self.empolyees = empolyees

    
    def add_emp(self,emp):
        if emp not in self.empolyees:
            self.empolyees.append(emp)

    def remove_emp(self,emp):
        if emp in self.empolyees:
            self.empolyees.remove(emp)
    
    def print_emp(self):
        for emp in self.empolyees:
            print('-->',emp.fullname());
        

mgr_1 = Manager('SUE','SMITH',90000,[dev_1])
print(mgr_1.email)
print(mgr_1.print_emp())

mgr_1.add_emp(dev_2);
print(mgr_1.print_emp())

mgr_1.remove_emp(dev_1);
print(mgr_1.print_emp())


print(isinstance(mgr_1,Manager));
print(isinstance(mgr_1,Employee));
print(isinstance(mgr_1,Developer));

print(issubclass(Manager,Employee));
print(issubclass(Manager,Developer));


''' SPecial Methods '''

print(emp_1);
emp_1.__str__();
emp_1.__repr__();

print(1+2)
print(int.__add__(1,2))
print(emp_1+emp_2) #equalivalent to emp1.__add__(emp_2)
print(emp_1.__add__(emp_2));

print(len(emp_1));
print(emp_1*emp_2);

def epic():
    print('SUch a great module')
if __name__ == '__main__':
    print('such awesome')

    '''user input '''

#x = input('What is your name? ')
#print(type(x))
#print('Hello',x)

''' Statistics Module '''

import statistics as s
from statistics import variance as v

example_list = [4,6,2,6,7,8,2,5,6,4,5,6,5,6,25]
x = s.mean(example_list)
y = s.mode(example_list)
z = s.median(example_list)
a = s.stdev(example_list)
#only variance
b = v(example_list)


print('Mean: ',x)
print('Mode: ',y)
print('Median: ',z)
print('Standard Deviation: ',a)
print('Variance: ',b)

#for import everything from module 
#from statistics import *

''' LIST VS TUPLE '''
#tuple are immutable cannot be changed one defined
#list can be changes after defination also

x = 5,6,7,8 #tuple
y = [5,6,7,8] #list
print(x)
print(y)


''' list manipulation '''
x = [56,2,5,4,1,3,6,52,1,3,6]
y = ['Jes','joe','bob','alen']
x.append(20)
#insert(where,what)
x.insert(2,99)
x.remove(2)
x.remove(x[2])
print(x)
print(x[5:7])

print(x.index(1))
print(x.count(6))
print(x)
x.sort()
print(x)
y.sort()
print(y)

''' 2D list '''

x = [[5,6],[6,7],[7,2],[2,5]]

print(x[1][0])

''' 3d list '''
y = [
        [
            [5,4],[1,2],[56,2],[2,3]

        ],
        [
            [2.50,25],[25,3],[8,25],[2,6]
        ]
]

print(y[0][1][1])
















