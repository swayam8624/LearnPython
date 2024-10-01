#pure functions
#2 rules - same output for the same input and there should not be any side effects to the outside world
def multiplyby_2(item):
    return item*2

#it is more of a guideline

def checkifodd(item):
    return item%2 != 0

l1=[1,2,3]
l2=[10,20,30]

#map()

print(list(map(multiplyby_2,[1,2,3]))) #map(action, datatype)
'''
iterates through all the items in the iterable and perform the actions on them by itself
doesnt modify actual list (iterable)
pure function
'''

#filter()

print(list(filter(checkifodd,[1,2,3]))) #same syntax
'''
performs check on each item of the iterable and filter the ones that do not satisfy the action
'''

#zip()

print(list(zip(l1,l2))) #zips the same index items of both the iterables into a tuple al inside one list
'''zip(iterable1 , iterable2, ... , iterable n)
pure function
'''

#reduce()

from functools import reduce
#functools is a toolbelt
def accumulator(acc,item):
    print(acc, item)
    return acc+item

print(reduce(accumulator,l1,0)) #function , iterable, initial
'''
reduces iterable into a primitive type
performs function on each item with start value of initial provided
base for all the map, zip, filter functions
'''

#lambda expressions
#lambda param: action(param)
#used when needed only once + anonymous
print(list(map(lambda item: item*2,l1)))
#there can be more than one parameters

#square
l3=[5,4,3]
newlist= list(map(lambda num: num*2 , l3))
print(newlist)

#list sorting
a=[(0,2),(4,3),(10,-1),(9,9)]
#based on second item
a.sort(key=lambda x: x[1])
print(a)

