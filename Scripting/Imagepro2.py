# Jpeg to Png converter

#terminal command : Imagepro2.py pokedex/ new/
#it will convert all the images in pokedex to png and store it in a new folder 

import sys,os
from PIL import Image

# grab first and second argument
first = sys.argv[1] #takes input while running file in the terminal in form of tuple
last = sys.argv[2]


# check if new/ exists or not
if not os.path.exists(last):
    os.makedirs(last)
# loop through pokedex

for jpg in os.listdir(first):
    img=Image.open(f'{first}{jpg}')
    # convert and  save them
    clean_name=os.path.splitext(jpg)[0] #removes extension and name and returns tuple of both
    img.save(f'{last}{clean_name}.png','png') #to convert


#OpenCv
# very powerful , usefull for video processing
