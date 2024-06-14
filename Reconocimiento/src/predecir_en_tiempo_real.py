import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Cargar el modelo entrenado
model = load_model('Reconocimiento/modelo_emociones.keras')

# Inicializar la cámara
cap = cv2.VideoCapture(0)

# Diccionario para las etiquetas
labels = {0: 'Asustado', 1: 'Enojado', 2: 'Feliz', 3: 'Serio', 4: 'Triste'}  

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        # Preprocesar la imagen capturada
        roi_gray = gray[y:y + h, x:x + w]
        roi_gray = cv2.resize(roi_gray, (64, 64))
        roi_rgb = cv2.cvtColor(roi_gray, cv2.COLOR_GRAY2RGB)  # Convertir a 3 canales
        roi_rgb = roi_rgb / 255.0
        roi_rgb = np.expand_dims(roi_rgb, axis=0)

        # Predecir la categoría de la imagen
        preds = model.predict(roi_rgb)
        label = np.argmax(preds, axis=1)[0]
        emotion = labels[label]

        # Dibujar un rectángulo alrededor de la cara y mostrar la emoción
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(frame, emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()