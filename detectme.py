import torch
import numpy as np
import cv2

# model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
# model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp5/weights/best.pt', force_reload=True)
model = torch.hub.load('ultralytics/yolov5', 'custom', path='cloudmodel/last2.pt', force_reload=True)

cap = cv2.VideoCapture(0)
while cap.isOpened():
    success,frame = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue
    results = model(frame)
    cv2.imshow('YOLO COCO 01', np.squeeze(results.render()))
    if cv2.waitKey (1) & 0xFF==27:
        break
cap.release ()
cv2.destroyAllWindows()