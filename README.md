# alchemist-ai-fastapi-v2
Alchemist 서비스 중 타이머를 자동으로 멈춰주는 기능입니다.  
5분에 한번씩 5초동안 5장의 사진을 찍어 API를 호출하면  
AI가 타이머 stop 여부를 결정합니다.

## 작동 알고리즘
```
1. client에서 5장의 사진을 5초에 걸쳐 찍음.
2. AI API를 호출하여 5장의 사진을 input.
3. files 파라미터가 비어있는지 확인.
    3-1. 비어있으면 400 Error 반환.
    3-2. 비어있지 않으면 4번 진행.
4. server에서 keypoint mask R-CNN Model이 사람을 Detect.
    4-1. 만약 사람이 없으면 400 Error 반환.
    4-2. 사람이 있으면 5번으로 진행.
5. server에서 CNN Model이 자세를 Classifity.
    5-1. 만약 공부하고 있으면 200 OK 반환 후 client에서 5분 뒤 다시 호출.
    5-2. 만약 자고 있으면 400 Error 반환.
```

## Installation
```
$ git clone https://github.com/dsm-alchemist/alchemist-ai-fastapi-v2.git
$ cd alchemist-ai-fastapi-v2

$ docker pull taki0412/alchemist-timer
$ docker run -it -d -p 8080:8080 --name "alchemist-timer" taki0412/alchemist-timer
```

## QUICK_START
```
$ git clone https://github.com/dsm-alchemist/alchemist-ai-fastapi-v2.git
$ cd alchemist-ai-fastapi-v2
$ pip3 install -r requrements.txt
$ python3 main.py
```