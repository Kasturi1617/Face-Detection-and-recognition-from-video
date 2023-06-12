import os

filePath = "Photos2/"

all_photos = os.listdir("../Photos2")

with open('Test.txt', 'w') as fp:
    for photo in all_photos:
        fp.write(f'{filePath}{photo}\n')
