import sys
import os
from tkinter import Tk
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Models.model import Model
from Screen.main_view import MainView
from Screen.credits_view import CreditsView
from Screen.capture_view import CaptureView
from Screen.training_view import TrainingView
from Screen.emotion_view import EmotionView
from controllerCapture import ControllerCapture

class Controller:
    def __init__(self, root):
        self.root = root
        self.model = Model()
        self.current_view = None
        self.controllerCapture = ControllerCapture(root, self)
        self.switch_to_main_view()

    def run(self):
        self.root.mainloop()

    def switch_to_main_view(self):
        if self.current_view is not None:
            self.current_view.destroy()
        self.current_view = MainView(self.root, self)

    def switch_to_capture_view(self):
        if self.current_view is not None:
            self.current_view.destroy()
        self.current_view = CaptureView(self.root, self.controllerCapture)

    def switch_to_training_view(self):
        if self.current_view is not None:
            self.current_view.destroy()
        self.current_view = TrainingView(self.root, self)

    def switch_to_emotion_view(self):
        if self.current_view is not None:
            self.current_view.destroy()
        self.current_view = EmotionView(self.root, self)

    def switch_to_credits_view(self):
        if self.current_view is not None:
            self.current_view.destroy()
        self.current_view = CreditsView(self.root, self)
        
if __name__ == "__main__":
    root = Tk()
    app = Controller(root)
    app.run()
