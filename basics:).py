#                 Fundamental Data types
# int -> Integer , it is a number like 2, 3,...
# float -> Floating point number, it is a number with a decimal point like 0.5, 1.2,...
# bool -> Boolean, it is either True or False
# str -> String, it is a piece of text like 'Hello', "Hello",...
# list -> List, it is a collection of items like [1,2,3,4,5]
# tuple -> Tuple, it is a collection of items like (1,2,3,4,5)
# set -> Set, it is a collection of unique items like {1,2,3,4,5}
# dict -> Dictionary, it is a collection of key-value pairs like {'a':1, 'b':2, 'c':3}

print(type(6))
print(type(2 - 4))  #-2
print(type(2 * 4))  #8
print(type(2 / 4))  #0.5
print(type(20 + 1.1))  #21.1
print(type(9.9 + 1.1))  #11.0

print(2**3)  #exponential
print(9 // 2)  #floor division
print(6 % 4)  #modulo
#all return int

#            math funtions
print(round(3.1))  #rounds up the number
print(abs(-20))  #no negatives
#there are several more

#float takes up lot more storage than int

#Classes -> custom types

#Specialized Data Types

None
#     operator precedence
20 + 12 * 4
# ()
# **
# * /
# + -

#complex -> complex numbers real+i(imaginary) it is a data type
#bin() -> binary representation of a number
print(int('0b101', 2))

#variables -> store information that can be used in our programs
#constant -> never change in a program (always in capital letters)
#python is a dynamic language so u dont need to specify the type of variables
#no need to initialize it with it's value
#              snake_case
#all lower case and underscore to separate words
#start with lowercase or underscore
#letters, numbers, underscores
#case sensitive
#dont overwrite keywords
#             keywords
#https://www.w3schools.com/python/python_ref_keywords.asp
#constants -> all in caps
#__ is called dunder. dont create a variable with two underscores
a, b, c = 1, 2, 3  #works

iq = 100
user_age = iq / 5  #iq/5 is an expression #statement is the entire line of code

#augmented assignment operator
some_value = 5
some_value += 2  #basically shorthand operator

#                strings -> piece of text
#can be written in '' or ""
#for multiline its written under """ """ or ''' '''
#       string concatenation -> adding strings together
a = 'swayam'
b = 'singal'
c = a + ' ' + b  # + is the concatination operator (only works with strings)
print(c)

#type conversion
print(type(int(str(100))))
#canverting a variable from one data type to another
#two types - inclusive and exclusive

#                   escape sequence
# \ -> whatever comes after this is a string .. it come with specific actions
#example
weather = "It\'s \"kind of\" sunny"
#here \ is a string and it is telling python that whatever comes after this is a string
print("hello \n hi")
#here \n is a new line indicator , like \t is tab , \r is carriage return
# \ is escape , \' is a single quote, \" is a double quote
#there are in all programming languages

#                   formatted strings
name = 'Johnny'
age = 55
print(f"hi {name} . you are {age} years old")  #f says it is formatted string
#if we want to remove f then
print('hi {} . you are {} years old'.format('Johnny',
                                            '55'))  #the variables in sequence.
print('hi {} . you are {} years old'.format(name, age))
#we can also use indexes with brackets like bracket with index 0
#would refer to first value in the variable tuple returned by format

#                   string indexes
selfish = 'me me me'
#01234567
#-8-7-6-5-4-3-2-1
#every character be it even space is stored in memory in a specific location
#thus each has its own index
print(selfish[0])  #we can access different parts of a string using its index
# [start:stop:stepover] also possible to access substrings
print(selfish[0:8:2])  #stepover 2 means skip every 2nd character
print(selfish[1:])  #starts at 1 and goes all the way to the end
print(selfish[:5])  #starts at 0 and goes all the way to 5
print(selfish[::1])  #starts at 0 and goes all the way to the end
#negative indexing also possible
print(selfish[-1])  #starts at the end and goes all the way to the beginning
print(selfish[::-1])  #starts at the end and goes all the way to the beginning
#                   immutability
#strings are immutable, they cannot be changed
# we can reassign strings but not specifc parts of it
#selfish[0]='8' #this is not possible
#we can though add characters
selfish += '8'
print(selfish)
#                   built in functions
#https://docs.python.org/3/library/functions.html
#len() -> length of the string
print(len('hello'))
#methods are similar to functions but they are owned by something
#slicing also possible
#https://docs.python.org/3/library/stdtypes.html#string-methods
print(selfish.upper())  #it returns a value so needs to be stored
#similar with lower,capitalise,find(returns bool),replace
#until the variable is assigned to a new value returned they do not change
#                   booleans
#bool -> True or False or 1 or 0
#                   type conversion

birth_year = input('what year were you born?')
age = 2024 - int(birth_year)
print(f'your age is {age}')
#best type converter for input is eval

#                   password checker

username = input('enter your username')
password = input('enter your password')
password_length = len(password)
hidden = '*' * password_length
print(f'{username}, your password {hidden} is {password_length} letters long')

#                        List
#ordered, mutable , allows duplicate elements, can be of different data types
#list is a collection of items (heterogeous))
#written inside [] square brackets
li = [1, 2, 3, 4, 5]
li2 = ['a', 'b', 'c']
li3 = [1, 2.5, 'a', True]
#list is a Data Structure
#it is a way to organize data
#slicing possible
print(li[0])
print(li[0:2])
#list are mutable
li[0] = 8
print(li)
#list slicing creates a new list, not alters the original
amazon = ['laptop', 'sunglasses', 'toys', 'grapes']
new = amazon
print(amazon)
print(new)
# this happens because python is value specific, two variables are
#pointing to the same memory location because of the assignment of same values
#instead we can do
new = amazon[:]  #this creates a copy of the list ,or .copy() function can be used
new[0] = 'gum'
print(amazon)
print(new)
#                    Matrix
#a way to describe 2D lists or multidimensional lists
matrix = [[1, 2, 3], [2, 4, 6], [7, 8, 9]]
#comes handy when we have data that is in tabular form or images
#accessing a matrix
print(matrix[0][1])  # value at 0th row and 1st column
#                    List Methods
#https://www.w3schools.com/python/python_ref_list.asp
print(len(amazon))
#adding
amazon.append('notebooks')  #for single values, does not return a value
print(amazon)
amazon.insert(2, 'toys')  # for a value at any index, does not return a value
print(amazon)
amazon.extend([100, 101])  #for multiple values, does not return a value
print(amazon)
#removing
amazon.pop()  #removes the last element, returns
print(amazon)
amazon.pop(0)  #removes the element at a specific index, returns
print(amazon)
amazon.remove(
    'toys')  #removes the first occurence of a value (value based removal)
#no return value
print(amazon)
amazon.clear()  #removes all the elements, returns
print(amazon)
x = amazon.clear()
print(x)
#index
basket = ['a', 'b', 'c', 'd', 'e', 'd']
print(basket.index('d'))  #returns the index of the value
#print(basket.index('d',0,2)) #returns error as d is not in the range
#here 0 is starting index and 2 is ending index
#in keyword
print('d' in basket)  #returns boolean
#count
print(basket.count('d'))  #returns the count of the value
#sort
basket.sort()  #sorts the list in place, returns nothing
print(basket)
#sorted
print(sorted(basket))
#difference is it create a new copy of basket , not modifies the existing one
#reverse
basket.reverse()  #reverses the list in place, returns nothing
print(basket)
print(basket[::-1])  #no modification in actual
#range
print(list(range(1, 10)))  #starts at 1 and goes to 99
#range(start,stop,stepover)
#join
sentence = '!'
new = sentence.join(['hi', 'my', 'name', 'is',
                     'jojo'])  #input should be a list(iterable)
print(
    new
)  #joins the elements of the list with the string in between as separators
#list unpacking
a, b, c, *other, d = [
    1, 2, 3, 4, 5, 6
]  #* allows take multiple values, if no other variable then
#* takes all element with itself
print(a)
print(b)
print(c)
print(other)
print(d)
#                    None
#None is a special data type, it represents the absence of value
#                    Dictionary
#unordered key value pair
dicti = {"a": [1, 1, 'hey'], "b": 2, "c": 3}
#key can be either string or an integer or boolean
#value can be anything(any data type)
print(dicti["b"])
#there is no concept of index in dictionary
#access only through key
print(dicti)
print(dicti['a'][1])
# there can be multi dimensional dimensions
# dictionary can be inside list
my_list = [{
    'a': [1, 2, 3],
    'b': 'hello',
    'c': True
}, {
    'a': [4, 5, 6],
    'b': 'hello',
    'c': True
}]
print(my_list[1])
print(my_list[0]['a'][2])
#dictionary keys should be immutable
#keys should be unique otherwise it gets overwritten
#dictionary hold much more information than list
#dictionary methods
#https://www.w3schools.com/python/python_ref_dictionary.asp
#get -> it gets the value of a key, without throwing error, it returns none in that case
print(dicti.get('age'))
#if we want to give a default value to the key that does not exist
print(dicti.get('age', 55))  #here 55 is a default value if age doesn't exist
#another way to create dictionary
user2 = dict(name='swayam')
print(user2)
#in keyword
print('a' in dicti)  #returns boolean
print('a' in dicti.keys())  #returns boolean (using keys method)
print('hello' in dicti.values())
print(dicti.items())  #tuple of key value pairs #entirely of nonetype
#needs to be converted into list before
user3 = user2.copy()
print(user3.clear())
print(user2)
print(dicti.pop('a'))  #removes and retruns the value of the key
print(dicti.popitem())  #randomly pops any item
user = {'ages': 45}
print(user.update({'ages': 55}))  #updates the value of the key
print(user)
#                    Tuples
#immutable lists
#cannot be modified
#faster than lists
#cannot be sorted, reversed
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1])
print(5 in my_tuple)
#tuple can be used as a key in dictionary
#tuple can be sliced
new_tuple = my_tuple[1:2]
print(new_tuple)
#tuple has only two methods
#count and index
print(my_tuple.count(5))
print(my_tuple.index(5))
#                    Set
#unordered collection of unique objects
#no duplicates allowed
#set is a collection of values (frozenset)
my_set = {1, 2, 3, 4, 5, 5}
print(my_set)
#no indexing possible, as it is unordered
#adding
my_set.add(100)
my_set.add(2)
print(my_set)
#converting list to set
l = [4, 5, 6, 7, 8, 9, 10, 4, 5]  #vice versa also possible
s = list(l)
print(set(l))
#in keyword works with set
#len() works with set
#copy() works with set
#clear() works with set
#set methods
#https://www.w3schools.com/python/python_ref_set.asp
#all actual set opeartions are possible
#difference
print(my_set.difference(s))
#discard
print(my_set.discard(5))
print(my_set)
#difference_update
my_set.difference_update(s)
print(my_set)
#intersection
print(my_set.intersection(s))  #also works with &
my_set.intersection_update(s)
print(my_set)
print(my_set.isdisjoint(s))
#union
print(my_set.union(s))  #also works with |
#issubset
print(my_set.issubset(s))
#issuperset
print(my_set.issuperset(s))
#                    Conditional Logic
#if-else
is_old = True
is_licensed = False
if is_old:  #enters the indentation is condition is true
    print('you are old enough to drive')
else:  #otherwise condition
    print('you are not old enough to drive')
print('checkcheck')
#elif
if is_old and is_licensed:
    print('you are old and liscensed to drive')
elif is_old and not is_licensed:  #other condition than all true and all false
    print('you are old enough to drive but not licensed')
else:
    print('you are not old enough to drive')
#there can be multiple elif , but a good programmer should only keep one if and one else
#                    Indentation in Python
#indentation is important in python
#they are spaces or tabs(4 spaces)
#lines at sane indentation are considered as part of the same block
#same as inside curly spaces in java
#                    Truthy and Falsy
#https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy
#basically anything that is not 0 or empty iterable datatype is considered as truthy
#otherwise it is considered as falsy (negative is truthy)
#                    Ternary Operator
#condition_if_true if condition else condition_if_false
is_friend = True
can_message = "message allowed" if is_friend else "not allowed to message"
#diff from standard java ternary
#in java its condition?true:false
print(can_message)
#                    Short Circuiting
is_user = True
print(is_friend or is_user)  #returns true even if any one is true
#short circuiting happens when the interpreter knows that one condition is already true
#in case of and , if false exists then it does not check the other conditions
#in case of or , if true exists then it does not check the other conditions
#                    Logical Operators
#and , or , > , < , == , != , not
print(4 > 5)
print(10 == 2 * 5)
#in case of string it uses ascii to compare
print('a' > 'A')
print(1 < 2 < 3 > 4)  #multiple possible (uses and)
# is vs ==
#is checks if the location in memory is same
#== checks if the value is same
print(True == 1)
print('1' == 1)
print([] == [])
print(10 == 10.0)
print([1, 2, 3] == [1, 2, 3])
print(True is 1)
print('1' is '1')
print([] is [])  #every data structure have different locations in memory
print(10 is 10.0)
print([1, 2, 3] is [1, 2, 3])

#                    For Loops
for item in 'zero to mastery':  #item is variable being iterated along the iterable
    #can be list ,string , set , tuple , dictionary or any iterable
    print(item)
for item in [1, 2, 3, 4, 5]:
    print(item)
#indentation should be maintained
print(item)  #final value of item is 5
for i in (1, 2, 3, 4, 5):
    for j in ['a', 'b', 'c']:
        print(i, j)
# multiple nested loops are possible
#                    Iterables
#list , dictionary , tuple , set , string
#iterated -> one by one check each item in the collection
user = {'name': 'golem', 'age': 5006, 'can_swim': False}
for key, value in user.items():
    print(key, value)
for item in user.items():  #tuples
    print(item)
for item in user.values():
    print(item)
for item in user.keys():
    print(item)
#                    Range
#range(start,stop,stepover)
#range is a special type of object, allowing iteration without iterables
print(range(10))
for i in range(0, 10, 2):  #default start is 0 , and stepover is 1
    print(i)
for i in range(10, 0, -1):
    print(i)
for i in range(2):
    print(list(range(10)))
#                    Enumerate
for i, char in enumerate('hello'):
    print(i, char)  #ability to get the index along
for i, char in enumerate(list(range(1, 100))):
    if char == 50:
        print(i, char)
#                    While Loops
#while a condition is happening (true) , do something
i = 0
while i < 50:
    i = i + 5
    if i == 25:
        continue
        print(i)  #will not be executed as continue is used
    elif i == 35:
        print(i)
        break
    else:
        print(i)

#be careful for infinite loops , do add counter update
#else also possible
i = 0
while i < 50:
    print(i)
    i = i + 10
else:
    print('done with all the work')
    #iff there isnt a break statement , else will be executed
    #else is executed only when loop condition becomes false
#break , continue , pass
#break -> breaks out of the loop
#continue -> goes to the top of the loop(the loop it is inside)
#pass -> does nothing , just passes to the next line , used when we dont know what to do
#works for every loop(for or while)
for item in [1, 2, 3, 4]:  #simpler
    print(item)
i = 0
mylist = [1, 2, 3, 4]
while i < len(mylist):  #more flexible
    print(mylist[i])
    i += 1
#while is used when no of iterations is not known
#user controlled exit

while True:
    response= input('say')
    if(response=='bye'):
        break

#                    First GUI
picture = [[0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 0],
           [1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 1, 0, 0, 0]]
for row in picture:  #iterate over picture
    for pixel in row:  #iterate over each row
        if (pixel == 1):  #checking is pixel is on
            print('*', end=''
                  )  #end provides string after the        print(defaut is \n)
            #there are several other parameters for print
        else:
            print(' ', end='')  #black space so that image is maintained
    print('')  #go to new line
#clean
#readability
#predictability
#DRY(do not repeat yourself)
#                    Exercise : Find Duplicates
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []
for i in some_list:
    if some_list.count(i) > 1 and i not in duplicates:  #if want to use count
        duplicates.append(i)
print(duplicates)

#else we can use set
#or we can use nested loops to check for duplicates (depends on the question)


#                    Functions
#defining a function
def say_hello():  #def keyword is used to define function
    print('hello')


say_hello()  #calling the function (() is important while calling function)
#allows modularity , reduce repetition , makes easier to update
print(say_hello)  #gives memory location


#            arguments and parameters
#parameters - used when defining the function
#values or variables that we pass along with to use inside the function
def sayhello(name, emoji):
    print(f'hello {name} {emoji}')


#formal(parameters) and actual parameters(arguments)
#arguments - used when actually calling the function
sayhello('swayam', '😊')  #called or invoked
sayhello('singal', '😊')
#above are positional arguments , as the position matters,
#if we change the order output will be different and for diff data types , error
sayhello('😕', 'swayam')
#keyword arguments - pass arguments with specific identities
#avoid mishaps of positional arguments
sayhello(emoji='😊', name='swayam')

#still u should maintain order
#default parameters
#when defining the functions we can give default value to parameters
#if an arg is missing while calling , it gives that call the default value to work with


#return keyword
def sum(num1, num2):
    return num1 + num2
    print('hi')  #the statement wont be executed as return exits the function


#allows us to return a value from the function, store in some variable outside
#helps the function to work with other functions outside
s = sum(4, 5)
d = sum(s, 6)
print(d)
#good practice is to return something
#return exits the function

#nested functions

def one_function(num1,num2):
    def another_func(n1,n2):
        return n1+n2



#the above function is not working as it doesnt return anything
#all we are doing is defining a function inside another function , not calling it
#we should either call the inside function or return it in the outer one
def one_function(num1, num2):

    def another_func(n1, n2):
        return n1 + n2

    return another_func(num1, num2)


print(one_function(4, 5))
#using different parameter names for clarity
#if not returning it returns none

#                 Tesla example

def checkDriverAge(age=0):
    if age > 18:
        return 'Powering On . enjoy the ride'
    elif age < 18:
        return 'sorry kiddo '
    else:
        return 'nice job passing kid'

age = input("What is your age?: ")
message= checkDriverAge(int(age))
print(message)

#methods vs functions
#methods are owned by objects
#sort(),len() etc
#called like object.function()
#functions are not owned by objects
#list(), print(), max() etc
#called like function() (independent of object)

#                Scope
#scope - what variables do i have access to ?
#global scope - any variable defined outside the function
#can be used by anyone
#function scope - any variable defined inside the function(local)
# can be used only by that function untill returned
#scope rules
#1 - start with local
#2 - parent local? (in case local declared not there)
#3 - global
#4 - built in python functions or keyword?
#variable initialized outside dont change its value even if it is changed inside the f/n
#that change creates a local add in its own universe without modifying the global one
#global keyword
#global keyword is used to access global variables inside the function
#change the value in the global add and not make local add like normal scenario
#while using global keyword, dont modify it in the same statement
#global keyword is not recommended
#nonlocal keyword
#nonlocal keyword is used to refer to the parent local variable.
#not global but a variable not inside the function but in its parent function


def outer():
    x = 'local'

    def inner():
        nonlocal x
        x = 'nonlocal'
        print('inner:', x)

    inner()
    print('outer:', x)


outer()
#not recommended to use nonlocal keyword either
#like nonlocal , global should also be declared in local section, not the global section
#keyword used to modify the variable
#Why do we need scope?
#to avoid memory leaks, wastage
#to avoid overwriting of variables

# *args and **kwargs
#args - arguments
#kwargs - keyword arguments

def super_func(*args,**kwargs):
    print(args)
    print(kwargs)
    total=0
    for items in kwargs.values():
        total+=items
    return sum(args)+total
print(super_func(1,2,3,4,5,num1=5,num2=10))

#rule of ordering of parameters
#params,*args,default parameters,**kwargs
#def super_func(name,*args,i='hi',**kwargs):

#walrus operator
# :=
#assigns values to variables as part of a larger expression
