import cv2
import dlib

def haarcascade(frame):

    detector = './algorithms/haarcascade_frontalface_default.xml'
    face_cascade = cv2.CascadeClassifier(detector)

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame_gray = cv2.equalizeHist(frame_gray)

    faces = face_cascade.detectMultiScale(frame_gray)
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2, cv2.LINE_AA)
    
    return frame


def dlibdetector(frame):
    
    detector = dlib.get_frontal_face_detector()
    face_detector = detector(frame)

    for face in face_detector:
        cv2.rectangle(frame, (face.left(), face.top()), (face.right(), face.bottom()), (255, 255, 255), 2, cv2.LINE_AA)

    return frame
