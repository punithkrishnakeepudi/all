#pip install ultralytics opencv-python

from ultralytics import YOLO
import cv2

# Load the YOLOv8 model (you can pick from yolov8n, yolov8s, yolov8m, yolov8l, yolov8x)
model = YOLO("yolov8n.pt")  # n = nano model (fastest, smallest)

# Define the objects you specifically want to label
target_objects = ["person", "car", "dog"]  # 👈 change this list as needed

# Load an image or start a video stream
cap = cv2.VideoCapture(0)  # 0 = webcam; or replace with a video file path

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLOv8 inference
    results = model(frame, stream=True)

    # Loop through detections
    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            conf = float(box.conf[0])

            # Filter for your specific objects
            if label in target_objects:
                # Get bounding box coordinates
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(
                    frame,
                    f"{label} {conf:.2f}",
                    (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6,
                    (0, 255, 0),
                    2
                )

    # Show the output
    cv2.imshow("YOLOv8 Object Detection", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
