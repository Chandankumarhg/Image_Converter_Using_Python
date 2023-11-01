from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')
img2 = Image.open('./pokedex/bulbasaur.jpg')
img3 = Image.open('./pokedex/squirtle.jpg')
# print(dir(img))
# print(img.format)
# print(img.size)
# print(img.mode)
filtered_image = img.filter(ImageFilter.BLUR)
filtered_image.save("blur.png", 'png')

filtered_image2 = img2.convert('L')
crooked = filtered_image2.rotate(90)
filtered_image2.save("grey.png", 'png')
# crooked.show()
resize = filtered_image2.resize((200, 200))
resize.save("resized_bulbasaur.png", 'png')


box = (200, 200, 400, 400)
region = img3.crop(box)
region.save('resize.png', 'png')


img4 = Image.open('./astro.jpg')
img4.thumbnail((400,400))
img4.save("cropped_astro.png", 'png') 





