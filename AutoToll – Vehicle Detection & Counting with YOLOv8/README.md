## Project Objective
Develop an automated toll monitoring system that uses YOLOv8 to detect vehicles in highway footage and track their direction to compute inflow and outflow counts at a toll booth.

## Overview
AutoToll leverages the real-time object detection capabilities of [YOLOv8](https://github.com/ultralytics/ultralytics) to identify vehicles in video streams. Each frame is analysed to determine whether a vehicle crosses a reference line, enabling the project to maintain separate counts for inbound and outbound traffic. The repository provides a Jupyter Notebook that demonstrates the entire workflow and produces an annotated video summarising the traffic.

## Features
- Detects multiple vehicle classes in recorded or live video.
- Differentiates inbound and outbound traffic using a configurable reference line.
- Produces an annotated output video and per-class counts.

## Getting Started
### Clone the repository
```bash
git clone https://github.com/Pavankumarmanagoli/Projects.git
cd "Projects/AutoToll – Vehicle Detection & Counting with YOLOv8"
```

### Install dependencies
Install the required Python packages. A virtual environment is recommended.
```bash
pip install ultralytics opencv-python numpy pandas matplotlib seaborn ipython
```

### Run the notebook
Launch Jupyter Notebook and open `automatictollbooth.ipynb`. The notebook is organised into sections that:
1. load the pretrained YOLOv8 model and the source video,
2. process frames to detect and classify vehicles,
3. update inflow/outflow counters and save an annotated video to `results/predicted_result.mp4`.

### Example script
The core detection logic can also be used in a Python script:
```python
from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture("input/highway.mp4")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
    results = model(frame)[0]
    cv2.imshow("AutoToll", results.plot())
    if cv2.waitKey(1) == 27:  # press Esc to exit
        break

cap.release()
cv2.destroyAllWindows()
```
Replace `yolov8n.pt` with a custom model if training on specific data.

## Methodology
1. Capture and optionally resize each frame using OpenCV.
2. Apply YOLOv8 to obtain bounding boxes, classes, and confidence scores.
3. Compute the centre of each detection and draw bounding boxes.
4. Compare the centre to a user-defined reference line to determine vehicle direction.
5. Maintain per-class inflow and outflow counts with dictionaries.

## Results
![Transformed Output Frame](results/final_result.jpg)

[Transformed Output Video](results/predicted_result.mp4)

## Future Work
- Calculate total toll revenue for each direction.
- Estimate vehicle speed and emission levels.
- Identify the most common vehicle type per direction.

## Conclusion
YOLOv8 offers fast and accurate vehicle detection suitable for traffic analytics and automated tolling. AutoToll demonstrates how these capabilities can be integrated into a practical counting system and serves as a foundation for more advanced monitoring solutions.
