
# YOLO Object Detection Using Python

A computer vision project that detects objects in an image using a pretrained YOLOv8 Nano model and OpenCV.

## Features

- Detects multiple objects in an image
- Uses a pretrained YOLOv8 Nano model
- Displays bounding boxes and class labels
- Shows the annotated image in an OpenCV window

## Technologies Used

- Python
- Ultralytics YOLO
- OpenCV
- Computer Vision
- Deep Learning

## Project Files

- `app.py` - Main object detection program
- `image.jpg` - Input image
- `yolov8n.pt` - YOLOv8 Nano model weights
- `requirements.txt` - Python dependencies

## Installation

1. Clone the repository:

   git clone https://github.com/akshatagurnale/YOLO-Object-Detection.git

2. Navigate to the project directory:

   cd YOLO-Object-Detection

3. Create a virtual environment:

   python -m venv myenv

4. Activate the environment on Windows:

   myenv\Scripts\activate

5. Install the dependencies:

   pip install -r requirements.txt

## Usage

Run the application:

python app.py

The program loads the input image, performs object detection, and displays the image with detected objects and bounding boxes.

Press any key while the result window is active to close it.

## Model

YOLOv8 Nano (`yolov8n.pt`)

The model detects objects from the classes included in its pretrained dataset.

## Limitations

- Detection accuracy depends on image quality and object visibility.
- The pretrained model recognizes only the classes it was trained to detect.
- Performance depends on the hardware and image size.

## Author

AKSHATA GURNALE
