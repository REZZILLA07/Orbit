import os
import pandas as pd

# Change this path to where your Chest_xrays folder is located
dataset_path = r"C:\Users\Havisha\Downloads\Chest_xrays\Chest_xrays"
train_path = os.path.join(dataset_path, "train")
test_path = os.path.join(dataset_path, "test")
labels_path = os.path.join(dataset_path, "train_labels.csv")

# Count images
train_images = os.listdir(train_path)
test_images = os.listdir(test_path)

print("Number of training images:", len(train_images))
print("Number of test images:", len(test_images))

# Read labels
labels = pd.read_csv(labels_path)

print("\nLabel columns:")
print(labels.columns)

print("\nFirst 5 rows:")
print(labels.head())

print("\nNumber of labels:", len(labels))