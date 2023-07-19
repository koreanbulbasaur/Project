import cv2
import mediapipe as mp
import numpy as np
import time
from PIL import ImageFont, ImageDraw, Image
import random

# 나눔글꼴(.ttf) 파일 경로
font_path = r'C:\Windows\Fonts\NanumGothic.ttf'  # 사용하는 폰트 파일명에 맞게 수정

max_num_hands = 1
gesture = {
    0:'rock', 1:'', 2:'', 3:'', 4:'', 5:'paper',
    6:'', 7:'', 8:'', 9:'scissors', 10:'ok',
}
rps_gesture = {0:'rock', 5:'paper', 9:'scissors', 10:'ok'}
options = ["rock", "scissors", "paper"]

# MediaPipe hands model
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands=max_num_hands,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)

# Gesture recognition model
file = np.genfromtxt('gesture_train.csv', delimiter=',')
angle = file[:,:-1].astype(np.float32)
label = file[:, -1].astype(np.float32)
knn = cv2.ml.KNearest_create()
knn.train(angle, cv2.ml.ROW_SAMPLE, label)

cap = cv2.VideoCapture(0)

cv2.namedWindow('Game', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Game', 800, 800)

# 기본값들 설정
countdown = False

title = True

count_start = False

game_start_bool = False

user_choice = None

computer_choice = None

border_color = (0, 0, 0)

# 프로젝트 동영상 저장
fourcc = cv2.VideoWriter_fourcc(*'DIVX')

width = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

out = cv2.VideoWriter('output.avi', fourcc, fps, (width, height))

# 이미지 불러오기
ai = cv2.imread('./img/ai.png')
ai_smile = cv2.imread('./img/ai_smile.jpg')
ai_ggang = cv2.imread('./img/ai_ggang.png')
cloud = cv2.imread('./img/cloud.png', cv2.IMREAD_UNCHANGED)

# 이미지 사이즈 조절
resize = (150, 150)
ai = cv2.resize(ai, resize)
ai_smile = cv2.resize(ai_smile, resize)
ai_ggang = cv2.resize(ai_ggang, resize)
cloud = cv2.resize(cloud, (600, 150))

# 투명 이미지 적용
def overlay(frame, x, y, w, h, overlay_image):
    overlay_image_resized = cv2.resize(overlay_image, (w, h))
    alpha = overlay_image_resized[:, :, 3]
    mask_image = alpha / 255.0

    for c in range(0, 3): # channel BGR
        frame[y:y+h, x:x+w, c] = (overlay_image_resized[:, :, c] * mask_image) + (frame[y:y+h, x:x+w, c] * (1 - mask_image))

# 랜덤 색깔
def bgr():
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    red = random.randint(0, 255)
    return blue, green, red

# 헥사 코드 -> bgr
def hex_to_bgr(hex_value):
    hex_value = hex_value.upper()

    # Hex 값을 16진수로 해석하여 RGB 값으로 추출
    red = int(hex_value[0:2], 16)
    green = int(hex_value[2:4], 16)
    blue = int(hex_value[4:6], 16)
    
    # BGR 형식으로 변환
    bgr_value = (blue, green, red)
    
    return bgr_value

# ok 사인을 표현하라는 글 표시
def title_show(frame):
    text = 'ok 사인을 표현하면 \n게임이 시작됩니다!'
    position = (280, 640)
    font_size = 50
    font_color = hex_to_bgr('54fbd9')
    border_thickness = 2

    frame_with_text = put_text_with_korean(frame, text, position, font_path, 
                                           font_size, font_color, border_color, 
                                           border_thickness)
    return frame_with_text

# 한글 표현 함수
def put_text_with_korean(frame, text, position, font_path, font_size, font_color, border_color, border_thickness):
    # PIL 이미지로 변환
    pil_image = Image.fromarray(frame)
    draw = ImageDraw.Draw(pil_image)

    # 폰트 설정
    font = ImageFont.truetype(font_path, font_size)

    # 텍스트의 외곽선 그리기
    for dx in range(-border_thickness, border_thickness + 1):
        for dy in range(-border_thickness, border_thickness + 1):
            draw.text((position[0] + dx, position[1] + dy), text, font=font, fill=border_color)

    # 한글 텍스트 그리기
    draw.text(position, text, font=font, fill=font_color)

    # 다시 OpenCV 이미지로 변환
    frame = np.array(pil_image)

    return frame

# 가위, 바위, 보
def start_countdown(frame, start_time):
    show_time = int(time.time() - start_time)

    if show_time == 1:
        count_hand = '가위'
    elif show_time == 2:
        count_hand = '바위'
    elif show_time == 3:
        count_hand = '보'
    else:
        count_hand = ''

    position = (400, 600)
    font_size = 140
    font_color = hex_to_bgr('e25556')
    border_thickness = 2

    frame_with_text = put_text_with_korean(frame, count_hand, position, font_path, 
                                        font_size, font_color, border_color, 
                                        border_thickness)
    return frame_with_text

while cap.isOpened():
    ret, frame = cap.read()

    # 화면 좌우 대칭
    frame = cv2.flip(frame, 1)

    if not ret:
        continue

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    result = hands.process(frame)

    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    frame = cv2.resize(frame, (800, 800))

    if result.multi_hand_landmarks is not None:

        for res in result.multi_hand_landmarks:

            joint = np.zeros((21, 3))
            for j, lm in enumerate(res.landmark):
                joint[j] = [lm.x, lm.y, lm.z]

            # Compute angles between joints
            v1 = joint[[0,1,2,3,0,5,6,7,0,9,10,11,0,13,14,15,0,17,18,19],:] # Parent joint
            v2 = joint[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],:] # Child joint
            v = v2 - v1 # [20,3]
            # Normalize v
            v = v / np.linalg.norm(v, axis=1)[:, np.newaxis]

            # Get angle using arcos of dot product
            angle = np.arccos(np.einsum('nt,nt->n',
                v[[0,1,2,4,5,6,8,9,10,12,13,14,16,17,18],:], 
                v[[1,2,3,5,6,7,9,10,11,13,14,15,17,18,19],:])) # [15,]

            angle = np.degrees(angle) # Convert radian to degree

            # Inference gesture
            data = np.array([angle], dtype=np.float32)
            ret, results, neighbours, dist = knn.findNearest(data, 3)
            idx = int(results[0][0])

            # Draw gesture result
            if idx in gesture.keys():
                center_x = 80
                center_y = 410
                cv2.putText(frame, text=gesture[idx].upper(), 
                            org=(int(res.landmark[0].x * frame.shape[1]) - center_x, int(res.landmark[0].y * frame.shape[0] - center_y)), 
                                fontFace=cv2.FONT_HERSHEY_SIMPLEX, 
                                fontScale=1, color=(0, 0, 0), 
                                thickness=5)
                cv2.putText(frame, text=gesture[idx].upper(), 
                            org=(int(res.landmark[0].x * frame.shape[1]) - center_x, int(res.landmark[0].y * frame.shape[0] - center_y)), 
                                fontFace=cv2.FONT_HERSHEY_SIMPLEX, 
                                fontScale=1, color=(0, 0, 255), 
                                thickness=2)

    # ai 사진
    frame[625:775, 5:155] = ai

    # 말풍선 사진
    overlay(frame, 200, 625, 550, 150, cloud)

    if title:
        frame = title_show(frame)

    if gesture[idx] == 'ok' and not countdown:
        print('ok')
        start_time = time.time()
        title = False
        countdown = True

    if countdown:
        frame = start_countdown(frame, start_time)

    cv2.imshow('Game', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

cap.release()
cv2.destroyAllWindows()