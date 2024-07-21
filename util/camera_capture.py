import cv2
import os
import imutils

def capture_data(emotion, num_capturas, ret, frame):
    emotion_dir = f"DataSet/{emotion}"
    if not os.path.exists(emotion_dir):
        os.makedirs(emotion_dir)

    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    captured_count = 0

    while captured_count < num_capturas:
        if not ret:
            print("Error: No se pudo capturar un frame.")
            break
        
        frame = imutils.resize(frame, width=640)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = frame.copy()

        faces = faceClassif.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            rostro = auxFrame[y:y + h, x:x + w]
            rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
            img_name = os.path.join(emotion_dir, f'rostro_{captured_count}.jpg')
            cv2.imwrite(img_name, rostro)
            captured_count += 1

        if cv2.waitKey(1) & 0xFF == 27:  # Presionar ESC para salir
            print("Escape presionado, cerrando...")
            break
