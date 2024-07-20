import cv2
import mediapipe as mp
import pyautogui as pt

cap = cv2.VideoCapture(0)
detect_hand = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils
screen_width , screen_hieght = pt.size()
index_y = 0
while True:
    ret , frame = cap.read()
    frame = cv2.flip(frame , 1)
    rgb_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    frame_height , frame_width , _ = frame.shape
    output = detect_hand.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame , hand)
            landmarks = hand.landmark
            for id , landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width )
                y = int(landmark.y * frame_height)
            
                if id == 8:
                    cv2.circle(img=frame , center= (x,y), radius=20 , color=(0 , 0 , 0))
                    index_x = screen_width / frame_width * x
                    index_y = screen_hieght / frame_height * y
                    pt.moveTo(index_x , index_y)
                if id == 4:
                    cv2.circle(img=frame , center= (x,y), radius=20 , color=(0 , 0 , 0))
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_hieght / frame_height * y
                    if abs(index_y - thumb_y) < 50:
                        print("click")
                        pt.click()
                        pt.sleep(2)
    cv2.imshow("gesture recognize" , frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break