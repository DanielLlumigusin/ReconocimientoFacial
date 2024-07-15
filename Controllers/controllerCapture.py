import sys
import os
from tkinter import Tk
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Screen.main_view import MainView

class ControllerCapture:
    def __init__(self, root, controllerMain):
        self.root = root
        self.current_view = None
        self.controllerMain = controllerMain

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
    controller.root.mainloop()
