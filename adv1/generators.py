#Generator

#range(100)
#list(range(100))
'''
def make_list(num):
    result=[]
    for i in range(num): #gives numbers one by one to iterable
        result.append(i*2)
    return result
my_list=make_list(10)
print(my_list)
'''
#iterable is anything through which we can loop through . have __iter__ working inside them

#every generator is a iterable but not every iterable is a generator

def generator_func(num):
    for i in range(num):
        yield i #instead of returning or appending it pauses the function

for item in generator_func(1000):
    print(item)
#no use of memory like above one

g= generator_func(100)
print(g) #give generator object
next(g)  
next(g)
print(next(g))
#yield pauses a function and comes back to it when next is used. it use the most recent one in the memory only
#next can be called as many times as we want until iteration is possible , after that it will give a stop iteration function

#as its not storing values they are much faster than list and ranges (look at decorator1.py for test)
