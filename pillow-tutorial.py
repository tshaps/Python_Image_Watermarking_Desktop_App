from PIL import Image
import os

# Opening an Image
filename = 'description_img.jpg'
img = Image.open(filename)
img.show()

# Creating an Image
red_img = Image.new('RGB', (400, 500), (255, 0, 0))
green_img = Image.new('RGB', (400, 500), (0, 255, 0))
blue_img = Image.new('RGB', (400, 500), (0, 0, 255))
yellow_img = Image.new('RGB', (400, 500), 'yellow')
# yellow_img.show()

# Rotating an Image
img_90 = img.rotate(angle=90, expand=True)
# img_90.show()

img_60 = img.rotate(angle=60, expand=True, fillcolor='white', resample=Image.Resampling(2))
img_60.show()

# Resizing Image
img = Image.open('description_img.jpg')
# print(img.width, img.height)
# img.show()
img_down_size = img.resize((int(img.width / 2), int(img.height / 2)))
# print(img_down_size.width, img_down_size.height)
# img_down_size.show()
img_up_size = img.resize((int(img.width * 2), int(img.height * 2)))
# print(img_up_size.width, img_up_size.height)
# img_up_size.show()


# Blending Images
img_1 = Image.open('new_images/image_1.jpg')
img_2 = Image.open('new_images/image_2.jpg')
img_blend = Image.blend(img_1, img_2, alpha=0.5)
# img_blend.show()


# Cropping an image
img_cropped = img.crop(box=(10, 10, 800, 800))
# img_cropped.show()

