# Face Detection
동영상 얼굴 추출 기술을 비교하기 위한 문서입니다.

## Algorithm
- OpenCV Haar Cascade
- Dlib Frontal Face Detector
- MTCNN
- SSD
- OpenCV DNN Face Detector

## 문서 구조
```
├── README.md                                           - README 파일
│   
├── algorithms/                                         - Face Detection 알고리즘
│   ├── haarcascade_frontalface_default.xml             - OpenCV Haar Cascade 알고리즘
│   ├── res10_300x300_ssd_iter_140000_fp16.caffemodel   - SSD 알고리즘
│   ├── deploy.prototxt                                 - SSD 알고리즘 config 파일
│   ├── opencv_face_detector_uint8.pb                   - OpenCV DNN Face Detector 알고리즘 
│   └── opencv_face_detector.pbtxt                      - OpenCV DNN Face Detector 알고리즘 config 파일
├── videos/                                             - test를 위한 video 파일 폴더
│   ├── test1.mp4
│   └── test2.mp4
├── detectors.py                                        - detector 함수 정의
└── main.py                                             - 파일 실행 함수
```

## 사용법
```
# 적용하고 싶은 알고리즘
python main.py [-d] {h, d, m, s, o}
- "h" : OpenCV Haar Cascade, 
- "d" : Dlib Frontal Face Detector,
- "m" : MTCNN,
- "s" : SSD,
- "o" : OpenCV DNN Face Detector
- default : 'h'

python main.py [--video_number] 숫자
- 알고리즘을 적용하고 싶은 videos 파일 속 동영상의 순번을 적는다.
- default : '0'

python main.py [--video_name] 파일명
- 알고리즘을 적용하고 싶은 videos 파일 속 동영상 이름을 적는다.
- default : None
```

## reference
- [face_detection_comparison](https://github.com/kairess/face_detection_comparison)