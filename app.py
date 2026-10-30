from ultralytics import YOLO
import cv2

#Load YOLOv8 pre-trained model
model = YOLO("yolov8n.pt")

# Read the image
image = cv2.imread("image.jpg")

# Run object detection
result = model(image)

# Display results
annotated_image = result[0].plot()
cv2.imshow("YOLO Object Detection", annotated_image)

# Wait until key press
cv2.waitKey(0)
cv2.destroyAllWindows()