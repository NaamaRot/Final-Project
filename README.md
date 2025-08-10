# Final-Project
Python code for a wearable navigation and object detection system with haptic feedback for deafblind users.
---
# Python Code for Haptic Visual Sensor (HVS)
This repository contains only the **Python code modules** for HVS, a wearable assistive device designed for individuals with combined vision and hearing impairments. The code integrates object recognition, distance measurement, and haptic feedback control, enabling real-time obstacle avoidance and environmental awareness.
---
## Links to Modules and Their Purpose
- [Main Controller](main/main.py) - orchestrates inputs, controls modes, and manages shutdown.
- [Camera Module](camera/camera.py) - captures images, enhances them, and detects specific objects using YOLOv8n.
- [Ultrasonic Sensor Module](us/us.py) - reads distances from multiple sensors and controls vibration feedback.
