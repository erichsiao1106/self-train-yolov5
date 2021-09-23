import cv2
from time import strftime
import os
# labels = ['glass','phone','mask','clean_face']
# labels = ['Good_boy','phone_forbid']
labels = ['hat','mask','seed','pikacu']
cap = cv2.VideoCapture(0)

while cap.isOpened():
    success, frame = cap.read()
    cv2.imshow('get pic', frame)

    keyb = cv2.waitKey(100) & 0xFF
    if keyb == 27:
        break
    elif keyb == ord('0') or keyb == ord('1') or keyb == ord('2') or keyb == ord('3'):
    # elif keyb == ord('0') or keyb == ord('1') :
        print(keyb - 48)
        systime = strftime("%Y%m%d%H%M%S")
        # imgname = os.path.join('data/images', labels[keyb - 48] + '.' + systime + '.jpg')
        imgname = os.path.join('data2/images', labels[keyb - 48] + '.' + systime + '.jpg')
        cv2.imwrite(imgname, frame)
cap.release()
cv2.destroyAllWindows()