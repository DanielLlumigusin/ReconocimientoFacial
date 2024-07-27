from tkinter import *
from tkinter import ttk
from util.styles import setup_styles

class EmotionView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Reconocimiento de Emociones")
        self.root.geometry("720x480")
        
        # Configurar estilos
        setup_styles()
        
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid(column=0, row=0, sticky=(N, S, E, W))
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        #Iniciar
        self.titleEmotion = ttk.Label(self.frm, text="¡Vista de Reconocimiento de Emociones!", style="Title.TLabel")
        self.camera = ttk.Label(self.frm, text="Cámara")
        self.back_button = ttk.Button(self.frm, text="Regresar", style="Custom.TButton", command=self.controller.switch_to_main_view)
        #Configurar
        
        self.frm.rowconfigure(2, weight=1)
        #Dibujar
        
        self.titleEmotion.grid(column=0, row=0, pady=10, padx=75)
        self.camera.grid(column=0, row=1, pady=150)
        self.back_button.grid(column=0, row=2, pady=10, sticky=(S,E))

    def destroy(self):
        self.frm.destroy()
