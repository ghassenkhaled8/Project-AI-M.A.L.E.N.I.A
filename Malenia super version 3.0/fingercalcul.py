import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

tip_ids = [4, 8, 12, 16, 20]
total_fingers = 0

try:
    with mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5) as hands:
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            results = hands.process(img_rgb)
            img = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2BGR)

            fingers = []
            if results.multi_hand_landmarks:
                for hand_landmark, handedness in zip(results.multi_hand_landmarks, results.multi_handedness):
                    lm_list = [[lm.x, lm.y, lm.z] for lm in hand_landmark.landmark]
                    hand_label = handedness.classification[0].label
                    if hand_label == 'Left':
                        is_left = True
                    else:
                        is_left = False

                    if lm_list[tip_ids[0]][0] > lm_list[tip_ids[0]-1][0] if is_left else lm_list[tip_ids[0]][0] < lm_list[tip_ids[0]-1][0]:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                    for id in range(1, 5):
                        if lm_list[tip_ids[id]][1] < lm_list[tip_ids[id]-2][1]:
                            fingers.append(1)
                        else:
                            fingers.append(0)

                    total_fingers = fingers.count(1)

                    if total_fingers < 0:
                        total_fingers = 0
                    elif total_fingers > 10:
                        total_fingers = 10

                    cv2.rectangle(img, (20, 300), (200, 425), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, str(total_fingers), (35, 375), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 5)

                    mp_draw.draw_landmarks(img, hand_landmark, mp_hands.HAND_CONNECTIONS)

            else:
                # Display message when hand is not detected
                cv2.putText(img, "No hand detected", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            cv2.imshow("Hand Tracking", img)

            if cv2.waitKey(1)==ord('q') :
                break

        cap.release()
        cv2.destroyAllWindows()

except Exception as e:
    print(f"Error: {e}")