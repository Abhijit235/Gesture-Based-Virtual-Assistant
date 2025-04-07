import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

def detect_gesture(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)
    fingers = 0

    if results.multi_hand_landmarks:
        for hand_landmark in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(image, hand_landmark, mp_hands.HAND_CONNECTIONS)

            finger_tips = [8, 12, 16, 20]  # index to pinky
            for tip in finger_tips:
                if hand_landmark.landmark[tip].y < hand_landmark.landmark[tip - 2].y:
                    fingers += 1

            if hand_landmark.landmark[4].x > hand_landmark.landmark[3].x:  # thumb
                fingers += 1

    return fingers, image
