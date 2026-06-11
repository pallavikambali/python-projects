import asyncio
import websockets
import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import joblib
import numpy as np
import json
import math
import base64

# Load your trained model
model = joblib.load("gesture_model.pkl")

# MediaPipe setup
base_options = python.BaseOptions(model_asset_path='hand_landmarker.task')
options = vision.HandLandmarkerOptions(
    base_options=base_options,
    num_hands=2
)
detector = vision.HandLandmarker.create_from_options(options)

gestures = {
    0: "I need help",
    1: "Hii/Hello",
    2: "Yes I agree with that",
    3: "Yes we did it!",
    4: "Pointing up/showing upside",
    5: "It is super ",
    6: "I am feeling happy.",
    7: "Go by this way(Left)",
    8: "Go by this way(Right)",
    9: "No I disagree with that"
}

HAND_CONNECTIONS = [
    (0,1),(1,2),(2,3),(3,4),
    (0,5),(5,6),(6,7),(7,8),
    (5,9),(9,10),(10,11),(11,12),
    (9,13),(13,14),(14,15),(15,16),
    (13,17),(17,18),(18,19),(19,20),
    (0,17)
]
hand_name = ""
async def stream(websocket): #socket.on('connection')
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    print("Client connected, starting stream...")

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
            result = detector.detect(mp_image)
            prediction = "No hand detected"
            confidence = 0.0
            if result.handedness:
             if(result.handedness[0][0].category_name=="Left"): 
              hand_name = "Right Hand" #because the image is flipped 
             else:hand_name = "Left Hand"
            h, w, _ = frame.shape

            if result.hand_landmarks:
                hand = result.hand_landmarks[0]

                # Draw landmarks on frame
                for lm in hand:
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    cv2.circle(frame, (cx, cy), 5, (255, 255, 0), -1)   # cyan dots

                # Draw connections
                for connection in HAND_CONNECTIONS:
                    start_idx, end_idx = connection
                    x1 = int(hand[start_idx].x * w)
                    y1 = int(hand[start_idx].y * h)
                    x2 = int(hand[end_idx].x * w)
                    y2 = int(hand[end_idx].y * h)
                    cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)  # blue lines

                # Feature extraction (same as test.py)
                wrist = hand[0]
                ref = hand[12]
                scale = math.sqrt((ref.x - wrist.x)**2 + (ref.y - wrist.y)**2)

                features = []
                for lm in hand:
                    x = (lm.x - wrist.x) / scale
                    y = (lm.y - wrist.y) / scale
                    features.extend([x, y])

                pred = model.predict([features])[0]
                proba = model.predict_proba([features])[0]
                confidence = float(np.max(proba))
                prediction = gestures.get(pred, str(pred))

            # Encode frame as JPEG → base64
            _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 70])
            frame_b64 = base64.b64encode(buffer).decode('utf-8')

            # Send both frame and prediction
            await websocket.send(json.dumps({
                "frame": frame_b64,
                "prediction": prediction,
                "confidence": round(confidence * 100, 2)
            }))

            await asyncio.sleep(0.033)  # ~30 FPS

    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")
    finally:
        cap.release()
        print("Camera released")

async def main():
    print("WebSocket server running on ws://localhost:8765")
    async with websockets.serve(stream, "localhost", 8765): #server.listen()
        await asyncio.Future()

asyncio.run(main())