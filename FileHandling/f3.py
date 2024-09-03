try:
    with open('test.txt',mode='r') as myfile:
        print(myfile.read())

except FileNotFoundError as err:
    print('file does not exist')
    raise err
except IOError as err2:
    raise err2
except FileExistsError as err3 :
    print("file do not exist")
