import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import cv2
from deepface import DeepFace

def get_face_attributes(frame):
    result = DeepFace.analyze(frame, actions=['emotion', 'age', 'gender', 'race'], enforce_detection=False)
    if isinstance(result, list):
        result = result[0]
    return result

def main():
    # Captura de video
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        
        if not ret:
            break
        
        # Conversión a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detección de rostros
        faces = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml').detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        
        for (x, y, w, h) in faces:
            # Dibujar un rectángulo alrededor del rostro
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            
            # Recortar el área del rostro
            face_crop = frame[y:y+h, x:x+w]
            
            # Obtener los atributos del rostro
            attributes = get_face_attributes(face_crop)
            emotion = attributes['dominant_emotion']
            age = attributes['age']
            gender = attributes['gender']
            race = attributes['dominant_race']
            
            # Mostrar los atributos en la ventana
            cv2.putText(frame, f'Emotion: {emotion}', (x, y-30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (36, 255, 12), 2)
            cv2.putText(frame, f'Age: {age}', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (36, 255, 12), 2)
            cv2.putText(frame, f'Gender: {gender}', (x, y+10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (36, 255, 12), 2)
            cv2.putText(frame, f'Race: {race}', (x, y+30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (36, 255, 12), 2)
        
        # Mostrar el video en una ventana
        cv2.imshow('Video', frame)
        
        # Salir del bucle con la tecla 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Liberar la captura de video y cerrar las ventanas
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
