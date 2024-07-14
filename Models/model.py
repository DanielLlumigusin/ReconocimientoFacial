import os

class Model:
    def __init__(self):
        self.data = ["Enojo", "Felicidad", "Sorpresa", "Tristeza"]

    def add_data(self, new_data):
        self.data.append(new_data)
        
    def check_file(self, filename):
        data_path = 'Data' 
        emotions_path = os.path.join(data_path, filename)
        if not os.path.exists(emotions_path):
            print('Carpeta creada: ', emotions_path)
            os.makedirs(emotions_path)