import os
import numpy as np
import pandas as pd

from PIL import Image
from sklearn.multioutput import MultiOutputClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

# Dataset paths
dataset_path = r"C:\Users\Havisha\Downloads\Chest_xrays\Chest_xrays"
train_path = os.path.join(dataset_path, "train")

# Load our saved splits
train_data = pd.read_csv("train_split.csv")
val_data = pd.read_csv("validation_split.csv")

conditions = [
    "Atelectasis",
    "Effusion",
    "Infiltration",
    "Nodule",
    "Pneumothorax"
]

# Resize images to make the baseline lightweight
IMAGE_SIZE = (64, 64)


def load_images(data):
    images = []

    for image_name in data["Image Index"]:
        image_path = os.path.join(train_path, image_name)

        image = Image.open(image_path).convert("L")
        image = image.resize(IMAGE_SIZE)

        # Convert pixels to values between 0 and 1
        image_array = np.array(image) / 255.0

        # Flatten the image
        images.append(image_array.flatten())

    return np.array(images)


print("Loading training images...")
X_train = load_images(train_data)

print("Loading validation images...")
X_val = load_images(val_data)

y_train = train_data[conditions].values
y_val = val_data[conditions].values

print("\nTraining data shape:", X_train.shape)
print("Validation data shape:", X_val.shape)

# Create baseline model
model = MultiOutputClassifier(
    LogisticRegression(max_iter=1000)
)

print("\nTraining baseline model...")
model.fit(X_train, y_train)

print("Training complete!")

# Predict probabilities
y_prob = model.predict_proba(X_val)

print("\nValidation ROC-AUC scores:")

for i, condition in enumerate(conditions):
    score = roc_auc_score(y_val[:, i], y_prob[i][:, 1])
    print(condition, ":", round(score, 4))

# Overall average
scores = []

for i in range(len(conditions)):
    score = roc_auc_score(y_val[:, i], y_prob[i][:, 1])
    scores.append(score)

print("\nAverage ROC-AUC:", round(np.mean(scores), 4))