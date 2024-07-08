import cv2
import os
import numpy as np

# Métodos usados para el entrenamiento y lectura del modelo
#method = 'EigenFaces'
#method = 'FisherFaces'
method = 'LBPH'

# Crear el reconocedor según el método elegido
if method == 'EigenFaces':
    emotion_recognizer = cv2.face.EigenFaceRecognizer_create()
elif method == 'FisherFaces':
    emotion_recognizer = cv2.face.FisherFaceRecognizer_create()
elif method == 'LBPH':
    emotion_recognizer = cv2.face.LBPHFaceRecognizer_create()

# Leer el modelo entrenado
emotion_recognizer.read('modelo' + method + '.xml')

# Directorio donde se almacenan los datos de entrenamiento
dataPath = 'Data'
imagePaths = os.listdir(dataPath)
print('imagePaths=', imagePaths)

# Inicializar la captura de video desde la cámara
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Clasificador de cascada para detectar rostros
faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    if not ret:
        print("No se puede capturar el frame")
        break

    # Convertir el frame a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    auxFrame = gray.copy()

    # Detectar rostros en el frame
    faces = faceClassif.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        # Recortar el rostro detectado y redimensionarlo a 150x150
        rostro = auxFrame[y:y + h, x:x + w]
        rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)

        # Realizar la predicción con el modelo entrenado
        result = emotion_recognizer.predict(rostro)
        
        # Dibujar un rectángulo alrededor del rostro detectado
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Mostrar el resultado de la predicción y la etiqueta correspondiente
        if method == 'EigenFaces':
            if result[1] < 5700:
                emotion = imagePaths[result[0]]
            else:
                emotion = 'Desconocido'

        elif method == 'FisherFaces':
            if result[1] < 500:
                emotion = imagePaths[result[0]]
            else:
                emotion = 'Desconocido'

        elif method == 'LBPH':
            if result[1] < 60:
                emotion = imagePaths[result[0]]
            else:
                emotion = 'Desconocido'

        # Mostrar el nombre de la emoción identificada sobre el rectángulo del rostro
        cv2.putText(frame, emotion, (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 1, cv2.LINE_AA)

    # Mostrar el frame con los rostros detectados y los resultados
    cv2.imshow('Reconocimiento Facial', frame)

    # Salir del bucle si se presiona la tecla 'Esc'
    k = cv2.waitKey(1)
    if k == 27:
        break

# Liberar la captura de video y cerrar todas las ventanas
cap.release()
cv2.destroyAllWindows()
