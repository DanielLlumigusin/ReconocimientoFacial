Reconocimiento Facial

Librerias necesarias
pip install opencv-python
pip install numpy
pip install imutils

1. Primer paso
Se debe almacenar información en la Data.

En donde el archivo capturandoRostros.py se encarga de capturar 200 veces y recortar los rostros para almacenarlo segun la cárpeta indicada en el código.

2. Segundo paso

Una vez cargada la data con sus respectivas carpetas de emociones, se debe proceder a ejecutar el archivo entrenando.py donde nos generará 3 archivos.
- modeloEigenFaces.xml
- modeloFisherFaces.xml
- modeloLBPH.xml

3. Tercer paso
Por último se debe ejecutar el archivo reconocimientoEmociones.py, se nos abrirá la cámara donde se ejecutara el modelo elegido por código y empezará el reconocimiento.