from PIL import Image,ImageFilter

img=Image.open('pokedex/pikachu.jpg')
# filtered= img.filter(ImageFilter.BLUR) sharpen, smooth etc also possible
# filtered.save('blur.png','png') to save it to current directory ,name, extension
#using img.convert('L') we can convert it into grey format
print(img.format)
print(img.size)
print(img.mode)
img.show() #shows the image
#.rotate(angle) rotates the image , needs to be stored as it returns the new image
#.resize also works, u need to pass a tuple of dimensions
#crop also possible , parameters are the pixel coordinates
#look into documentation for more
#to keep the aspect ration , we use img.thumbnail((x,y)), it doesnot return anything but changes the image itself. it automatically adjusts coordinates 

