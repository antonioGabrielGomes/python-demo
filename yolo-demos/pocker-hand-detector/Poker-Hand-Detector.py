import math

from ultralytics import YOLO
import cv2
import cvzone
import PockerHandFunction 

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

model = YOLO('../Yolo-Weights/playingCards.pt')

className = [
    '10C', '10D', '10H', '10S', '2C', 
    '2D', '2H', '2S', '3C', '3D', 
    '3H', '3S', '4C', '4D', '4H', 
    '4S', '5C', '5D', '5H', '5S', 
    '6C', '6D', '6H', '6S', '7C', 
    '7D', '7H', '7S', '8C', '8D', 
    '8H', '8S', '9C', '9D', '9H', 
    '9S', 'AC', 'AD', 'AH', 'AS', 
    'JC', 'JD', 'JH', 'JS', 'KC', 
    'KD', 'KH', 'KS', 'QC', 'QD', 
    'QH', 'QS'
]



while True:
    success, frame = cap.read()
    results = model(frame, stream=True)
    hand = []

    if not success:
        break

    for r in results:
        boxes = r.boxes
        for box in boxes:
            # Bounding Box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w, h = x2-x1, y2-y1
            bounding_box = int(x1), int(y1), int(w), int(h)
            cvzone.cornerRect(frame, bounding_box)
            # Confidence
            conf = math.ceil((box.conf[0]*100))/100
            # Class Name
            class_name = box.cls[0]

            cvzone.putTextRect(frame, f'{className[int(class_name)]} {conf}',
                               (max(0, x1), max(35, y1)),
                               scale=1, thickness=3)
            
            if conf > 0.5:
                hand.append(className[int(class_name)])

    print(hand)
    hand = list(set(hand))
    print(hand)


    if len(hand) == 5:
        results = PockerHandFunction.findPokerHand(hand)
        cvzone.putTextRect(frame, f'Your Hand: {results}', (300, 75), scale=3, thickness=5)
        print(results)

    cv2.imshow("image", frame)
    cv2.waitKey(1)