"""
Display controller for micro:bit LED matrix
"""

from microbit import display, Image
import time

class DisplayController:
    def __init__(self):
        """Initialize display"""
        self.current_display = None
    
    def show_number(self, number):
        """Display number on LED matrix"""
        if 0 <= number <= 9:
            display.show(str(number))
        else:
            display.show("?")
        
        self.current_display = number
    
    def show_question_mark(self):
        """Display question mark"""
        question_mark = Image("00900:"
                             "09090:"
                             "00900:"
                             "00000:"
                             "00900")
        display.show(question_mark)
    
    def show_face_icon(self):
        """Display face icon"""
        face = Image("00000:"
                    "09090:"
                    "00000:"
                    "90009:"
                    "09990")
        display.show(face)
    
    def show_checkmark(self):
        """Display checkmark for successful recognition"""
        check = Image("00000:"
                     "00001:"
                     "00010:"
                     "10100:"
                     "01000")
        display.show(check)
        time.sleep(0.5)
    
    def show_xmark(self):
        """Display X mark for failed recognition"""
        xmark = Image("10001:"
                     "01010:"
                     "00100:"
                     "01010:"
                     "10001")
        display.show(xmark)
        time.sleep(0.5)
    
    def show_startup_animation(self):
        """Display startup animation"""
        frames = [
            Image.HEART,
            Image.HEART_SMALL,
            Image.SMILE,
            Image.HAPPY
        ]
        
        for frame in frames:
            display.show(frame)
            time.sleep(0.3)
        
        display.clear()
    
    def show_countdown(self, seconds=3):
        """Display countdown"""
        for i in range(seconds, 0, -1):
            display.show(str(i))
            time.sleep(1)
    
    def clear(self):
        """Clear display"""
        display.clear()
        self.current_display = None
    
    def show_custom_pattern(self, pattern_string):
        """
        Display custom pattern
        pattern_string: 25 characters, 0=off, 9=on
        Example: "99999" * 5 for all on
        """
        if len(pattern_string) == 25:
            image = Image(pattern_string)
            display.show(image)