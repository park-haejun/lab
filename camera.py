import numpy as np
import cv2

def showVideo():
    try:
        print('카메라를 구동합니다.')
        cap = cv2.VideoCapture(0)
    except:
        print('카메라 구동 실패')
        return
    # 화면의 크기 설정
    cap.set(3, 480)
    cap.set(4, 320)

    while True:
        ret, frame = cap.read()

        if not ret:
            print('비디오 읽기 오류')
            break

        gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('video', gray)
        cv2.imshow('original', frame)

        k = cv2.waitKey(1) & 0xFF
        if k ==27:
            break

    cap.release()
    cv2.destroyAllWindows()

showVideo()