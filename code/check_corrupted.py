import os
from PIL import Image

dataset_path = r"C:\Users\Havisha\Downloads\Chest_xrays\Chest_xrays"
train_path = os.path.join(dataset_path, "train")

image_files = [
    f for f in os.listdir(train_path)
    if f.lower().endswith((".png", ".jpg", ".jpeg"))
]

corrupted = []

for image_name in image_files:
    image_path = os.path.join(train_path, image_name)

    try:
        with Image.open(image_path) as img:
            img.verify()
    except Exception:
        corrupted.append(image_name)

print("Total images checked:", len(image_files))
print("Corrupted images:", len(corrupted))

if corrupted:
    print("\nCorrupted files:")
    for image in corrupted:
        print(image)