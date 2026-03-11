from PIL import Image
import os

img = Image.open('images/itsmybot.com-wp-content-uploads-2024-04-companies.webp')
w, h = img.size
# Let's guess 5 companies
num_slices = 5
slice_w = w // num_slices

for i in range(num_slices):
    box = (i * slice_w, 0, (i + 1) * slice_w, h)
    slice_img = img.crop(box)
    slice_img.save(f'images/company_{i+1}.png')
print("Saved 5 slices")
