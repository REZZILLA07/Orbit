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

print("Label co-occurrence:\n")

for i in range(len(conditions)):
    for j in range(i + 1, len(conditions)):
        condition1 = conditions[i]
        condition2 = conditions[j]

        count = ((labels[condition1] == 1) &
                 (labels[condition2] == 1)).sum()

        print(condition1, "+", condition2, ":", count)