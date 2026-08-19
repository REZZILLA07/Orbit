import os
import matplotlib.pyplot as plt
from PIL import Image

dataset_path = r"C:\Users\Havisha\Downloads\Chest_xrays\Chest_xrays"
train_path = os.path.join(dataset_path, "train")

image_files = [
    f for f in os.listdir(train_path)
    if f.lower().endswith((".png", ".jpg", ".jpeg"))
]

# Select first 6 images
selected_images = image_files[:6]

plt.figure(figsize=(12, 8))

for i, image_name in enumerate(selected_images):
    image_path = os.path.join(train_path, image_name)
    image = Image.open(image_path)

    plt.subplot(2, 3, i + 1)
    plt.imshow(image, cmap="gray")
    plt.title(image_name)
    plt.axis("off")

plt.tight_layout()
plt.show()