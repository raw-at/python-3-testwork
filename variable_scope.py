'''
    LEGB
    Local,Enclosing,Global and built-in

'''
x = 'global x'
'''
def test():
    y = 'local y' #local to this function
    print(y)

    print(x) #check for local scope->enclosing scope->global scope found there and print

test();
'''

def test_2():
    global x
    x = 'local x' 
    print(x) #access local x as local x is present
    #We want to modify global x from here i.e from local scope of the test_2 function

test_2()
print(x) #this also changes 


def test_3(z):
    print(z) #local to the test_3() function

test_3('local z')


#built-in
m = min([2,5,3,6,5])
print(m)

''' ENclosing '''

x = 'global x'

def outer():
    x = 'outer x'
    def inner():
        nonlocal x
        x='changed x'
        #x = 'inner x'
        print(x)        
    inner()
    print(x)

outer()

