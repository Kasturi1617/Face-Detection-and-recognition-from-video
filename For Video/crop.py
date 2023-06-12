import cv2
import json
from PIL import Image

result = open('../result.json')
array = json.load(result)

for obj in array:
    filename = obj["filename"]
    for i in range(0, len(obj["objects"])):

        img = cv2.imread(f'../{filename}')
        # with Image.open(f'../{filename}') as img:
        height, width = img.shape[ :2]
        center_x = obj["objects"][i]["relative_coordinates"]["center_x"]
        center_y = obj["objects"][i]["relative_coordinates"]["center_y"]
        width_of_box = obj["objects"][i]["relative_coordinates"]["width"]
        height_of_box = obj["objects"][i]["relative_coordinates"]["height"]
        # dim = (center_x, center_y, width_of_box, height_of_box)
        # print()
        width_of_box = int(width_of_box * width)
        height_of_box = int(height_of_box * height)
        center_x = center_x * width
        center_y = center_y * height
        x_min = int(center_x - (width_of_box/2))
        y_min = int(center_y - (height_of_box/2))
        bbox = (x_min, y_min, width_of_box, height_of_box)
        # print(bbox)
        x, y, w, h = bbox
        cropped_img = img[y : y + h, x : x + w]
        image_name = filename.split("/")[1]
        output_path = f"C:/Users/kastu/Desktop/Face Recognition/darknet/darknet/build/darknet/x64/Cropped_Photos2/{i}_{image_name}"
        print(output_path)
        cv2.imwrite(output_path, cropped_img)
        # cv2.imshow("Cropped", cropped_img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows(0)
