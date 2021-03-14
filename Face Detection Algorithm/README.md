# Face Detection
동영상 얼굴 추출 기술을 비교하기 위한 문서입니다.

## Algorithm
- Haar Cascade

## 문서 구조
```
├── README.md                               - 리드미 파일
│
├── algorithms/                             - Face Detection 알고리즘
│   └── haarcascade_frontalface_default.xml     - haarcascade 알고리즘
├── videos/                                 - test를 위한 video 파일 폴더
│   ├── test1.mp4
│   └── test2.mp4
├── detectors.py                            - detector 함수 정의
└── main.py                                 - 파일 실행 함수
```

## 사용법
```
# 적용하고 싶은 알고리즘
python main.py [-d] {h, d}
- h : haar-cascade
- d : dlib
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