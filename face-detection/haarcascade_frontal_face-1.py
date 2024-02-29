import cv2
import sys

url_img = "datasets/9.jpg"

haar_file = "./Cascades/haarcascade_frontalface_default.xml"

image = cv2.imread(cv2.samples.findFile(url_img))

image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

if image is None:
    sys.exit("Could not read the image.")

# deteccao 
detector_facial = cv2.CascadeClassifier(haar_file)

# image = cv2.resize(image, (width, height)) 

deteccoes = detector_facial.detectMultiScale(image_gray, 1.1, 5)

for x, y, w, h in deteccoes:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0,255,255), 5)
    # cv2.rectangle(image_gray, (x, y), (x + w, y + h), (0,255,255), 5)


cv2.imwrite(f"result-haar.png", image)
