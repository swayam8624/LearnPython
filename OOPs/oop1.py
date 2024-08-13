# Inheritance

'''
Users 
 -Wizards
 -Archers
'''
class User: #super class
    def __init__(self,email):
        self.email=email

    def sign_in(self):
        print('logged in')

    def attack(self):
        print(f'do nothing') # it will get overwritten

class Wizard(User): #subclass
    def __init__(self, name , power,email):
        User.__init__(self,email)  #for initializing , super().__init__(email) also possible, in this self not required
        self.name= name
        self.__power=power
        
    
    def attack(self):
        print(f'attacking with power of {self.__power}')
#subclassing done by passing superclass while creating subclass
#multiple super classes can be passed

class Archer(User): #subclass
    def __init__(self, name , arr):
        self.name= name
        self.arr=arr
    
    def attack(self):
        print(f'attacking with no of {self.arr} arrows')
    
    def run(self):
        print("ran really fast")

class Hybrid(Wizard, Archer):
    def __init__(self, name, power , arr , email):
        Wizard.__init__(self,name, power,email) 
        Archer.__init__(self,name,arr )
        


w1= Wizard('os',50,'hi@gmail.com')
a1=Archer('hob',34)
h1=Hybrid('hybrido', power=87,email='bod@hi.com' ,arr=8)
w1.sign_in()
a1.sign_in()
w1.attack()
a1.attack()
h1.run()
h1.attack()
#isinstance(instance , Class)
print(isinstance(w1, Wizard))
print(isinstance(w1, User)) # as it is the super class
print(isinstance(w1, object)) # object is of the base class python comes with
print(issubclass(Wizard,User))
print(w1.email)
#to get the user attack function to work(super class function) , we need to call it as User.attack in the wizard attack method (subclass function)

#subclasses can use functions and public+protected variables of the parent or super class
#Polymorphism
'''
both wizard and archer have attack but print different things based on which objects is calling it
'''

def player_attack(char): #this char is not character but an attribute that is object of classes in this case
    char.attack()

player_attack(w1)
player_attack(a1)

for char in [w1,a1]:
    char.attack()

#introspection
#determining the type of object during run time
print(dir(w1)) #give a list of all the methods w1 has access to (dir function)

