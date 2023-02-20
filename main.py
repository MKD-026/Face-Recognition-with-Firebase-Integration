import cv2
import os

imgBG = cv2.imread("Resources/background.png") #1280x720
folderPath = "Resources/Modes"
modePath = os.listdir(folderPath)

imgMode = []
for path in modePath:
    imgMode.append(cv2.imread(os.path.join(folderPath,path)))

cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)



while True:
    success, img = cam.read()
    img = cv2.flip(img, 1)

    imgBG[162: 162 + 480, 55: 55 + 640] = img
    imgBG[44: 44 + 633, 808: 808 + 414] = imgMode[1]
    cv2.imshow("Face Attendance System", imgBG)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()