#เปิดกล้อง opencv
from tkinter import Frame
import cv2

cap = cv2.VideoCapture(1)
cap2 = cv2.VideoCapture(0)
while (True):
    check , frame = cap.read()
    check , frame1 = cap2.read()
    cv2.imshow("Output1",frame1)
    cv2.imshow("Output",frame)
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break

cap.release()
cv2.destroyAllwindow()
