from tkinter import *
from tkinter import ttk
from styles import setup_styles
from PIL import Image, ImageTk

class CreditsView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Créditos")
        self.root.geometry("720x480")
        
        # Configurar estilos
        setup_styles()

        self.frm = ttk.Frame(self.root, padding=10)
        
        #Cargar imagen
        image_path = 'Screen/assets/image/Daniel_Llumigusin.png'
        image = Image.open(image_path)
        image = image.resize((150, 150)) 
        self.photo = ImageTk.PhotoImage(image)
        
        # Declarar
        self.LabelTitulo = ttk.Label(self.frm, text="¡Créditos!", style="Title.TLabel")
        self.LabelName = ttk.Label(self.frm, text="Daniel Llumigusin", style="Credits.TLabel")
        self.Photo = ttk.Label(self.frm, image=self.photo)
        self.TextContent = ttk.Label(self.frm, text="Estudiante de Ingeniería de Software - ESPE", style="Credits.TLabel")
        self.back_button = ttk.Button(self.frm, text="Regresar", style="Custom.TButton", command=self.controller.switch_to_main_view)
        
        # Configurar
        self.frm.grid(column=0, row=0, sticky=(N, S, E, W))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.frm.columnconfigure(0, weight=1)
        self.frm.rowconfigure(0, weight=1)
        self.frm.rowconfigure(1, weight=1)
        self.frm.rowconfigure(2, weight=1)
        
        # Dibujar
        self.LabelTitulo.grid(column=0, row=0, sticky=(N))
        self.LabelName.grid(column=0, row=1, sticky=(N))
        self.Photo.grid(column=0, row=1)
        self.TextContent.grid(column=0, row=1, sticky=(S))
        self.back_button.grid(column=0, row=2, sticky=(S, E))

    def destroy(self):
        self.frm.destroy()
