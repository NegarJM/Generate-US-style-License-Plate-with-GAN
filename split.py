import os
from sklearn.model_selection import train_test_split
import shutil

# Paths to your datasets
dataset_path_1 = "./LicensePlateDataset/"
dataset_path_2 = "./LicensePlateDatasetOutlines/"

# Output paths for train, test, and val sets for both datasets
train_path_1 = "./LicensePlateDataset/train"
test_path_1 = "./LicensePlateDataset/test"
val_path_1 = "./LicensePlateDataset/validation"

train_path_2 = "./LicensePlateDatasetOutlines/train"
test_path_2 = "./LicensePlateDatasetOutlines/test"
val_path_2 = "./LicensePlateDatasetOutlines/validation"

# List all files in the datasets
all_files_1 = os.listdir(dataset_path_1)
all_files_2 = os.listdir(dataset_path_2)

# Split the datasets into train, test, and val sets
train_files_1, test_val_files_1 = train_test_split(
    all_files_1, test_size=0.2, random_state=42
)
test_files_1, val_files_1 = train_test_split(
    test_val_files_1, test_size=0.5, random_state=42
)

# Create directories for train, test, and val sets for both datasets
os.makedirs(train_path_1, exist_ok=True)
os.makedirs(test_path_1, exist_ok=True)
os.makedirs(val_path_1, exist_ok=True)

os.makedirs(train_path_2, exist_ok=True)
os.makedirs(test_path_2, exist_ok=True)
os.makedirs(val_path_2, exist_ok=True)

# Move files to their respective directories for both datasets
for file in train_files_1:
    # Check if the corresponding file exists in dataset 2
    corresponding_file_path_2 = os.path.join(dataset_path_2, file)
    if os.path.isfile(corresponding_file_path_2):
        shutil.move(
            os.path.join(dataset_path_1, file), os.path.join(train_path_1, file)
        )
        shutil.move(corresponding_file_path_2, os.path.join(train_path_2, file))

for file in test_files_1:
    corresponding_file_path_2 = os.path.join(dataset_path_2, file)
    if os.path.isfile(corresponding_file_path_2):
        shutil.move(os.path.join(dataset_path_1, file), os.path.join(test_path_1, file))
        shutil.move(corresponding_file_path_2, os.path.join(test_path_2, file))

for file in val_files_1:
    corresponding_file_path_2 = os.path.join(dataset_path_2, file)
    if os.path.isfile(corresponding_file_path_2):
        shutil.move(os.path.join(dataset_path_1, file), os.path.join(val_path_1, file))
        shutil.move(corresponding_file_path_2, os.path.join(val_path_2, file))

print("Datasets split into train, test, and val sets for both datasets.")
