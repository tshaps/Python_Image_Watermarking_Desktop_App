from PIL import Image
import os


# Resize image function
def resize_images(input_folder, output_folder, size=(800, 600)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            img = Image.open(os.path.join(input_folder, filename))
            img = img.resize(size)
            img.save(os.path.join(output_folder, filename))
            print(f"Resized {filename}")


resize_images("images", "new_images", size=(800, 600))
