import torch
import cv2
import os
import numpy as np
# array_of_img = []

# model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
# model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp7/weights/best.pt', force_reload=True)
model = torch.hub.load('ultralytics/yolov5', 'custom', path='cloudmodel/0data1000.pt', force_reload=True)

for filename in os.listdir("data/images"):
    img = cv2.imread("data/images" + "/" + filename)
    results = model(img)
    results.print()
    print(results.xyxy)
    cv2.imshow ('YOLO COCO', np. squeeze (results.render()))
    cv2.waitKey (0)
    # array_of_img.append(img)
    # print(array_of_img)
    
# model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
# model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp7/weights/best.pt', force_reload=True)
# model = torch.hub.load('ultralytics/yolov5', 'custom', path='cloudmodel/2data1603.pt', force_reload=True)
# print(model)
# img=cv2.imread('s.jpg')
# img=cv2.imread('data/images/clean_face.20210917165219.jpg')
# img=cv2.imread('data1/images/mask.20210918142439.jpg')
# img=cv2.imread('data2/images/pikacu.20210918192354.jpg')
# results = model(img)
# results.print()
# print(results.xyxy)
# cv2.imshow ('YOLO COCO', np. squeeze (results.render()))
# cv2.waitKey (0)