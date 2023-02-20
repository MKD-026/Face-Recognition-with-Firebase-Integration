import cv2
import pickle
import face_recognition
import os

#Student images
folderPath = "Images"
pathList = os.listdir(folderPath)
#print(pathList)

imgList = []
studentIDs = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    studentIDs.append(os.path.splitext(path)[0])
#print(studentIDs)

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

print("Encoding started...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIDs = [encodeListKnown, studentIDs]
#print(encodeListKnown)
print("Encoding finished!")

#Saving file
file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIDs, file)
file.close()