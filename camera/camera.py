import time
from picamera2 import Picamera2
import cv2
from gpiozero import OutputDevice
from ultralytics import YOLO
import os

picam = Picamera2()
image_path = '/home/whyme/Final/lib/img.jpg'

def capture():
    print("capturing...")
    picam.start(show_preview=False)
    picam.capture_file(image_path)
    picam.stop()

def enhance(image):
    image = cv2.convertScaleAbs(image, alpha=0.7, beta=0)
    image = cv2.GaussianBlur(image, (3, 3), 0)
    return image

def detect(image_path):
    # load the model
    model = YOLO('yolov8n.pt')
    # load and process the image
    image = cv2.imread(image_path)
    image = enhance(image)
    # perform prediction - confidence threshold 9.25
    results = model.predict(source=image, save=True, conf=0.15, augment=True)
    # print detected objects and their confidence scores
    for result in results:
        boxes = result.boxes
        for box in boxes:
            class_id = int(box.cls[0])
            class_name = result.names[class_id]
            confidence = float(box.conf[0])
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            print(f"Detected {class_name} with confidence: {confidence:.2f}")
            if class_name.lower() in ["phone", "cell phone", "mobile phone"]:
                return True
    return False


def on_press(right_motor, left_motor):
    start = time.time()
    if os.path.exists(image_path):
        os.remove(image_path)
    capture()
    if detect(image_path) == True:
        print("yes")
        print("\non")
        right_motor.on()
        left_motor.on()
        time.sleep(0.5)
        print("\noff")
        right_motor.off()
        left_motor.off()
        phone = False
        print("\nthe time is: ")
        print(time.time()-start)
    else:
        print("no")
        print("\non")
        right_motor.on()
        left_motor.on()
        time.sleep(0.5)
        print("\noff")
        right_motor.off()
        left_motor.off()
        time.sleep(0.5)
        print("\non")
        right_motor.on()
        left_motor.on()
        time.sleep(0.5)
        print("\noff")
        right_motor.off()
        left_motor.off()
        print("\nthe time is: ")
        print(time.time()-start)
    time.sleep(0.5)

