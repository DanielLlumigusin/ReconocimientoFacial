import sys
import os
from tkinter import Tk
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Screen.main_view import MainView
from util.camera_capture import capture_data

class ControllerCapture:
    def __init__(self, root, controllerMain):
        self.root = root
        self.current_view = None
        self.controllerMain = controllerMain
        self.show_capture_view()

    def show_capture_view(self):
        if self.current_view is not None:
            self.current_view.destroy()
        from Screen.capture_view import CaptureView
        self.current_view = CaptureView(self.root, self)

    def checkRadioButtons(self, emotion, num_capturas):
        print(f"Emoción seleccionada: {emotion}, Número de capturas: {num_capturas}")

    def switch_to_main_view(self):
        if self.current_view is not None:
            self.current_view.destroy()
        self.current_view = MainView(self.root, self.controllerMain)

# Ejecutar el controlador
if __name__ == "__main__":
    root = Tk()
    controller_main = None  # Placeholder para evitar error en ejecución directa
    controller = ControllerCapture(root, controller_main)
    root.mainloop()
