#EXERCISE 13.1

from PIL import Image

with Image.open('kot.jpg') as image1:
    print(f'Mode: {image1.mode}')
    print(f'Size: {image1.size}') 
    print(f'Width: {image1.width}')  
    print(f'Height: {image1.height}') 
    print(f'Format: {image1.format}') 
    print(f'Image information: {image1.info}') 
    image1.show()

with Image.open("kot.jpg") as im:
    im.thumbnail((128, 128))
    im.save('kot_thumbnail.jpg', "JPEG")