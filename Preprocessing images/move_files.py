# import shutil
# import os
# destination_directory = 'All_Files'
#
# directories = os.listdir("images")
#
# for directory in directories:
#     shutil.copy(f'images/{directory}', destination_directory)

import os
import shutil
source = os.getcwd() + "/images"
destination = os.getcwd() + "/Temp"
source_files = os.listdir(source)

for file_name in source_files:
    all_file = os.listdir(os.path.join(source,file_name))
    for file in all_file:
        full_file_name = os.path.join(os.path.join(source,file_name), file)
        shutil.copy(full_file_name, destination)
