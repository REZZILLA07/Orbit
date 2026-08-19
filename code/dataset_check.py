import os
from PIL import Image

dataset_path = r"C:\Users\Havisha\Downloads\Chest_xrays\Chest_xrays"

train_path = os.path.join(dataset_path, "train")

# Get image files
image_files = [
    f for f in os.listdir(train_path)
    if f.lower().endswith((".png", ".jpg", ".jpeg"))
]

print("Number of image files:", len(image_files))

# Check first image
first_image = os.path.join(train_path, image_files[0])

try:
    img = Image.open(first_image)

    print("First image:", image_files[0])
    print("Image format:", img.format)
    print("Image size:", img.size)
    print("Image mode:", img.mode)

except Exception as e:
    print("Error opening image:", e)