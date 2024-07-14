import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Models.model import Model
from Screen.main_view import MainView
from Screen.secondary_view import SecondaryView
from Screen.capture_view import CaptureView
from Screen.training_view import TrainingView
from Screen.emotion_view import EmotionView
from tkinter import Tk

class Controller:
    def __init__(self):
        self.root = Tk()
        self.model = Model()
        self.current_view = None
        self.switch_to_main_view()

    def run(self):
        self.root.mainloop()

    def switch_to_main_view(self):
        if self.current_view is not None:
            self.current_view.destroy()
        self.current_view = MainView(self.root, self)

    def switch_to_secondary_view(self):
        if self.current_view is not None:
            self.current_view.destroy()
        self.current_view = SecondaryView(self.root, self)

    def capture_data(self):
        if self.current_view is not None:
            self.current_view.destroy()
        self.current_view = CaptureView(self.root, self)

    def train_data(self):
        if self.current_view is not None:
            self.current_view.destroy()
        self.current_view = TrainingView(self.root, self)

    def recognize(self):
        if self.current_view is not None:
            self.current_view.destroy()
        self.current_view = EmotionView(self.root, self)

if __name__ == "__main__":
    app = Controller()
    app.run()
