import cv2
import mediapipe
import pyautogui

cap = cv2.VideoCapture(0)
hand_detector = mediapipe.solutions.hands.Hands()
drawing_utils = mediapipe.solutions.drawing_utils
while True:
    _, frame = cap.read()
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand)
    cv2.imshow('Virtual mouse', frame)
    cv2.waitKey(1)
