"""
Main program for micro:bit Face Recognition Robot
Controls the overall flow and integration of all modules
"""

import time
from microbit import *
from face_module import FaceRecognizer
from display_module import DisplayController
from security_module import DataProtector
from config import KNOWN_FACES, FACE_NUMBER_MAPPING

class RobotController:
    def __init__(self):
        """Initialize all components"""
        self.face_recognizer = FaceRecognizer()
        self.display = DisplayController()
        self.protector = DataProtector()
        self.running = True
        
        # Load known faces
        self.known_faces = {}
        self.load_known_faces()
        
        print("Robot initialized successfully")
        self.display.show_startup_animation()
    
    def load_known_faces(self):
        """Load pre-trained face encodings"""
        for name, encoding_path in KNOWN_FACES.items():
            encoding = self.face_recognizer.load_encoding(encoding_path)
            if encoding is not None:
                hashed_encoding = self.protector.hash_encoding(encoding)
                self.known_faces[name] = hashed_encoding
                print(f"Loaded face: {name}")
    
    def process_camera_frame(self):
        """
        Capture and process one frame from camera
        Returns: (face_detected, person_name, confidence)
        """
        # Simulate camera capture (replace with actual camera code)
        # In real implementation, use camera module
        frame = self.simulate_camera_capture()
        
        if frame is None:
            return False, None, 0
        
        # Detect faces in frame
        faces = self.face_recognizer.detect_faces(frame)
        
        if len(faces) == 0:
            return False, None, 0
        
        # Get first face
        face_encoding = self.face_recognizer.encode_face(faces[0])
        hashed_current = self.protector.hash_encoding(face_encoding)
        
        # Compare with known faces
        best_match = None
        best_confidence = 0
        
        for name, known_hash in self.known_faces.items():
            similarity = self.protector.compare_hashes(hashed_current, known_hash)
            if similarity > best_confidence and similarity > 0.7:  # 70% confidence threshold
                best_confidence = similarity
                best_match = name
        
        return True, best_match, best_confidence
    
    def simulate_camera_capture(self):
        """
        Simulate camera capture for testing
        Replace with actual camera code for Yahboom Tinybit Pro
        """
        # TODO: Integrate actual camera module
        # Return simulated image data
        return bytearray([0] * 100)  # Placeholder
    
    def run(self):
        """Main execution loop"""
        print("Starting face recognition robot...")
        
        while self.running:
            # Check for button press to stop
            if button_a.is_pressed() and button_b.is_pressed():
                print("Stopping robot...")
                self.running = False
                break
            
            # Process camera input
            face_detected, person_name, confidence = self.process_camera_frame()
            
            if face_detected and person_name:
                # Get number to display
                number = FACE_NUMBER_MAPPING.get(person_name, 0)
                
                # Display number on LED matrix
                self.display.show_number(number)
                
                # Log recognition
                print(f"Recognized: {person_name} -> Number {number} (Confidence: {confidence:.2f})")
                
                # Optional: Move robot or perform action
                self.perform_action(person_name)
            else:
                # Show question mark if face not recognized
                self.display.show_question_mark()
                print("No face recognized")
            
            # Delay between frames
            sleep(500)  # 0.5 seconds
    
    def perform_action(self, person_name):
        """Perform robot action based on recognized person"""
        # Example: Different movements for different people
        actions = {
            "Alice": self.move_forward,
            "Bob": self.turn_right,
            "Charlie": self.turn_left,
        }
        
        action = actions.get(person_name, self.stop_movement)
        action()
        sleep(300)  # Perform action for 0.3 seconds
        self.stop_movement()
    
    # Robot movement functions (placeholder - implement based on your hardware)
    def move_forward(self):
        """Move robot forward"""
        # pin0.write_analog(512)  # Example for motor control
        # pin1.write_analog(512)
        print("Moving forward")
    
    def turn_right(self):
        """Turn robot right"""
        print("Turning right")
    
    def turn_left(self):
        """Turn robot left"""
        print("Turning left")
    
    def stop_movement(self):
        """Stop all motors"""
        # pin0.write_analog(0)
        # pin1.write_analog(0)
        print("Stopped")

def main():
    """Entry point"""
    try:
        robot = RobotController()
        robot.run()
    except Exception as e:
        print(f"Error: {e}")
        display.show(Image.SAD)
    finally:
        display.clear()
        print("Program ended")

if __name__ == "__main__":
    main()