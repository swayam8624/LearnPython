from collections import Counter, defaultdict, OrderedDict

li=[1,2,3,4,5,6,7,7]
print(Counter(li)) #gives dictionary with all elements as key and their count as value(in descending order)

dictionary= defaultdict(lambda:5 ,{'a':1,'b':2}) #gives a callable object to the dict 
print(dictionary['c'])

odict= OrderedDict()
odict['a']=1
odict['b']=2

odict2= OrderedDict()
odict2['b']=2
odict2['a']=1

print(odict==odict2) #ordered in form of insertion
#we no longer need it though as python made dictionaries ordered by default

import datetime

print(datetime.time(5,43,3))
print(datetime.date.today())

from array import array
#takes less memory than list and is faster
arr= array('i',[1,2,3] )
print(arr)