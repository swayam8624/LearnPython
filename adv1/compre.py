#comprehension

#           list
#list=[param/exp for param in iterable]

mylist=[]
for char in 'hello':
    mylist.append(char)

print(mylist)

#Or 

my_list=[char for char in 'hello']
print(my_list)
l2= [num*2 for num in range(0,15,2)]
print(l2)
l3=[num**2 for num in range(0,15) if num%2==0]
print(l3)

#         Set 

#same as list just change the brackets

#dictionsary

simpledict={
    'a':1,
    'b':2
}
mydict={key:value**2 for key,value in simpledict.items()}
print(mydict)
#if also available here
d2={num:num*2 for num in [1,2,3]}
print(d2)

