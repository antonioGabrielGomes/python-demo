import cv2
import face_recognition
import pickle
import os 
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import  storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "",
    'storageBucket': ""
})

# Importing student images
folderPath = 'Images'
pathList = os.listdir(folderPath)

# print(f"folderPath: {folderPath}")
# print(f"pathList: {pathList}")

imgList = []
studentIds = []
for path in pathList:
    img = cv2.imread(os.path.join(folderPath, path))

    imgList.append(img) # image path
    studentIds.append(os.path.splitext(path)[0]) # image name only  abcd.png => abcd
    
    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

   

def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_encodings(img)

        if len(face_locations) > 0: 
            encode = face_locations[0]
            encodeList.append(encode)

    return encodeList


print("Encoding Started ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")

file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File Saved")