import cv2
import numpy as np
import serial
import time
import torch

# Initialize serial port for Arduino communication
ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

# Load a pre-trained YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

def detect_bottle(frame):
    results = model(frame)
    bottles = results.xyxy[0][results.xyxy[0][:, -1] == 39]
    if len(bottles) > 0:
        x1, y1, x2, y2 = int(bottles[0, 0]), int(bottles[0, 1]), int(bottles[0, 2]), int(bottles[0, 3])
        center = ((x1+x2)//2, (y1+y2)//2)
        return (x1, y1, x2, y2), center
    return None, None

def calculate_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def main():
    cap = cv2.VideoCapture(4)
    ideal_state = None
    last_time = time.time()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        if ser.in_waiting:
            line = ser.readline().decode('utf-8').strip()
            if line == "reset":
                ideal_state = None
                print("Ideal position reset, setting new position.")

        bbox, center = detect_bottle(frame)
        if bbox:
            cv2.rectangle(frame, bbox[:2], bbox[2:], (255, 0, 0), 2)
            if ideal_state is None:
                if time.time() - last_time > 3:
                    ideal_state = center
                    print("Ideal state set.")
                    ser.write(b'ideal\n')  # Buzzer on
            else:
                cv2.circle(frame, ideal_state, 5, (0, 255, 0), -1)
                distance = calculate_distance(center, ideal_state)
                if distance < 50:
                    print("Bottle back to ideal state")
                    ser.write(b'ideal\n')  # Buzzer on
                else:
                    direction = ""
                    ser.write(b'off\n')  # Turn off buzzer, prepare for LEDs
                    if abs(center[0] - ideal_state[0]) > 50:
                        direction += "left" if center[0] < ideal_state[0] else "right"
                    if abs(center[1] - ideal_state[1]) > 50:
                        direction += ("" if direction == "" else ",") + "up" if center[1] < ideal_state[1] else "down"
                    print(f"Direction: {direction}")
                    ser.write(f"{direction}\n".encode())
        else:
            last_time = time.time()

        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

