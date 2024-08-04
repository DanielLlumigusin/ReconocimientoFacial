from Controllers.navegator import Navegator
from tkinter import *
from tkinter import ttk
from styles import setup_styles
from PIL import Image, ImageTk

class CreditsScreen(Tk):
    def __init__(self, navigator):
        super().__init__()
        self.navegator = navigator
        self.title("Créditos")
        self.geometry("768x576")
        
        # Configurar estilos
        setup_styles()
        
        self.frm = ttk.Frame(self, padding=10)
        
        # Cargar imagen
        image_path = 'Screen/assets/image/Daniel_Llumigusin.png'
        image = Image.open(image_path)
        image = image.resize((150, 150)) 
        self.photo = ImageTk.PhotoImage(image)
        
        # Declarar widgets
        self.LabelTitulo = ttk.Label(self.frm, text="¡Créditos!", style="Title.TLabel")
        self.LabelName = ttk.Label(self.frm, text="Daniel Llumigusin", style="Credits.TLabel")
        self.Photo = ttk.Label(self.frm, image=self.photo)
        self.TextContent = ttk.Label(self.frm, text="Estudiante de Ingeniería de Software - ESPE", style="Credits.TLabel")
        self.back_button = ttk.Button(self.frm, text="Regresar", style="Custom.TButton", command=self.navegator.switch_to_main_view)
        
        # Configurar widgets
        self.frm.grid(column=0, row=0, sticky=(N, S, E, W))
        
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.frm.columnconfigure(0, weight=1)
        self.frm.rowconfigure(0, weight=1)
        self.frm.rowconfigure(1, weight=1)
        self.frm.rowconfigure(2, weight=1)
        
        # Dibujar widgets
        self.LabelTitulo.grid(column=0, row=0, sticky=(N))
        self.LabelName.grid(column=0, row=1, sticky=(N))
        self.Photo.grid(column=0, row=1)
        self.TextContent.grid(column=0, row=1, sticky=(S))
        self.back_button.grid(column=0, row=2, sticky=(S, E))

    def destroy(self):
        self.frm.destroy()
        super().destroy()  

if __name__ == "__main__":
    navigator = Navegator()
    app = CreditsScreen(navigator)
    app.mainloop()
