import cv2
import dlib
import numpy as np
from time import sleep

# 얼굴 검출기 초기화
detector = dlib.get_frontal_face_detector()
# 얼굴 및 눈 검출을 위한 dlib의 face landmark predictor 로딩
predictor_path = 'shape_predictor_68_face_landmarks.dat'
predictor = dlib.shape_predictor(predictor_path)

# 웹캠 열기
cap = cv2.VideoCapture(0)
# 이미지 저장을 위한 변수 초기화
frame_count = 0

# 눈동자 중심 좌표 이동 평균을 위한 큐 초기화
left_eye_center_queue = []
right_eye_center_queue = []
queue_size = 5  # 큐 크기


while True:
    # 프레임 읽기
    ret, frame = cap.read()
    # 그레이스케일 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img_gray_gaussian = cv2.GaussianBlur(gray, (5, 5), 0)  # 가우시안 필터 적
    # 얼굴 검출
    faces = detector(img_gray_gaussian)

    for face in faces:
        # 얼굴에서 눈 영역 찾기
        landmarks = predictor(gray, face)

        left_eye_pts = []
        right_eye_pts = []

        for n in range(36, 42):  # 왼쪽 눈 랜드마크 인덱스: 36 ~ 41
            x, y = landmarks.part(n).x, landmarks.part(n).y
            left_eye_pts.append((x, y))

        for n in range(42, 48):  # 오른쪽 눈 랜드마크 인덱스: 42 ~ 47
            x, y = landmarks.part(n).x, landmarks.part(n).y
            right_eye_pts.append((x, y))

        # 눈 영역 추출
        left_eye_region = np.array(left_eye_pts, np.int32)
        right_eye_region = np.array(right_eye_pts, np.int32)

        # 눈동자 추정을 위해 ROI 설정
        left_eye_roi = gray[min(left_eye_region[:, 1]):max(left_eye_region[:, 1]),
                       min(left_eye_region[:, 0]):max(left_eye_region[:, 0])]
        right_eye_roi = gray[min(right_eye_region[:, 1]):max(right_eye_region[:, 1]),
                        min(right_eye_region[:, 0]):max(right_eye_region[:, 0])]

        # 눈동자 검출
        _, left_eye_thresh = cv2.threshold(left_eye_roi, 40, 255, cv2.THRESH_BINARY)
        _, right_eye_thresh = cv2.threshold(right_eye_roi, 40, 255, cv2.THRESH_BINARY)

        # 가장 어두운 부분 찾기
        left_eye_dark_region = np.unravel_index(np.argmin(left_eye_roi), left_eye_roi.shape)
        right_eye_dark_region = np.unravel_index(np.argmin(right_eye_roi), right_eye_roi.shape)

        # 눈동자 영역 그리기
        cv2.circle(frame, (min(left_eye_region[:, 0]) + left_eye_dark_region[1],
                           min(left_eye_region[:, 1]) + left_eye_dark_region[0]), 2, (0, 255, 0), -1)

        cv2.circle(frame, (min(right_eye_region[:, 0]) + right_eye_dark_region[1],
                           min(right_eye_region[:, 1]) + right_eye_dark_region[0]), 2, (0, 255, 0), -1)

        # 눈동자 중심 좌표 계산
        left_eye_center = (min(left_eye_region[:, 0]) + left_eye_dark_region[1],
                           min(left_eye_region[:, 1]) + left_eye_dark_region[0])
        right_eye_center = (min(right_eye_region[:, 0]) + right_eye_dark_region[1],
                            min(right_eye_region[:, 1]) + right_eye_dark_region[0])

        # 이동 평균을 적용하여 흔들림 보정
        left_eye_center_queue.append(left_eye_center)
        right_eye_center_queue.append(right_eye_center)

        if len(left_eye_center_queue) > queue_size:
            left_eye_center_queue.pop(0)
        if len(right_eye_center_queue) > queue_size:
            right_eye_center_queue.pop(0)

        left_eye_center_smoothed = np.mean(left_eye_center_queue, axis=0)
        right_eye_center_smoothed = np.mean(right_eye_center_queue, axis=0)

        # 보정된 눈동자 중심 좌표 출력
        print(f'Left Eye Center: {left_eye_center_smoothed},  Right Eye Center: {right_eye_center_smoothed}')
        if 260 <= left_eye_center_smoothed[0] <= 310:
            print("O")
            sleep(0.5)
        else :
            print("X")
            sleep(0.5)


    # 화면에 출력
    cv2.imshow('Eye Tracking', frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # 프레임 카운트 증가
    frame_count += 1

# 종료
cap.release()
cv2.destroyAllWindows()