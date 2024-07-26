import cv2
import os
import numpy as np
import time
import threading
import queue

class ControllerTraining:
    def __init__(self, root, controllerMain):
        self.root = root
        self.current_view = None
        self.controllerMain = controllerMain
        self.show_training_view()

    def show_training_view(self):
        if self.current_view is not None:
            self.current_view.destroy()
        from Screen.training_view import TrainingView
        self.current_view = TrainingView(self.root, self)

    def obtener_modelo(self, method, faces_data, labels):
        if method == 'EigenFaces':
            emotion_recognizer = cv2.face.EigenFaceRecognizer_create()
        elif method == 'FisherFaces':
            emotion_recognizer = cv2.face.FisherFaceRecognizer_create()
        elif method == 'LBPH':
            emotion_recognizer = cv2.face.LBPHFaceRecognizer_create()

        print(f"Entrenando ({method})...")
        inicio = time.time()
        emotion_recognizer.train(faces_data, np.array(labels))
        tiempo_entrenamiento = time.time() - inicio
        print(f"Tiempo de entrenamiento ({method}): {tiempo_entrenamiento}")

        emotion_recognizer.write(f"modelo{method}.xml")

    def train_models(self, queue):
        data_path = 'DataSet'
        emotions_list = os.listdir(data_path)
        print('Lista de emociones:', emotions_list)

        labels = []
        faces_data = []
        label = 0

        for name_dir in emotions_list:
            emotions_path = os.path.join(data_path, name_dir)

            for file_name in os.listdir(emotions_path):
                labels.append(label)
                faces_data.append(cv2.imread(os.path.join(emotions_path, file_name), 0))
            label += 1

        self.obtener_modelo('EigenFaces', faces_data, labels)
        self.obtener_modelo('FisherFaces', faces_data, labels)
        self.obtener_modelo('LBPH', faces_data, labels)
        queue.put("Entrenamiento completado")
