import pandas as pd

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

print("Label distribution:\n")

for condition in conditions:
    positive = labels[condition].sum()
    negative = len(labels) - positive

    print(condition)
    print("Positive:", positive)
    print("Negative:", negative)
    print()