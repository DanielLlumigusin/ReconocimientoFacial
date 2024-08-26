from tkinter import ttk

def setup_styles():
    style = ttk.Style()
    
    # Estilo general para los botones, con un color de fondo más suave
    style.configure("Custom.TButton",
                    font=("Helvetica", 14),
                    foreground="#333333",  # Color del texto
                    background="#e0e0e0",  # Color de fondo suave
                    padding=10,
                    borderwidth=1,
                    relief="flat")
    
    style.map("Custom.TButton",
              background=[("active", "#cccccc"), ("pressed", "#b3b3b3")],
              foreground=[("active", "#333333")])
    
    # Estilo personalizado para el título
    style.configure("Title.TLabel",
                    font=("Helvetica", 20, "bold"),
                    foreground="#333333")  # Color del texto
    
    # Estilo para los créditos
    style.configure("Credits.TLabel",
                    font=("Times New Roman", 18),
                    foreground="#555555")  # Color del texto

    # Estilo para los botones específicos del entrenamiento
    style.configure("Train.TButton",
                    font=("Helvetica", 14),
                    background="#ffcc80",  # Color naranja claro
                    foreground="#333333",
                    padding=10,
                    relief="flat")
    
    style.map("Train.TButton",
              background=[("active", "#ffb74d"), ("pressed", "#ffa726")],
              foreground=[("active", "#333333")])

    # Estilo básico para los frames
    style.configure("TFrame",
                    background="#f9f9f9")  # Color de fondo claro
