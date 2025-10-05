This project demonstrates a complete real-time computer vision pipeline built using OpenCV, YOLOv8, and MediaPipe.
It combines image processing, object detection, and pose estimation to enable intelligent human–AI interaction for IoT, robotics, and smart systems.

The process starts with OpenCV, which captures frames from a webcam or video source and performs preprocessing such as resizing, color conversion, and normalization. These cleaned frames are then passed into YOLO (You Only Look Once), a state-of-the-art deep learning model that detects and labels multiple objects within a single image in real time. YOLO outputs bounding boxes and confidence scores for each detected object.

Once objects like “person” are identified, the frames are further analyzed using MediaPipe, a lightweight framework by Google that tracks human body landmarks such as joints, face features, and hand positions. MediaPipe’s pose detection model extracts 33 body keypoints, allowing the system to recognize movements, gestures, or posture changes.

The final stage of the pipeline uses these detections to trigger custom logic — for example, counting fitness reps, controlling robotic arms, or enabling gesture-based interfaces.

This integration allows OpenCV to handle low-level image processing, YOLO to manage high-level object understanding, and MediaPipe to interpret fine-grained human motion — resulting in a seamless AI vision workflow.

In short,

OpenCV handles “seeing”,
YOLO handles “understanding what’s seen”, and
MediaPipe handles “understanding how it’s moving”.

Together, they form a powerful and efficient computer vision stack suitable for modern AI-driven applications like fitness tracking, gesture control, surveillance, and robotic automation.
