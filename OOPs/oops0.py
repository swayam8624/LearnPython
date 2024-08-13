#                                                         Object Oriented Programming
#classes are abstract data type including data types and there methods
#blueprint of an object
#object is an instance of a class
#camel case not 
'''
class BigObject: #class
    pass

obj1= BigObject()  #instantiation of the class 
print(type(obj1))
#multiple objects possible
'''

from typing import Any


class PlayerCharacter:
    membership = True # available to all the methods  , it is a class object attribute , no need to use self while using  this attribute
    def __init__(self, name, age):  #dunder method or magic method, here it is a constructor
        self.name = name #attributes
        self.age = age
#constructor always run when class is instantiated
#self is the pointer to the class itself, to avoid name anomality
    def run(self):
        print('run')

    def shout(self):
        print(f'my name is {self.name}')

    @classmethod 
    def adding_things(cls, num1, num2):
        return cls('teddy', num1+num2) #would instantiate the class with attributes teddy and age as num1+num2
    @staticmethod
    def adding_things2(num1, num2): # same as classmethod just without cls, cannot create objects
        return num1+num2 

player1= PlayerCharacter('Aditi',20)
player1.run()
player1.shout()
print(player1, player1.age)
print(player1.adding_things(2,3))
player2= PlayerCharacter.adding_things(4,5) # another way of object creation 

# 4 pillers of oop
# a) Encapsulation 
'''
binding of data and functions associated with them (attributes and methods)
ex - class , its datas , and methods available to it
another example are python inbuilt data types and there methods
gives more powers , its like a dictionary with extra powers (methods)
'''
# b) Abstraction
'''
hiding away information and giving access to only the needed ones
when we call method shout , we get output and return value at max , we dont bother how was it implemented
same with builtin functions
more efficiency
public vs private variables
public can be accessed by anyone out or inside the class (default)
private can only be accessed inside the class by the class methods . to make a variable private we dont have private keyword but we add an underscore before the variable name in constructor , its an convention, there is no option for privacy , thats why a convention was introduced
to avoid programmers from touching that variable ( they can still do it, but shouldn't)
Ex - self._name= name
Though privatization could be achiecved using dundering (adding 2 underscores)
'''
# c) Inheritance
'''
new objects to take properties of existing ones
more on it in oop1.py
'''
# d) Polymorphism
'''
giving same method name different functions , they act differently
more oon it in oop1.py
'''

#Dunder Magic methods
class Toy:
    def __init__(self, color, age):
        self.color=color
        self.age=age
        self.my_dict ={
            'name':'yoyo',
            'has_pets': False
        }

    def __str__(self):
        return f'{self.color}'
    
    def __len__(self):
        return self.age
    def __call__(self):
        return 'yess???'
    def __getitem__(self):
        return self.my_dict


action_figure=Toy('red',1)
print(action_figure.__str__()) # same as str(action_figure)
print(str(action_figure)) # output for this also changes
print(action_figure.__len__() , len(action_figure))
print(action_figure.__call__())
print(action_figure.__getitem__())
#del keyword deletes some sort of variable we might have had


class SuperList(list): #inheriting list class
    def __len__(self):
        return 1000


sl1=SuperList()
print(len(sl1))
sl1.append(5)
print(sl1[0])
print(issubclass(SuperList,list))
print(issubclass(list , object))

#Method Resolution Order
class A:
    num=10
class B(A):
    pass
class C(A):
    num=1
class D(B,C):
    pass
'''
        A
      /   \
     B     C
      \   /
        D
''' 
print(D.num) # mro is D->B->C->A thus output is 1
print(D.mro()) #depth first search
