import os
os.chdir("C:/Users/kastu/Desktop/Face Recognition")

names = []
files = os.listdir('Temp')
pathname = "data/All_Files"

for file in files:
  if "jpg" in file:
    names.append(f'{pathname}/{file}')

with open("train.txt", "w") as fp:
  for name in names:
    fp.write(name + "\n")

print(len(names))

# import shutil
# import os
#
# target = 'C:/Users/kastu/Desktop/Face Recognition/All_Files'
# source = 'C:/Users/kastu/Desktop/All_Files'
#
# files=os.listdir(source)
# for file in files:
#     shutil.copy2(os.path.join(source,file), target)
