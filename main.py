import cv2
import requests

url = 'https://localhost:4578/ems/face/'

def fun():
 is_face_detected = False
 # Load the cascade
 face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read the input image
 video = cv2.VideoCapture(0)
 _, img = video.read()

 # Convert into grayscale
 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 

# Detect faces
 faces = face_cascade.detectMultiScale(gray, 1.1, 4)
 

# Draw rectangle around the faces
 for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    if (w != 0):
            is_face_detected = True
    else:
            is_face_detected = False
 cv2.imshow('img', img)
 cv2.waitKey(1000)

 print(is_face_detected)
 myobj = {'isFaceDetected': is_face_detected}
 x = requests.post(url, data = myobj)

 
# Display the output
while True:
 fun()
 cv2.waitKey(300000)  #five minutes
