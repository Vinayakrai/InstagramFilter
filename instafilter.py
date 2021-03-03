import cv2 as cv
import numpy as np
import dlib
from math import hypot

cap=cv.VideoCapture(0)
cap.set(10, 100)
nose_image=cv.imread("Resources/rabbit.jpg")
detector=dlib.get_frontal_face_detector()
predictor=dlib.shape_predictor("Resources/shape_predictor_68_face_landmarks.dat")

while True:
    success, frame=cap.read()
    gray_frame=cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces=detector(frame)
    for face in faces:
        landmarks=predictor(gray_frame, face)
        top_nose=(landmarks.part(29).x, landmarks.part(29).y)
        center_nose=(landmarks.part(30).x, landmarks.part(30).y)
        left_nose=(landmarks.part(31).x, landmarks.part(31).y)
        right_nose = (landmarks.part(35).x, landmarks.part(35).y)
        nose_width=int(hypot(left_nose[0]- right_nose[0], left_nose[1]-right_nose[1])*1.1)
        nose_height = int(nose_width * 1.67)   #Seen the Ratio Image Size 920*550, Ratio=1.67
        top_left=(int(center_nose[0]-nose_width/2),
                             int(center_nose[1]-nose_height/2))
        bottom_right=(int(center_nose[0]+nose_width/2),
                      int(center_nose[1]+nose_height/2))
        nose_pig=cv.resize(nose_image, (nose_width,nose_height))
        nose_pig_gray=cv.cvtColor(nose_pig, cv.COLOR_BGR2GRAY)
        _, nose_mask=cv.threshold(nose_pig_gray, 25, 255, cv.THRESH_BINARY)
        nose_area=frame[top_left[1]: top_left[1]+nose_height,
                  top_left[0]:top_left[0]+nose_width]
        nose_area_no_nose=cv.bitwise_and(nose_area, nose_area, mask= nose_mask)
        final_nose=cv.add(nose_area_no_nose, nose_pig)
        frame[top_left[1]: top_left[1] + nose_height,
        top_left[0]:top_left[0] + nose_width]=final_nose

    cv.imshow("Frame", frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break