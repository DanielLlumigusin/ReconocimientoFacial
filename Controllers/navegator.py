# navegator.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class Navegator:
    def __init__(self):
        self.current_screen = None

    def switch_to_capture_view(self):
        from Screen.captureScreen import CaptureScreen
        if self.current_screen:
            self.current_screen.destroy()
        self.current_screen = CaptureScreen(self)

    def switch_to_train_view(self):
        from Screen.trainScreen import TrainScreen
        if self.current_screen:
            self.current_screen.destroy()
        self.current_screen = TrainScreen(self)
        
    def switch_to_emotion_view(self):
        from Screen.emotionScreen import EmotionScreen
        if self.current_screen:
            self.current_screen.destroy()
        self.current_screen = EmotionScreen(self)
        
    def switch_to_credits_view(self):
        from Screen.creditsScreen import CreditsScreen
        if self.current_screen:
            self.current_screen.destroy()
        self.current_screen = CreditsScreen(self)
    
    def switch_to_main_view(self):
        from Screen.menuScreen import MenuScreen
        if self.current_screen:
            self.current_screen.destroy()
        self.current_screen = MenuScreen(self)
        self.current_screen.mainloop()