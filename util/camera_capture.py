import cv2
import os
import imutils
import time

def capture_data(emotion, num_capturas, cap):
    emotion_dir = f"DataSet/{emotion}"
    if not os.path.exists(emotion_dir):
        os.makedirs(emotion_dir)

    faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    captured_count = 0

    while captured_count < num_capturas:
        ret, frame = cap.read()
        if not ret:
            print("Error: No se pudo capturar un frame.")
            break

        frame = imutils.resize(frame, width=640)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = frame.copy()

        faces = faceClassif.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            rostro = auxFrame[y:y + h, x:x + w]
            rostro = cv2.resize(rostro, (150, 150), interpolation=cv2.INTER_CUBIC)
            img_name = os.path.join(emotion_dir, f'rostro_{captured_count}.jpg')
            cv2.imwrite(img_name, rostro)
            captured_count += 1
            if captured_count >= num_capturas:
                break

        # Pequeño delay para evitar capturas demasiado rápidas
        time.sleep(0.1)

