import pandas as pd
from skmultilearn.model_selection import iterative_train_test_split

dataset_path = r"C:\Users\Havisha\Downloads\Chest_xrays\Chest_xrays"
labels_path = dataset_path + r"\train_labels.csv"

labels = pd.read_csv(labels_path)

conditions = [
    "Atelectasis",
    "Effusion",
    "Infiltration",
    "Nodule",
    "Pneumothorax"
]

# Image names
X = labels[["Image Index"]].values

# Labels
y = labels[conditions].values

# 80% training, 20% validation
X_train, y_train, X_val, y_val = iterative_train_test_split(
    X, y, test_size=0.2
)

# Create dataframes
train_data = pd.DataFrame(X_train, columns=["Image Index"])
train_data[conditions] = y_train

val_data = pd.DataFrame(X_val, columns=["Image Index"])
val_data[conditions] = y_val

# Save the splits
train_data.to_csv("train_split.csv", index=False)
val_data.to_csv("validation_split.csv", index=False)

print("Training samples:", len(train_data))
print("Validation samples:", len(val_data))

print("\nSaved:")
print("train_split.csv")
print("validation_split.csv")