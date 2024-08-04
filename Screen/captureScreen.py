from tkinter import *
from tkinter import ttk
from styles import setup_styles
from Controllers.navegator import Navegator
import imutils
import cv2
from PIL import Image
from PIL import ImageTk
import os
import time
import threading

class CaptureScreen(Tk):
    def __init__(self, navigator):
        super().__init__()
        self.navigator = navigator
        self.title("Capturar Emociones")
        self.geometry("850x500")
        
        # Configurar estilos
        setup_styles()

        # Variable para el grupo de radiobuttons
        self.emocion_var = StringVar()

        # Variable para controlar el estado del hilo de captura
        self.capturing = False

        # Declarar widgets
        self.frm = ttk.Frame(self, padding=10)
        self.camara_label = Label(self.frm)
        self.titleCapture = ttk.Label(self.frm, text="¡Captura de Datos!", style="Title.TLabel")
        self.radioButtonFeliz = ttk.Radiobutton(self.frm, text="Feliz", variable=self.emocion_var, value="Feliz")
        self.radioButtonEnojado = ttk.Radiobutton(self.frm, text="Enojado", variable=self.emocion_var, value="Enojado")
        self.radioButtonTriste = ttk.Radiobutton(self.frm, text="Triste", variable=self.emocion_var, value="Triste")
        self.radioButtonAsustado = ttk.Radiobutton(self.frm, text="Asustado", variable=self.emocion_var, value="Asustado")
        self.messageLabel = ttk.Label(self.frm, text="", foreground="red")
        self.buttonEmpezar = ttk.Button(self.frm, text="Empezar", command=self.check_selection)
        self.back_button = ttk.Button(self.frm, text="Regresar", style="Custom.TButton", command=self.close_camera)

        # Configurar widgets
        self.frm.grid(column=0, row=0, sticky=(N, S, E, W))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.frm.columnconfigure(0, weight=1)
        self.frm.columnconfigure(1, weight=1)

        # Dibujar widgets
        self.titleCapture.grid(column=0,columnspan=2, row=0, pady=10, padx=10, sticky=(W, E))
        self.camara_label.grid(column=0, row=1, rowspan=8, padx=20, pady=20, sticky=(W, E))
        self.radioButtonFeliz.grid(column=1, row=2, pady=10, padx=10, sticky=(W, E))
        self.radioButtonEnojado.grid(column=1, row=3, pady=10, padx=10, sticky=(W, E))
        self.radioButtonTriste.grid(column=1, row=4, pady=10, padx=10, sticky=(W, E))
        self.radioButtonAsustado.grid(column=1, row=5, pady=10, padx=10, sticky=(W, E))
        self.messageLabel.grid(column=1, row=6, pady=10, padx=10, sticky=(W, E))
        self.buttonEmpezar.grid(column=1, row=7, pady=10, padx=10, sticky=(W, E))
        self.back_button.grid(column=1, row=8, pady=10, padx=10, sticky=(W, E))
        
        # Inicializar la cámara
        self.cap = cv2.VideoCapture(0)
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

    def deteccion_facilal(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = faceClassif.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        return frame

    def check_selection(self):
        emotion = self.emocion_var.get()
        if not emotion:
            self.messageLabel.configure(text="Seleccione una emoción")
            return
        self.messageLabel.configure(text="Capturando...")
        self.radioButtonFeliz.configure(state="disabled")
        self.radioButtonTriste.configure(state="disabled")
        self.radioButtonEnojado.configure(state="disabled")
        self.radioButtonAsustado.configure(state="disabled")
        self.buttonEmpezar.configure(state="disabled")
        self.back_button.configure(state="disabled")
        self.capturing = True
        self.capture_thread = threading.Thread(target=self.capture_data, args=(emotion,))
        self.capture_thread.start()
        self.monitor_capture_thread()

    def monitor_capture_thread(self):
        if self.capture_thread.is_alive():
            self.after(100, self.monitor_capture_thread)
        else:
            self.radioButtonFeliz.configure(state="enabled")
            self.radioButtonTriste.configure(state="enabled")
            self.radioButtonEnojado.configure(state="enabled")
            self.radioButtonAsustado.configure(state="enabled")
            self.buttonEmpezar.configure(state="enabled")
            self.back_button.configure(state="enabled")
            self.capturing = False
            self.messageLabel.configure(text="Captura completada")

    def close_camera(self):
        if self.cap.isOpened():
            self.cap.release()
        if self.capturing:
            self.capture_thread.join()
        self.navigator.switch_to_main_view()

    def capture_data(self, emotion):
        emotion_dir = f"DataSet/{emotion}"
        if not os.path.exists(emotion_dir):
            os.makedirs(emotion_dir)
        
        captured_count = 0
        while captured_count < 250:
            if self.cap.isOpened():
                ret, frame = self.cap.read()
                if ret:
                    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
                    faces = faceClassif.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
                    for (x, y, w, h) in faces:
                        rostro = frame[y:y + h, x:x + w]
                        rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
                        img_name = os.path.join(emotion_dir, f'rostro_{captured_count}.jpg')
                        cv2.imwrite(img_name, rostro)
                        captured_count += 1
                        if captured_count >= 250:
                            break
            time.sleep(0.1)

if __name__ == "__main__":
    navigator = Navegator()
    app = CaptureScreen(navigator)
    app.mainloop()
