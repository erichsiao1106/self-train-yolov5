import torch
import cv2
import numpy as np

model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
# model.conf = 0.5
# print(model)
img=cv2.imread('IMG_2997.JPG')
results = model(img)
results.print()
print(results.xyxy)
cv2.imshow('YOLO COCO', np.squeeze(results.render()))
cv2.waitKey(0)


