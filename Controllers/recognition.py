import cv2
import os
import numpy as np
from PIL import Image, ImageTk

class EmotionRecognizer:
    def __init__(self, method='LBPH', model_path='modeloLBPH.xml', dataset_path='DataSet'):
        self.method = method
        self.model_path = model_path
        self.dataset_path = dataset_path
        self.recognizer = self.load_trained_model()
        self.face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.image_paths = os.listdir(self.dataset_path)

    def create_recognizer(self):
        if self.method == 'EigenFaces':
            return cv2.face.EigenFaceRecognizer_create()
        elif self.method == 'FisherFaces':
            return cv2.face.FisherFaceRecognizer_create()
        elif self.method == 'LBPH':
            return cv2.face.LBPHFaceRecognizer_create()
        else:
            raise ValueError(f"Método desconocido: {self.method}")

    def load_trained_model(self):
        recognizer = self.create_recognizer()
        recognizer.read(self.model_path)
        return recognizer

    def detect_faces(self, gray_image):
        return self.face_classifier.detectMultiScale(gray_image, 1.3, 5)

    def predict_emotion(self, face_image):
        result = self.recognizer.predict(face_image)
        if self.method == 'EigenFaces' and result[1] < 5700:
            return self.image_paths[result[0]]
        elif self.method == 'FisherFaces' and result[1] < 500:
            return self.image_paths[result[0]]
        elif self.method == 'LBPH' and result[1] < 60:
            return self.image_paths[result[0]]
        return 'Desconocido'

    def process_frame(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.detect_faces(gray)
        for (x, y, w, h) in faces:
            face_image = gray[y:y + h, x:x + w]
            face_image = cv2.resize(face_image, (150, 150), interpolation=cv2.INTER_CUBIC)
            emotion = self.predict_emotion(face_image)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, emotion, (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
        return frame
