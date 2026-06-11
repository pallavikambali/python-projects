import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import csv
import math
import time

# ========== MODEL SETUP ==========
base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')

options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=1
)

detector = vision.HandLandmarker.create_from_options(options)

cap = cv2.VideoCapture(0)

# ========== LABEL MAP ==========
labels = {
    ord('0'): 0,
    ord('1'): 1,
    ord('2'): 2,
    ord('3'): 3,
    ord('4'): 4,
    ord('5'): 5,
    ord('6'): 6,
    ord('7'): 7,
    ord('8'): 8,
    ord('9'): 9,
}

# cooldown to prevent multiple saves per press
last_save_time = 0
cooldown = 0.5  # seconds

# ========== MAIN LOOP ==========
while cap.isOpened():
    ret, frame = cap.read()
    if not ret: #stops if camera feed is not available
        break

    frame = cv2.flip(frame, 1) #mirror the frame
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
    result = detector.detect(mp_image) #detects hand landmarks in the frame
    key = cv2.waitKey(1) & 0xFF #captures key presses

    if key == ord('q'):
        break

    if key in labels and result.hand_landmarks:# if we have both key and hand marks
        current_time = time.time()

        # debounce
        if current_time - last_save_time > cooldown:
            label = labels[key]

            for hand in result.hand_landmarks:
                wrist = hand[0]
                ref = hand[12]

                scale = math.sqrt((ref.x - wrist.x)**2 + (ref.y - wrist.y)**2) #dis bw wrist and middle finger tip is used as refresnce so diff hand size doesnt change the prediction

                row = [label]

                for lm in hand:
                    x = (lm.x - wrist.x) / scale
                    y = (lm.y - wrist.y) / scale
                    row.extend([x, y])

                with open("gesture_data.csv", "a", newline="") as f:
                    writer = csv.writer(f)
                    writer.writerow(row)

                print(f"Saved ONE sample for label {label}")
                last_save_time = current_time

                cv2.putText(frame, f"Saved: {label}", (10, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Collecting Data", frame)

cap.release()
cv2.destroyAllWindows()