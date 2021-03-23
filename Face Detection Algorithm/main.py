import os
import cv2
import argparse
import time
from detectors import *

parser = argparse.ArgumentParser(description='Select face detector which you want to use')
parser.add_argument('--detector', '-d', choices=['h','d','m', 's', 'o'], help='''
                        "h" : OpenCV Haar Cascade, 
                        "d" : Dlib Frontal Face Detector,
                        "m" : MTCNN,
                        "s" : SSD,
                        "o" : OpenCV DNN Face Detector
                        ''',
                    default='h')
parser.add_argument('--video_number',
                    help='Select the Nth video for face detection.', type=int, default=0)
parser.add_argument('--video_name',
                    help='Input your video name for face detection.', default=None)

args = parser.parse_args()

video_number = args.video_number

video_name = None
if args.video_name is not None:
    video_name = args.video_name

file_path = './videos/'
abs_path = os.path.abspath(file_path)
if video_name is not None:
    video_path = os.path.join(abs_path, video_name)
else:
    video = os.listdir(abs_path)[video_number]
    video_path = os.path.join(abs_path, video)

cap = cv2.VideoCapture(video_path)

detector = args.detector
frame_count, t = 0, 0

model = {
    'h':'haar',
    'd': 'dlib',
    'm': 'mtcnn',
    's': 'SSD',
    'o': 'DNN'
}

if detector == 's':
    model_path = './algorithms/res10_300x300_ssd_iter_140000_fp16.caffemodel'
    config_path = './algorithms/deploy.prototxt'
    net = cv2.dnn.readNet(model_path, config_path)
else:
    model_path = './algorithms/opencv_face_detector_uint8.pb'
    config_path = './algorithms/opencv_face_detector.pbtxt'
    net = cv2.dnn.readNet(model_path, config_path)


while True:
    ret, frame = cap.read()
    if ret is None:
        break

    frame_count += 1
    start_time = time.time()

    frame = cv2.resize(frame, dsize=None, fx=0.75, fy=0.75)
    
    if detector == 'h':
        frame = haarcascade(frame)
    if detector == 'd':
        frame = dlibdetector(frame)
    if detector == 'm':
        frame = mtcnndetector(frame)
    if detector in ('s', 'o'):
        frame = OpenCVDNN(frame, net)
    
    t += time.time() - start_time
    fps = frame_count / t
    cv2.putText(frame, 'FPS(%s): %.2f' % (model[detector], fps), (
        10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
    
    cv2.imshow('frame', frame)

    if cv2.waitKey(10) == 27:
        break
    
cap.release()
cv2.destroyAllWindows()
