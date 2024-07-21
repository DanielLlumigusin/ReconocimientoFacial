from tkinter import *
from tkinter import ttk
from util.styles import setup_styles

class TrainingView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Entrenamiento")
        self.root.geometry("720x480")
        
        #Inicializar
        
        # Configurar estilos
        setup_styles()
        
        #Configurar
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid(column=0, row=0, sticky=(N, S, E, W))
        self.titleLabel = ttk.Label(self.frm, text="¡Entrenamiento!", style="Title.TLabel")
        
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        #Dibujar
        self.titleLabel.grid(column=0, row=0, pady=10, padx=75)
        self.back_button = ttk.Button(self.frm, text="Regresar", style="Custom.TButton", command=self.controller.switch_to_main_view)
        self.back_button.grid(column=0, row=1, pady=10)

    def destroy(self):
        self.frm.destroy()
