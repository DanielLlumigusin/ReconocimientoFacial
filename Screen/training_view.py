import threading
import queue
from tkinter import *
from tkinter import ttk
from util.styles import setup_styles

class TrainingView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Entrenamiento")
        self.root.geometry("720x480")
        
        self.frm = ttk.Frame(self.root, padding=10)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Configurar estilos
        setup_styles()
        
        # Inicializar
        self.titleLabel = ttk.Label(self.frm, text="¡Entrenamiento!", style="Title.TLabel")
        self.descriptionLabel = ttk.Label(self.frm, text="Pulsa el botón para entrenar")
        self.messageLabel = ttk.Label(self.frm, text="")
        self.buttonTrain = ttk.Button(self.frm, text="Entrenar Datos", command=self.train)
        self.back_button = ttk.Button(self.frm, text="Regresar", style="Custom.TButton", command=self.controller.controllerMain.switch_to_main_view)
        
        # Configurar
        self.frm.grid(column=0, row=0, sticky=(N, S, E, W))
        self.frm.columnconfigure(0, weight=1)
        
        # Dibujar
        self.titleLabel.grid(column=0, row=0, pady=10, padx=75)
        self.descriptionLabel.grid(column=0, row=1, pady=10)
        self.messageLabel.grid(column=0, row=2, pady=10)
        self.buttonTrain.grid(column=0, row=3, pady=10)
        self.back_button.grid(column=0, row=4, pady=10)

        # Cola para comunicación entre hilos
        self.queue = queue.Queue()

    def train(self):
        self.messageLabel.config(text="Entrenando...", foreground="green")
        threading.Thread(target=self.controller.train_models, args=(self.queue,)).start()
        self.root.after(100, self.check_queue)

    def check_queue(self):
        try:
            message = self.queue.get_nowait()
        except queue.Empty:
            self.root.after(100, self.check_queue)
        else:
            self.messageLabel.config(text=message, foreground="green")

    def destroy(self):
        self.frm.destroy()
