def special_for(iterable):
    iterator=iter(iterable)
    while True:
        try:
            print(iterator)
            print(next(iterator)) #next provides the current and moves to next
        except StopIteration:
            break

special_for([1,2,3])
 #how range actually underneath the hood in range
class MyGen():
    current=0
    def __init__(self,first,last):
        self.first=first
        self.last=last

    def __iter__(self):
        return self
    
    def __next__(self):
        if MyGen.current<self.last:
            num = MyGen.current
            MyGen.current+=1
            return num
        raise StopIteration


gen=MyGen(0,10)
for i in gen:
    print(i)

print('*****')
#fibonacci 
def fib(num):
    a=0
    b=1
    for i in range(num):
        yield a
        temp=a
        a=b
        b=temp+b #temp introduced because a is already being updated before we could update b

for i in fib(13):
    print(i)
        