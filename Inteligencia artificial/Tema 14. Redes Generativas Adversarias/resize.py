import os
from PIL import Image

input_dir = "D:\CEIABD\img_align_celeba"

output_dir = "D:\CEIABD\img_align_celeba_89x109"

os.makedirs(output_dir, exist_ok=True)

for image_name in os.listdir(input_dir):
    image_path = os.path.join(input_dir, image_name)
    image = Image.open(image_path)
    image = image.resize((89, 109))
    image.save(os.path.join(output_dir, image_name))

print("Se ha redimensionado correctamente.")