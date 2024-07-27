import cv2
import os
import numpy as np
import time
import threading
import queue

class ControllerEmotion:
    def __init__(self, root, controllerMain):
        self.root = root
        self.current_view = None
        self.controllerMain = controllerMain
        self.show_emotion_view()

    def show_emotion_view(self):
        if self.current_view is not None:
            self.current_view.destroy()
        from Screen.emotion_view import EmotionView
        self.current_view = EmotionView(self.root, self)