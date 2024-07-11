import cv2
import os
import numpy as np

# Método usado para el entrenamiento y lectura del modelo
METHOD = 'LBPH'

# Crear el reconocedor según el método elegido
def create_recognizer(method):
    if method == 'EigenFaces':
        return cv2.face.EigenFaceRecognizer_create()
    elif method == 'FisherFaces':
        return cv2.face.FisherFaceRecognizer_create()
    elif method == 'LBPH':
        return cv2.face.LBPHFaceRecognizer_create()
    else:
        raise ValueError(f"Método desconocido: {method}")

# Leer el modelo entrenado
def load_trained_model(method):
    recognizer = create_recognizer(method)
    recognizer.read(f'modelo{method}.xml')
    return recognizer

# Inicializar la captura de video desde la cámara
def initialize_video_capture():
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    if not cap.isOpened():
        raise IOError("No se puede abrir la cámara")
    return cap

# Detectar rostros en la imagen
def detect_faces(face_classifier, gray_image):
    return face_classifier.detectMultiScale(gray_image, 1.3, 5)

# Predecir la emoción del rostro detectado
def predict_emotion(recognizer, face_image, method, image_paths):
    result = recognizer.predict(face_image)
    if method == 'EigenFaces' and result[1] < 5700:
        return image_paths[result[0]]
    elif method == 'FisherFaces' and result[1] < 500:
        return image_paths[result[0]]
    elif method == 'LBPH' and result[1] < 60:
        return image_paths[result[0]]
    return 'Desconocido'

def main():
    try:
        # Cargar el modelo entrenado
        recognizer = load_trained_model(METHOD)

        # Directorio donde se almacenan los datos de entrenamiento
        data_path = 'Data'
        image_paths = os.listdir(data_path)
        print('imagePaths=', image_paths)

        # Inicializar la captura de video y el clasificador de rostros
        cap = initialize_video_capture()
        face_classif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        while True:
            ret, frame = cap.read()
            if not ret:
                print("No se puede capturar el frame")
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            aux_frame = gray.copy()

            faces = detect_faces(face_classif, gray)
            for (x, y, w, h) in faces:
                face_image = aux_frame[y:y + h, x:x + w]
                face_image = cv2.resize(face_image, (150, 150), interpolation=cv2.INTER_CUBIC)
                emotion = predict_emotion(recognizer, face_image, METHOD, image_paths)

                # Dibujar el rectángulo alrededor del rostro detectado
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.putText(frame, emotion, (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 1, cv2.LINE_AA)

            # Mostrar el frame con los rostros detectados y los resultados
            cv2.imshow('Reconocimiento Facial', frame)

            # Salir del bucle si se presiona la tecla 'Esc'
            if cv2.waitKey(1) == 27:
                break

        # Liberar la captura de video y cerrar todas las ventanas
        cap.release()
        cv2.destroyAllWindows()

    except Exception as e:
        print(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    main()
