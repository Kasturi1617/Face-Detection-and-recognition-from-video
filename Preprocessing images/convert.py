import os
from PIL import Image
file = open('new_annotations.txt', 'rt')
content = file.read()

chunks = content.split('\n')
i = 0
classList = []

while i < len(chunks):
    folder_name = chunks[i].split('/')[0]
    name_of_file = chunks[i].split('/')[1]
    class_name = folder_name.split('--')[0]
    file_name = name_of_file.split('.')[0]
    final_file_name = file_name + ".txt"
    no_of_object = int(chunks[i + 1])

    print(chunks[i])

    i = i + 1

    if(class_name == '59'):
        folder_name = "59--people_driving_car"

    # with open('classes.txt', 'a') as cf:
    #     if folder_name.split('--')[1] not in classList:
    #         classList.append(folder_name.split('--')[1])
    #         cf.write(folder_name.split('--')[1] + "\n")
    # cf.close()

    with open(f'images/{folder_name}/{final_file_name}', 'w') as fp:
        with Image.open(f'images/{folder_name}/{file_name}.jpg') as img:
            width,height = img.size
            list = []

            while no_of_object:
                i = i + 1
                no_of_object = no_of_object - 1
                list = chunks[i].split(' ')
                xmin=int(list[0])
                xmax=int(list[0])+int(list[2])
                ymin=int(list[1])
                ymax=int(list[1])+int(list[3])
                cx=(xmin+xmax)/2
                cy=(ymin+ymax)/2
                cx=cx/width
                cy=cy/height
                if cx == 0:
                    cx = 0.001
                if cy == 0:
                    cy = 0.001
                w=int(list[2])/width
                h=int(list[3])/height
                fp.write(f'0 {cx} {cy} {w} {h}\n')
        fp.close()

    i = i + 1
    if i < len(chunks) and 'jpg' not in chunks[i]:
        i = i + 1
