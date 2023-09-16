import face_recognition
import cv2
import pyttsx3

#recognition of knownface in the team
#class akash:

known_image = face_recognition.load_image_file("known_face.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

#intiallizing the required varibles

password_attempts = 0
max_attempts = 3
engine = pyttsx3.init()

#function to record and store the face of thief

def capture_face():
    video_capture = cv2.VideoCapture(0)
    _, frame = video_capture.read()
    video_capture.release()
    cv2.imwrite("captured1.jpg", frame)
   # cv2.imshow("captured_face", frame)

#playing sound you like

def play_alert():
    engine.say("charan fucker leave my device ")
    engine.runAndWait()

#logic to capture the thief face
    
while password_attempts < max_attempts:
    password = input("Enter password:")

    if password == "jaibalaya":
        print("Login successful")
        break
    password_attempts += 1
  
    if password_attempts == max_attempts:
        play_alert()
        capture_face()
        print("Donga dhorikesadu roiii")
        break
    else:
        print("Incorrect password! Attempts left: {max_attempts - password_attempts}")
