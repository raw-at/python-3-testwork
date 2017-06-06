def mult_by_2(num):
    return num*2


#passing function as a parameter
def do_math(func,num):
    return func(num)

c = do_math(mult_by_2,5)
print(c)


#function returning function
def get_func_mult_by_num(num):
    
    def mult_by(value):
        return num*value
    return mult_by

a = get_func_mult_by_num(5)
print(a(2))

''' function anotation '''
def random_func(name:str,age:int,weight:float)->str:
    print('Name:',name)
    print('age:',age)
    print('weight:',weight)

random_func('Derek',23,57)


''' Lambda anonymous function '''
#lambda arg1,arg2: arg1*arg2

sum = lambda x,y:x+y
print(sum(4,5))

can_vote = lambda age:True if(age>=18) else False
print(can_vote(56))


powerList = [lambda x:x**2,lambda x:x**3,lambda x:x**4]

for func in powerList:
    print(func(4))


attack = {'quick':(lambda:print('Quick Attack')),'power':(lambda:print('Power Attack')),'miss':(lambda:print('Missed Attack'))}

import random
attackKey = random.choice(list(attack.keys()))
attack[attackKey]()

''' Map function '''
#Map execute a function on each item on a list

oneTo10 = range(1,11)

def dbl_num(n):
    return n*2

print(list(map(dbl_num,oneTo10)))

print(list(map(lambda x:x*3,oneTo10)))

def print_data(n):
    print('hi'*n)

print(list(map(print_data,oneTo10)));


alist = list(map(lambda x,y:x+y,[1,2,3],[7,8,9]))
print(alist)

''' filter '''
#select value from the list based on the condition

print(list(filter(lambda x:x%2==0,range(1,10))))

''' reduce '''
from functools import reduce
print(reduce((lambda x,y:x+y),range(1,6)))







