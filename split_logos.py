from PIL import Image
import os

img = Image.open('images/itsmybot.com-wp-content-uploads-2024-04-companies.webp').convert("RGBA")
w, h = img.size

# Let's slice into 6 equal segments to be safe.
num_slices = 6
slice_w = w // num_slices

idx = 1
for i in range(num_slices):
    box = (i * slice_w, 0, (i + 1) * slice_w, h)
    slice_img = img.crop(box)
    bbox = slice_img.getbbox()
    if bbox:
        trimmed = slice_img.crop(bbox)
        if trimmed.width > 20 and trimmed.height > 10:
            trimmed.save(f'images/company_logo_{idx}.png')
            print(f"Saved company_logo_{idx}.png: {trimmed.width}x{trimmed.height}")
            idx += 1
