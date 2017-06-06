nums = [1,2,3,4,5,6,7,8,9,10]
'''
my_list = []
for n in nums:
    my_list.append(n)

print(my_list)
'''
my_list = [n for n in nums] #list comprehension

my_list = [n*n for n in nums] #list comprehension

my_list = [n for n in nums if n%2==0]
print(my_list)

my_list = [(letter,number) for letter in 'abcd' for number in range(4)]
print(my_list)

''' zip function '''

names = ['Bruce','Clark','peter','logan','wade']
heros = ['Batman','Superman','spiderman','wolverine','Deadpool']
x = zip(names,heros)
for i in x:
    print(i)
#zip function make tuple of the corresponding element of the list and make a
#overall list

my_dict = {}
for name,hero in zip(names,heros):
    my_dict[name]=hero

print(my_dict)




my_dict = {name:hero for name,hero in zip(names,heros)}
print(my_dict)



''' generator '''

def gen_fun(nums):
    for n in nums:
        yield n*n

my_gen = gen_fun(nums)

for i in my_gen:
    print(i)


''' generator comprehension '''
my_gen = (n*n for n in nums)

for i in my_gen:
    print(i)