'''
def heloo():
    print('helloooooo')

greet =heloo
heloo()
del heloo #just deletes the name reference to the function
#functions work exactly like variable
#without () they just point to the functions like pointer variable

print(greet()) 
'''
#Higher order function HOC
def greet(func):
    func()

def greet2():
    def func():
        return 5
    return func
#any HOc is just a function that can either accpet the function as parameter or return a function.. ex(map)

#Decorator
def my_decorator(func):
    def wrap_func(x):
        print('*****')
        func(x)
        print('*****')
    return wrap_func

@my_decorator
def hello(greeting):
    print("hellooooooo"+greeting)

hello('hii')
#decorator allows us to enhance the current function
#allows us to superboost a function by only using one extra line 
#we need to call @decorator before every function we need to boost
#same as my_decorator(hello)()
#in order to make decorator independent of no of parameter  just pass *args and **kwargs in place of x
