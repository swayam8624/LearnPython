with open('test.txt',mode='r+') as myfile: #the name is actually the path of file
    text=myfile.write(':)') #overwrites existing
    print(text)

#to write from where we ended , use append mode
#if file does not exist write mode creates a new one , or overwrite the existing one while treating it as new
#use pathlib for directories. it takes care of it for u




