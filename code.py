import face_recognition
import cv2
import pyttsx3

#recognition of knownface in the team

known_image = face_recognition.load_image_file("akash.jpg")
known_encoding = face_recognition.face_encodings(known_image)[0]

#intiallizing the required varibles

password_attempts = 0
max_attempts = 3
warning = pyttsx3.init()

#function to record and store the face of thief

def capture_face():
    image_capture = cv2.VideoCapture(0)
    _, frame = image_capture.read()
    image_capture.release()
    cv2.imwrite("captured1.jpg", frame)
   # cv2.imshow("captured_face", frame)

#giving warning to the thief

def warn():
    warning.say("leave my device orelse, you are prohibited !")
    warning.runAndWait()

#logic to capture the thief face and warn the thief
    
while password_attempts < max_attempts:
    password = input("Enter password:")

    if password == "jaibalaya":
        print("Akash Login successful")
        warning.say("good job Akaash, your successfully logged into your device ")
        warning.runAndWait()
        break
    warning.say("Akaash please kindly enter your correct password")
    warning.runAndWait()
    password_attempts += 1
    
  
    if password_attempts == max_attempts:
        capture_face()
        warn()
        print("you can't hide your face damn")
        break
        
    else:
        print('Incorrect password! Attempts left:- {}' .format(max_attempts-password_attempts))



