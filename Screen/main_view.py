from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from styles import setup_styles

class MainView:
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
        
        image_path = "emociones.png"
        image = Image.open(image_path)
        image = image.resize((300, 400))  # Redimensionar la imagen a 300x400 píxeles
        self.photo = ImageTk.PhotoImage(image)
        
        ttk.Label(self.frm, image=self.photo).grid(column=0, row=0, rowspan=5, padx=10, pady=25 )
        ttk.Label(self.frm, text="¡Reconocimiento \n de Emociones!", style="Title.TLabel").grid(column=1, row=0,  padx=50)
        
        self.capture_button = ttk.Button(self.frm, text="Capturar Datos", style="Custom.TButton", command=self.controller.capture_data)
        self.capture_button.grid(column=1, row=1, )
        
        self.train_button = ttk.Button(self.frm, text="Entrenar Datos", style="Custom.TButton", command=self.controller.train_data)
        self.train_button.grid(column=1, row=2, )
        
        self.recognize_button = ttk.Button(self.frm, text="Reconocimiento", style="Custom.TButton", command=self.controller.recognize)
        self.recognize_button.grid(column=1, row=3, )

        self.switch_button = ttk.Button(self.frm, text="Creditos", style="Custom.TButton", command=self.controller.switch_to_secondary_view)
        self.switch_button.grid(column=1, row=4, )

    def destroy(self):
        self.frm.destroy()
