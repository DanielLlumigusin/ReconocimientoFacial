from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from styles import setup_styles
from Controllers.navegator import Navegator

class MenuScreen(Tk):
    def __init__(self, navigator):
        super().__init__()
        self.navigator = navigator
        self.title("Reconocimiento de Emociones")
        self.geometry("768x576")
        
        # Cargar y redimensionar la imagen
        try:
            self.image = Image.open("emociones.png").resize((400, 400))
            self.photo = ImageTk.PhotoImage(self.image)
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
            self.photo = None
        
        # Inicializar frame
        self.frm = ttk.Frame(self, padding=10)
        self.frm.grid(column=0, row=0, sticky=(N, S, E, W))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.frm.columnconfigure(0, weight=1)
        self.frm.columnconfigure(1, weight=1)
        
        # Configurar estilos
        setup_styles()
        
        # Crear y dibujar widgets
        self.imgMenu = ttk.Label(self.frm, image=self.photo)
        self.titleMenu = ttk.Label(self.frm, text="¡Reconocimiento \n de Emociones!", style="Title.TLabel")
        self.capture_button = ttk.Button(self.frm, text="Capturar Datos", style="Custom.TButton", command=self.navigator.switch_to_capture_view)
        self.train_button = ttk.Button(self.frm, text="Entrenar Datos", style="Custom.TButton", command=self.navigator.switch_to_train_view)
        self.recognize_button = ttk.Button(self.frm, text="Reconocimiento", style="Custom.TButton", command=self.navigator.switch_to_emotion_view)
        self.switch_button = ttk.Button(self.frm, text="Créditos", style="Custom.TButton",command=self.navigator.switch_to_credits_view)
        
        # Posicionar widgets en la grilla
        if self.photo:
            self.imgMenu.grid(column=0, row=0, rowspan=5, padx=10, pady=25)
        self.titleMenu.grid(column=1, row=0, padx=50, pady=10)
        self.capture_button.grid(column=1, row=1, pady=10)
        self.train_button.grid(column=1, row=2, pady=10)
        self.recognize_button.grid(column=1, row=3, pady=10)
        self.switch_button.grid(column=1, row=4, pady=10)
        
        

if __name__ == "__main__":
    navigator = Navegator()
    app = MenuScreen(navigator)
    app.mainloop()
