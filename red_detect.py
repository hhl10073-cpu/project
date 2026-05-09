import cv2
import numpy as np

# 1. 이미지 로드 (파일명이 똑같아야 합니다!)
image = cv2.imread('sample.jpg') 

# 이미지가 제대로 불러와졌는지 확인하는 코드 (추가함)
if image is None:
    print("에러: 'sample.jpg' 파일을 찾을 수 없습니다. 폴더를 확인해 주세요!")
else:
    # 2. BGR에서 HSV 색상 공간으로 변환
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 3. 빨간색 범위 지정 (두 개의 범위를 설정해야 함)
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    # 4. 마스크 생성
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2 # 두 개의 마스크를 합침

    # 5. 원본 이미지에서 빨간색 부분만 추출
    result = cv2.bitwise_and(image, image, mask=mask)

    # 6. 결과 이미지 출력
    cv2.imshow('Original', image)
    cv2.imshow('Red Filtered', result)

    print("아무 키나 누르면 창이 닫힙니다.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()