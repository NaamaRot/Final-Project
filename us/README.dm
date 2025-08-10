
---

**`modules/us/README.md`**
```markdown
# Ultrasonic Sensor Module

This module handles:
- Reading distances from multiple ultrasonic sensors
- Determining closest object direction (left, right, or center)
- Generating vibration patterns based on proximity

## Functions
- `get_min_distance(sub_mode)` — Returns minimum distance and direction.
- `get_timers(distance, sub_mode)` — Returns vibration ON/OFF durations.
- `vibrate_side(timers, motor)` — Vibrates one motor.
- `vibrate(timers, motor1, motor2)` — Vibrates both motors.
