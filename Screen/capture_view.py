from tkinter import *
from tkinter import ttk
from styles import setup_styles

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
        
        self.camara = ttk.Label(self.frm, text="Camara")
        self.titleCaputre = ttk.Label(self.frm, text="¡Captura de Datos!", style="Title.TLabel")
        self.numeroCapturas = Text(self.frm, width=20, height=1)
        self.radioButtonFeliz = ttk.Radiobutton(self.frm, text="Feliz", variable=self.emocion_var, value="Feliz")
        self.radioButtonEnojado = ttk.Radiobutton(self.frm, text="Enojado", variable=self.emocion_var, value="Enojado")
        self.radioButtonTriste = ttk.Radiobutton(self.frm, text="Triste", variable=self.emocion_var, value="Triste")
        self.radioButtonAsustado = ttk.Radiobutton(self.frm, text="Asustado", variable=self.emocion_var, value="Asustado")
        self.error_label = ttk.Label(self.frm, text="", foreground="red")
        self.buttonEmpezar = ttk.Button(self.frm, text="Empezar", command=self.check_selection)
        self.back_button = ttk.Button(self.frm, text="Regresar", style="Custom.TButton", command=self.controller.switch_to_main_view)               
        
        # Configurar widgets
        self.frm.grid(column=0, row=0, sticky=(N, S, E, W))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Dibujar widgets
        self.camara.grid(column=0, row=0, rowspan=8, padx=180, pady=100, sticky=W)
        self.titleCaputre.grid(column=1, row=0, pady=10, padx=10, sticky=W)
        self.numeroCapturas.grid(column=1, row=1, pady=10, padx=10, sticky=W)
        self.radioButtonFeliz.grid(column=1, row=2, pady=10, padx=10, sticky=W)
        self.radioButtonEnojado.grid(column=1, row=3, pady=10, padx=10, sticky=W)
        self.radioButtonTriste.grid(column=1, row=4, pady=10, padx=10, sticky=W)
        self.radioButtonAsustado.grid(column=1, row=5, pady=10, padx=10, sticky=W)
        self.error_label.grid(column=1, row=6, pady=10, padx=10, sticky=W)
        self.buttonEmpezar.grid(column=1, row=7, pady=10, padx=10, sticky=(W , E))
        self.back_button.grid(column=1, row=8, pady=10, padx=10, sticky=(W , E))
        

    def check_selection(self):
        selected_emotion = self.emocion_var.get()
        numero_capturas = self.numeroCapturas.get("1.0", "end-1c")  # Obtener el contenido del Text widget
        
        if not selected_emotion:
            self.error_label.config(text="Error: debe elegir una opción")
        elif not numero_capturas:
            self.error_label.config(text="Error: el campo de número de capturas no debe estar vacío")
        elif not numero_capturas.isdigit():
            self.error_label.config(text="Error: el campo de número de capturas debe contener solo números")
        else:
            self.error_label.config(text="Capturando...", foreground="green")
            self.controller.checkRadioButtons(selected_emotion, int(numero_capturas))  # Pasar el número de capturas como entero

    def destroy(self):
        self.frm.destroy()
