import os
import random

def select_random_files(folder_path, num_files):
    files = os.listdir(folder_path)
    num_files = min(num_files, len(files))
    selected_files = random.sample(files, num_files)
    return [os.path.join(folder_path, file) for file in selected_files]

folder_path = "clean_dataset/images"
num_files_to_select = 15

selected_files = select_random_files(folder_path, num_files_to_select)
print("Randomly selected files:")
for file in selected_files:
    print(file)


