import os
import shutil
import random
from pathlib import Path
from PIL import Image

images = []
filepath = "All_Files"
AllFiles = os.listdir(filepath)

for file in AllFiles:
    if 'jpg' in file:
        names = file.split('.')[0]
        images.append(names)
    shutil.copy(f'All_Files/{file}', f"Temp/{file}")
#
# print(images)
size_of_images = len(images)
test_images = []
size_of_test_images = int((size_of_images) * 0.3)

while size_of_test_images > 0:
    index = int(random.random() * size_of_images)
    if index not in test_images:
        test_images.append(index)
        size_of_test_images = size_of_test_images - 1

for index in test_images:
    # shutil.copy(f'Temp/{images[index]}.jpg', 'Temp/Test')
    # shutil.copy(f'Temp/{images[index]}.txt', 'Temp/Test')
    # os.remove(f'Temp/{images[index]}.jpg')
    # os.remove(f'Temp/{images[index]}.txt')
    with open('test.txt', 'a') as test:
        test.write(f'data/All_Files/{images[index]}.jpg\n')

with open('train.txt', 'a') as train:
    for i in range(0, len(images)):
        if i not in test_images:
            train.write(f'data/All_Files/{images[i]}.jpg\n')
            # shutil.copy(f'Temp/{images[i]}.jpg', 'Temp/Train')
            # shutil.copy(f'Temp/{images[i]}.txt', 'Temp/Train')
            # os.remove(f'Temp/{images[i]}.jpg')
            # os.remove(f'Temp/{images[i]}.txt')
