from tkinter import *
from tkinter import ttk
from styles import setup_styles
from Controllers.navegator import Navegator
import cv2
import os
import time
import threading
import numpy as np
import queue

class TrainScreen(Tk):
    def __init__(self, navigator):
        super().__init__()
        self.navigator = navigator
        self.title("Entrenar Emociones")
        self.geometry("768x576")
        
        # Configurar estilos
        setup_styles()
        
        # Inicializar widgets
        self.frm = ttk.Frame(self, padding=10)
        self.titleLabel = ttk.Label(self.frm, text="¡Entrenamiento!", style="Title.TLabel")
        self.descriptionLabel = ttk.Label(self.frm, text="Pulsa el botón para entrenar")
        self.messageLabel = ttk.Label(self.frm, text="")
        self.buttonTrain = ttk.Button(self.frm, text="Entrenar Datos", style="Train.TButton", command=self.train)
        self.back_button = ttk.Button(self.frm, text="Regresar", style="Custom.TButton", command=self.navigator.switch_to_main_view)
        
        # Configurar layout
        self.frm.grid(column=0, row=0, sticky=(N, S, E, W))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.frm.columnconfigure(0, weight=1)
        self.frm.rowconfigure(4, weight=1)

        # Dibujar widgets
        self.titleLabel.grid(column=0, row=0, pady=10, padx=75)
        self.descriptionLabel.grid(column=0, row=1, pady=10)
        self.messageLabel.grid(column=0, row=2, pady=10)
        self.buttonTrain.grid(column=0, row=3, pady=10)
        self.back_button.grid(column=0, row=4, pady=10, sticky=(S, E))

        # Inicializar cola de mensajes
        self.queue = queue.Queue()

    def obtener_modelo(self, method, faces_data, labels):
        if method == 'EigenFaces':
            emotion_recognizer = cv2.face.EigenFaceRecognizer_create()
        elif method == 'FisherFaces':
            emotion_recognizer = cv2.face.FisherFaceRecognizer_create()
        elif method == 'LBPH':
            emotion_recognizer = cv2.face.LBPHFaceRecognizer_create()

        print(f"Entrenando ({method})...")
        inicio = time.time()
        emotion_recognizer.train(faces_data, np.array(labels))
        tiempo_entrenamiento = time.time() - inicio
        print(f"Tiempo de entrenamiento ({method}): {tiempo_entrenamiento}")

        emotion_recognizer.write(f"modelo{method}.xml")

    def train_models(self, queue):
        data_path = 'DataSet'
        emotions_list = os.listdir(data_path)
        print('Lista de emociones:', emotions_list)

        labels = []
        faces_data = []
        label = 0

        for name_dir in emotions_list:
            emotions_path = os.path.join(data_path, name_dir)
            for file_name in os.listdir(emotions_path):
                labels.append(label)
                faces_data.append(cv2.imread(os.path.join(emotions_path, file_name), 0))
            label += 1

        self.obtener_modelo('EigenFaces', faces_data, labels)
        self.obtener_modelo('FisherFaces', faces_data, labels)
        self.obtener_modelo('LBPH', faces_data, labels)
        self.buttonTrain.config(state="enabled")
        self.back_button.config(state="enabled")
        queue.put("Entrenamiento completado")

    def train(self):
        self.messageLabel.config(text="Entrenando...", foreground="green")
        self.buttonTrain.config(state="disabled")
        self.back_button.config(state="disabled")
        training_thread = threading.Thread(target=self.train_models, args=(self.queue,))
        training_thread.start()
        self.after(100, self.check_queue)

    def check_queue(self):
        try:
            message = self.queue.get_nowait()
        except queue.Empty:
            self.after(100, self.check_queue)
        else:
            self.messageLabel.config(text=message, foreground="green")

    def destroy(self):
        self.frm.destroy()
        super().destroy()

if __name__ == "__main__":
    navigator = Navegator()
    app = TrainScreen(navigator)
    app.mainloop()
