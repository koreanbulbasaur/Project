import cv2
import mediapipe as mp
import numpy as np
import time
from PIL import ImageFont, ImageDraw, Image
import random

# 나눔글꼴(.ttf) 파일 경로
font_path = r'C:\Windows\Fonts\NanumGothic.ttf'  # 사용하는 폰트 파일명에 맞게 수정

# 한글 폰트 로드
strat_num_size = 300
start_num_font = ImageFont.truetype(font_path, strat_num_size)

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

countdown = False

title_show = True

count_start = False

game_start_bool = False

user_choice = None

computer_choice = None

def start(img):
    remaining_time = int(3 - (time.time() - start_time))
    
    # 한글 텍스트 그리기
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    start_num_position = (int(img.shape[0]/2), int((img.shape[1]/2)-strat_num_size))

    draw.text(start_num_position, str(remaining_time), font=start_num_font, fill=(0, 0, 255))

    img = np.array(img_pil)

    return img

def game_count(img, start_time):
    show_time = int(time.time() - start_time)

    if show_time == 4:
        show_hand = '가위'
    elif show_time == 5:
        show_hand = '바위'
    elif show_time == 6:
        show_hand = '보'
    else:
        show_hand = ''

    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)

    strat_num_size = 200
    start_num_font = ImageFont.truetype(font_path, strat_num_size)

    start_num_position = (10, 0)

    draw.text(start_num_position, str(show_hand), font=start_num_font, fill=(0, 0, 255))

    img = np.array(img_pil)

    return img

def game_start(img, user_choice, computer_choice, game_start_time):
    if user_choice == computer_choice:
        result = 'Tie'
        color = (255, 0, 0)

    elif (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock"):
        result = 'WIN'
        color = (0, 255, 0)

    else:
        result = 'Lose'
        color = bgr()

    cv2.putText(img, result, (int(img.shape[1]/2), int(img.shape[0]/2)), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 8, cv2.LINE_AA)
    cv2.putText(img, result, (int(img.shape[1]/2), int(img.shape[0]/2)), cv2.FONT_HERSHEY_SIMPLEX, 2, color, 5, cv2.LINE_AA)
    cv2.putText(img, f'computer : {computer_choice}', (0, 400), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 8, cv2.LINE_AA)
    cv2.putText(img, f'computer : {computer_choice}', (0, 400), cv2.FONT_HERSHEY_SIMPLEX, 2, color, 5, cv2.LINE_AA)

    game_start_end_time = time.time() - game_start_time
    if game_start_end_time <= 3:
        return img, True, game_start_end_time
    else:
        return img, False, game_start_end_time
    
def bgr():
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    red = random.randint(0, 255)
    return blue, green, red

while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        continue

    img = cv2.flip(img, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    result = hands.process(img)

    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

    if title_show:
        cv2.putText(img, 
                    'Show the OK sign and Start playing',
                    (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 0), 5, cv2.LINE_AA)
        cv2.putText(img, 
                    'Show the OK sign and Start playing',
                    (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, bgr(), 2, cv2.LINE_AA)

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
                cv2.putText(img, text=gesture[idx].upper(), 
                            org=(int(res.landmark[0].x * img.shape[1]), int(res.landmark[0].y * img.shape[0] + 20)), 
                                fontFace=cv2.FONT_HERSHEY_SIMPLEX, 
                                fontScale=1, color=(0, 0, 0), 
                                thickness=5)
                cv2.putText(img, text=gesture[idx].upper(), 
                            org=(int(res.landmark[0].x * img.shape[1]), int(res.landmark[0].y * img.shape[0] + 20)), 
                                fontFace=cv2.FONT_HERSHEY_SIMPLEX, 
                                fontScale=1, color=(0, 0, 255), 
                                thickness=2)

            
            if gesture[idx] == 'ok' and not countdown:
                print('ok')
                start_time = time.time()
                countdown = True

            # mp_drawing.draw_landmarks(img, res, mp_hands.HAND_CONNECTIONS)

    if countdown:
        title_show = False
        img = start(img)
        count_start = True

    if count_start and time.time() - start_time >= 3.:
        countdown = False
        img = game_count(img, start_time)
        if time.time() - start_time >= 7:
            user_choice = gesture[idx]
            computer_choice = random.choice(options)
            game_start_bool = True
            game_start_time = time.time()

    if game_start_bool:
        count_start = False
        print(user_choice)
        img, _, game_start_end_time = game_start(img, user_choice, computer_choice, game_start_time)
        if game_start_end_time >= 4:
            game_start_bool = False
            title_show = True

    cv2.imshow('Game', img)
    if cv2.waitKey(1) == ord('q'):
        break