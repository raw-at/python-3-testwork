print('Hello world!')
print("We'r going to store");
print('he said "Hi."');
 
#excape character
print('we\'r going to the store');

#concatenate with + symbol
print("hi"+"there");

#concate with , symbol this add a space
print('hi','there'); 

print('hi',5);
#string coversion
print('hi '+str(5));

#int coversion
print(int('13')+5);

#float conversion
print(float('8.5')+4);

#Maths + - * / 

''' This is for multiple line comment 
We can put multiple comments here
'''

#Add operation 
print(1+3);

#Subtraction
print(3-1);

#Multiplication
print(4*4);

#Division this give decimal value 
print(5/34);

#power operation
print(4**4);

''' Variables '''

exampleVar = 53;
print(exampleVar);

#variable having function
exampleVar = print('whoa');

#unpacking into variables
x,y = (3,5)
print("x-axis",x,"y-axis",y);

''' while loop '''

condition = 1
while condition<10:
    print(condition);
    condition+=1;

'''
#Infinte loop
while True:
    print('doing stuff');
''' 

''' For Loop '''

#use to iterate through the list

exampleList = [1,2,3,54,6,5,4,60]
for i in exampleList:
    print(i);

print('continue program ');

#range upto last number
for x in range(1,11):
    print(x);


''' If statement '''

x = 5
y = 8
z = 5
a = 3
if(x<y):
    print('x is lesser than y')

if(z<y>x>a):
    print('y is greater than z and the greater than x');

if z<=x:
    print('z is less than or eqaul to x');

if  z == x:
    print('z is equal to x');    

if z != y:
    print('z is not equal to y')

''' if else '''

if(x>y):
    print('X is greater than y')
else:
    print('X is lesser than y');

if x>y:
    print('X is greater than y');
if x<y:
    print('X is lesser than y');
if x==y:
    print('x is equal to y');
else:
    print('ok ok');

''' elif Else '''
x = 5
y = 10
z = 22
if x>y:
    print('x is greater than y')
elif x<z:
    print('x is lesss than z')
elif 5>2:
    print('5 is greater than 2')
else:
    print('if and elif never run'); 










