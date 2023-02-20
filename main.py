import cv2
import os
import pickle
import numpy as np
import face_recognition

from utils import *

imgBG = cv2.imread("Resources/background.png") #1280x720
folderPath = "Resources/Modes"
modePath = os.listdir(folderPath)

imgMode = []
for path in modePath:
    imgMode.append(cv2.imread(os.path.join(folderPath,path)))

cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)

#ILoading Encoding file
print("Loading Encoded file...")
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIDs = pickle.load(file)
file.close()

encodeListKnown, studentIds = encodeListKnownWithIDs
print("Encode file loaded!")


while True:
    success, img = cam.read()
    img = cv2.flip(img, 1)
    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    imgBG[162: 162 + 480, 55: 55 + 640] = img
    imgBG[44: 44 + 633, 808: 808 + 414] = imgMode[1]

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)

    for encoFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encoFace)
        faceDistance = face_recognition.face_distance(encodeListKnown, encoFace)
        #print("Matches", matches)
        #print("Face Distance", faceDistance)

        matchIndex = np.argmin(faceDistance)
        #print("Match Index", matchIndex)

        if matches[matchIndex]:
            print("Known face detected :)")
            print(studentIds[matchIndex])
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1 #image offset since we using background
            imgBG = cornerRect(imgBG, bbox, rt=0)


    cv2.imshow("Face Attendance System", imgBG)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()