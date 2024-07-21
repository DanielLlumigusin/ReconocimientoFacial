import cv2
import threading
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import imutils
from util.styles import setup_styles
from util.camera_capture import capture_data

class CaptureView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Captura de Datos")
        self.root.geometry("720x480")

        # Configurar estilos
        setup_styles()

        # Variable para el grupo de radiobuttons
        self.emocion_var = StringVar()

        # Declarar widgets
        self.frm = ttk.Frame(self.root, padding=10)
        self.camara_label = Label(self.frm)
        self.titleCaputre = ttk.Label(self.frm, text="¡Captura de Datos!", style="Title.TLabel")
        self.labelCapturas = ttk.Label(self.frm, text="Ingrese numero de captura")
        self.numeroCapturas = Text(self.frm, width=10, height=1)
        self.radioButtonFeliz = ttk.Radiobutton(self.frm, text="Feliz", variable=self.emocion_var, value="Feliz")
        self.radioButtonEnojado = ttk.Radiobutton(self.frm, text="Enojado", variable=self.emocion_var, value="Enojado")
        self.radioButtonTriste = ttk.Radiobutton(self.frm, text="Triste", variable=self.emocion_var, value="Triste")
        self.radioButtonAsustado = ttk.Radiobutton(self.frm, text="Asustado", variable=self.emocion_var, value="Asustado")
        self.error_label = ttk.Label(self.frm, text="", foreground="red")
        self.buttonEmpezar = ttk.Button(self.frm, text="Empezar", command=self.check_selection)
        self.back_button = ttk.Button(self.frm, text="Regresar", style="Custom.TButton", command=lambda: [self.destroy(), self.controller.switch_to_main_view()])

        # Configurar widgets
        self.frm.grid(column=0, row=0, sticky=(N, S, E, W))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.frm.columnconfigure(0, weight=1)
        self.frm.columnconfigure(1, weight=1)

        # Dibujar widgets
        self.camara_label.grid(column=0, row=0, rowspan=8, padx=20, pady=20, sticky=(W, E))
        self.titleCaputre.grid(column=1, row=0, pady=10, padx=10, sticky=(W, E))
        self.labelCapturas.grid(column=1, row=1, pady=10, padx=10, sticky=(W))
        self.numeroCapturas.grid(column=1, row=1, pady=10, padx=10, sticky=(E))
        self.radioButtonFeliz.grid(column=1, row=2, pady=10, padx=10, sticky=(W, E))
        self.radioButtonEnojado.grid(column=1, row=3, pady=10, padx=10, sticky=(W, E))
        self.radioButtonTriste.grid(column=1, row=4, pady=10, padx=10, sticky=(W, E))
        self.radioButtonAsustado.grid(column=1, row=5, pady=10, padx=10, sticky=(W, E))
        self.error_label.grid(column=1, row=6, pady=10, padx=10, sticky=(W, E))
        self.buttonEmpezar.grid(column=1, row=7, pady=10, padx=10, sticky=(W, E))
        self.back_button.grid(column=1, row=8, pady=10, padx=10, sticky=(W, E))

        # Inicializar cámara e hilo para captura de video
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("Error: No se pudo abrir la cámara.")
        else:
            self.update_frame()

    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = imutils.resize(frame, width=320)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            imgtk = ImageTk.PhotoImage(image=img)
            self.camara_label.imgtk = imgtk
            self.camara_label.configure(image=imgtk)
        self.camara_label.after(10, self.update_frame)

    def check_selection(self):
        selected_emotion = self.emocion_var.get()
        numero_capturas = self.numeroCapturas.get("1.0", "end-1c")

        if not selected_emotion:
            self.error_label.config(text="Error: debe elegir una opción")
        elif not numero_capturas:
            self.error_label.config(text="Error: el campo de número de capturas \nno debe estar vacío")
        elif not numero_capturas.isdigit():
            self.error_label.config(text="Error: el campo de número de capturas \ndebe contener solo números")
        else:
            self.error_label.config(text="Capturando...", foreground="green")
            ret, frame = self.cap.read() 
            threading.Thread(target=capture_data, args=(selected_emotion, int(numero_capturas), ret, frame)).start()

    def destroy(self):
        self.cap.release()
        self.frm.destroy()
