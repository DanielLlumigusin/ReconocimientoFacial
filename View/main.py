import tkinter as tk
from tkinter import ttk
import i18n as i

i.load_path.append("../i18n")
root = tk.Tk()
root.config(width=900, height=500)
root.title("Aplicación de escritorio Reconocimiento")
frame = tk.Frame(root)


root.mainloop()