from tkinter import ttk

def setup_styles():
    style = ttk.Style()
    
    # Estilo personalizado para los botones
    style.configure("Custom.TButton",
                    font=("Helvetica", 14, "bold"),
                    foreground="black",
                    background="#007acc",
                    padding=15)
    
    # Estilo personalizado para los botones cuando se presionan
    style.map("Custom.TButton",
              background=[("active", "#005f99")])
    
    # Estilo personalizado para el título
    style.configure("Title.TLabel",
                    font=("Helvetica", 20, "bold"))
