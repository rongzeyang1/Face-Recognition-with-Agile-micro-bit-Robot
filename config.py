"""
Configuration file for micro:bit face recognition robot
"""

# Robot settings
ROBOT_NAME = "FaceBot v1.0"
VERSION = "1.0.0"

# Face recognition settings
FACE_DETECTION_THRESHOLD = 0.7  # 70% confidence
MAX_FACES = 5
FRAME_WIDTH = 320
FRAME_HEIGHT = 240

# LED display settings
DISPLAY_BRIGHTNESS = 7  # 0-9
DISPLAY_TIMEOUT = 3000  # ms

# Security settings
HASH_ALGORITHM = "sha256"
ENCRYPTION_ENABLED = True

# Known faces mapping
KNOWN_FACES = {
    "Alice": "data/faces/alice_face.dat",
    "Bob": "data/faces/bob_face.dat",
    "Charlie": "data/faces/charlie_face.dat"
}

# Face to number mapping
FACE_NUMBER_MAPPING = {
    "Alice": 1,
    "Bob": 2,
    "Charlie": 3
}

# Robot movement settings
MOVE_FORWARD_SPEED = 512
TURN_SPEED = 300
MOVE_DURATION = 1000  # ms

# GPIO pin mappings (for Yahboom Tinybit Pro)
PIN_LEFT_MOTOR = pin0
PIN_RIGHT_MOTOR = pin1
PIN_CAMERA_TRIGGER = pin2
PIN_LED_CONTROL = pin8

# Network settings (if using companion device)
COMPANION_IP = "192.168.1.100"
COMPANION_PORT = 5000

# Debug settings
DEBUG_MODE = True
LOG_LEVEL = "INFO"  # DEBUG, INFO, WARNING, ERROR