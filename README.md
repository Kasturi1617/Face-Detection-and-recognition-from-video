# Face-Detection-and-recognition-from-video
This project aims to develop an efficient and accurate computer vision system capable of detecting and recognizing multiple human faces in images and videos. It uses Yolov4 object detection algorithm and the darknet neural network framework, to achieve real-time performance. 

# Proposed method: using YOLOv4

* A famous deep learning based model YOLOv4 is used for face detection.
* It is the fourth version in the You Only Look Once family of models.
* The original YOLO (You Only Look Once) was written by Joseph Redmon in a custom framework called darknet.
* YOLOv4 is developed by three developers Alexey Bochkovskiy, Chien-Yao Wang, and Hong-Yuan Mark Liao.
* YOLOv4 is thought for its fast and green real-time face/item detection capabilities.
* It follows an easy and simple structure in comparison to different face detection methods.
* YOLOv4 can detect more than one faces in an image accurately.
* YOLOv4 model is known for its high accuracy, speed and flexibility. 
* YOLO is based on a single Convolutional Neural Network (CNN)

## YOLOv4 architecture and working:

YOLOv4 architecture mainly consists of three parts:
I. Backbone: "backbone" is initial part of the neural network that is responsible for extracting high-level features from the input data. It is typically a convolutional neural network (CNN) architecture that performs the initial processing of the input data, capturing low-level and mid-level features.

II. Neck: the "neck" refers to the intermediate component of the architecture that connects the backbone network to the detection head. It collects feature maps from different stages of the backbone and then mixes and combines them to prepare for the next step.

III. Head: The main function of face detection which is locating bounding boxes and performing classification, is performed by head.

![image](https://github.com/Kasturi1617/Face-Detection-and-recognition-from-video/assets/96917574/b9823f90-1da1-4b59-9093-f70cd33d24d9)



