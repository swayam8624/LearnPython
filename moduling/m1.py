import m0
# import p1.m2
from p1.m2 import aftertax


print(m0)
print(m0.multiply(2,3))
print(m0.divide(2,3))
print(aftertax(45))

#if module is inside another folder: folder containing modules = packages
#for them :
# import package.module | from package.module import function | from package import module

if __name__=='__main__':
    print('please run this')
