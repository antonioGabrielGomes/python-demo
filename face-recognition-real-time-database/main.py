import cv2
import os
import face_recognition
import pickle
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

imgBackground = cv2.imread('Resources/background.png')

folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []

for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

# load the encoding file
print("Loading the encoding file ...")
file = open('EncodeFile.p', 'rb')
encodeListKnowWithIds = pickle.load(file)
file.close()
encodeListKnow, studentIds = encodeListKnowWithIds
#print(studentIds)
print("Encode file loade")



while True:
    success, img = cap.read()

    if not success:
        break

    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)


    imgBackground[162:162+480,55:55+640] = img
    imgBackground[44:44+633,808:808+414] = imgModeList[3]


    for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnow, encodeFace)
        faceDistance = face_recognition.face_distance(encodeListKnow, encodeFace)
        # print("maches", matches)
        # print("faceDistance", faceDistance)


        matchIndex = np.argmin(faceDistance)
        # print("Match index", matchIndex)

        if matches[matchIndex]:
            print("Known Face Detected")


    # cv2.imshow("Webcam", img)    
    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)

#1:00:32   ->    https://www.youtube.com/watch?v=iBomaK2ARyI&list=WL&index=3&t=2830s
