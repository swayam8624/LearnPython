from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1=time()
        result=fn(*args , **kwargs)
        t2=time()
        print(f'took {t2-t1} ms')
        return result
    return wrapper

@performance
def long_time():
    for i in range(10000000):
        i*5

@performance
def long_time2():
    for i in list(range(10000000)): #take more time
        i*5

@performance
def generator_func(num):
    for i in range(num):
        yield i #instead of returning or appending it pauses the function



long_time() #0.3 sec
long_time2() #0.41 sec
generator_func(10000000) #2.14 microsec (fastest)
#for longer ranges list one wouldnt even run completely
#generator allows least time
