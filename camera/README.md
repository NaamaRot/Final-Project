
---

## **2. Module READMEs**

**`modules/camera/README.md`**
```markdown
# Camera Module

This module handles:
- Capturing images from the Pi Camera
- Enhancing images using OpenCV
- Detecting objects using YOLO (via Ultralytics library)

## Functions
- `capture()` — Captures and saves an image.
- `enhance(image)` — Applies brightness/contrast adjustment and Gaussian blur.
- `detect(image_path)` — Runs YOLO detection on the given image file.
- `on_press(right_motor, left_motor)` — Integrates camera capture and detection with motor feedback.
