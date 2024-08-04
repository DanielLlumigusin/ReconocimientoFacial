import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import cv2
import os
from styles import setup_styles
from Controllers.navegator import Navegator
import imutils

class EmotionScreen(tk.Tk):
    def __init__(self, navigator):
        super().__init__()
        self.navigator = navigator
        self.title("Reconocimiento de Emociones")
        self.geometry("800x600")
        self.METHOD = "LBPH"
        self.path = "DataSet"
        self.image_paths = os.listdir(self.path)
        self.recognizer = self.load_trained_model(self.METHOD) 

        # Configurar estilos
        setup_styles()

        self.frm = ttk.Frame(self, padding=10)
        self.frm.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))

        # Configurar el grid en el frame
        self.frm.columnconfigure(0, weight=1)
        self.frm.rowconfigure(0, weight=1)
        self.frm.rowconfigure(1, weight=1)
        self.frm.rowconfigure(2, weight=1)

        # Declarar widgets
        self.titleEmotion = ttk.Label(self.frm, text="¡Vista de Reconocimiento de Emociones!", style="Title.TLabel")
        self.camara_label = ttk.Label(self.frm)
        self.back_button = ttk.Button(self.frm, text="Regresar", style="Custom.TButton", command=self.close_camera)
        self.messageLabel = ttk.Label(self.frm, text="", style="Error.TLabel")

        # Dibujar widgets
        self.titleEmotion.grid(column=0, row=0, pady=10, padx=10, sticky=(tk.W, tk.E))
        self.camara_label.grid(column=0, row=1, pady=20, padx=10, sticky=(tk.W, tk.E))
        self.back_button.grid(column=0, row=2, pady=10, padx=10, sticky=(tk.S, tk.E))
        self.messageLabel.grid(column=0, row=3, pady=10, padx=10, sticky=(tk.W, tk.E))

        # Inicializar la cámara
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            self.messageLabel.configure(text="Error al abrir la cámara")
            return
        self.update_camera()

    def update_camera(self):
        ret, frame = self.cap.read()
        if ret:
            frame = imutils.resize(frame, width=640)
            frame = self.deteccion_facilal(frame)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)
            self.camara_label.configure(image=img)
            self.camara_label.image = img
        self.after(10, self.update_camera)

    # Crear el reconocedor según el método elegido
    def create_recognizer(self, method):
        if method == 'EigenFaces':
            return cv2.face.EigenFaceRecognizer_create()
        elif method == 'FisherFaces':
            return cv2.face.FisherFaceRecognizer_create()
        elif method == 'LBPH':
            return cv2.face.LBPHFaceRecognizer_create()
        else:
            raise ValueError(f"Método desconocido: {method}")

    # Leer el modelo entrenado
    def load_trained_model(self, method):
        recognizer = self.create_recognizer(method)
        recognizer.read(f'modelo{method}.xml')
        return recognizer

    def deteccion_facilal(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = faceClassif.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            face_image = gray[y:y + h, x:x + w]
            emotion, confidence = self.deteccion_emocion(face_image)
            frame = cv2.putText(frame, f"{emotion} ({confidence:.2f}%)", (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 1, cv2.LINE_AA)

        return frame

    # Predecir la emoción del rostro detectado
    def predict_emotion(self, recognizer, face_image, method, image_paths):
        result = recognizer.predict(face_image)
        if method == 'EigenFaces' and result[1] < 5700:
            return image_paths[result[0]], 100 - result[1] / 5700 * 100
        elif method == 'FisherFaces' and result[1] < 500:
            return image_paths[result[0]], 100 - result[1] / 500 * 100
        elif method == 'LBPH' and result[1] < 60:
            return image_paths[result[0]], 100 - result[1] / 60 * 100
        return 'Desconocido', 0

    def deteccion_emocion(self, face_image):
        emotion, confidence = self.predict_emotion(self.recognizer, face_image, self.METHOD, self.image_paths)
        return emotion, confidence

    def close_camera(self):
        if self.cap.isOpened():
            self.cap.release()
        self.navigator.switch_to_main_view()

if __name__ == "__main__":
    navigator = Navegator()
    app = EmotionScreen(navigator)
    app.mainloop()
