import cv2
import dlib
from mtcnn.mtcnn import MTCNN

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

def mtcnndetector(frame):
    
    detector = MTCNN()
    face_detector = detector.detect_faces(frame)

    for face in face_detector:
        x, y, w, h = face['box']

        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2, cv2.LINE_AA)

    return frame

def OpenCVDNN(frame, net):

    blob = cv2.dnn.blobFromImage(frame, 1, (300, 300), (104, 177, 123))
    net.setInput(blob)

    detector = net.forward()
    detect = detector[0, 0, :, :]

    h, w = frame.shape[:2]

    for i in range(detect.shape[0]):
        confidence = detect[i, 2]
        if confidence < 0.5:
            break
        
        x1 = int(detect[i, 3] * w)
        y1 = int(detect[i, 4] * h)
        x2 = int(detect[i, 5] * w)
        y2 = int(detect[i, 6] * h)

        cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 255), 2, cv2.LINE_AA)

    return frame
