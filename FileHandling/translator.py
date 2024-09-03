#using offline python translation
from translate import Translator

translator=Translator(to_lang='ja')
try:
    with open('test.txt', mode='r') as myfile:
        text=myfile.read()
        translation=translator.translate(text)
        print(translation)
except FileNotFoundError as e:
    print("file does not exist "+ e )
    

