**Reconocimiento de Emociones**

Entorno de Ejecución

Librerias necesarias
pip install opencv-contrib-python
pip install opencv-python
pip install numpy
pip install imutils
pip install tkinter

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Version 1.0**
1. Primer paso
Generar capturas de rostros según las emociones.

En donde el archivo capturandoRostros.py se encarga de capturar 250 veces y recortar los rostros para almacenarlo según la carpeta DataSet en donde se guardará en una carpeta de la emoción escogida.

2. Segundo paso

Una vez cargada la data con sus respectivas carpetas de emociones, se debe proceder a seleccionar donde nos generará 3 archivos.
- modeloEigenFaces.xml
- modeloFisherFaces.xml
- modeloLBPH.xml

3. Tercer paso
Por último se debe ejecutar el archivo reconocimientoEmociones.py, se nos abrirá la cámara donde se ejecutara el modelo elegido por código y empezará el reconocimiento.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Version 2.0**

Implementación de Interfaz mediante tkinter

Menú
  - Captura de Datos
  - Entrenar Datos
  - Reconocimiento
  - Créditos


------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**Version 3.0 **
Mejoras y Completo

1. Ejecutar con el comando **python main.py**

![](https://github.com/DanielLlumigusin/ReconocimientoFacial/blob/main/README_IMG/menu.png)

2. Dar clic en el botón de **Capturar Datos**

- **Seleccionar una emoción**
- Dar clic en el botón de **Empezar**

Se nos generará una carpeta llamada DataSet y subcarpetas según sea la emoción seleccionada. Así mismo se nos guardará 250 frames que se usará para el entrenamiento.

- Dar clic en el botón de **Regresar**

![](https://github.com/DanielLlumigusin/ReconocimientoFacial/blob/main/README_IMG/capturaDatos.png)


3. Dar clic en el botón de **Entrenar Datos**

  Por siguiente:
- Dar clic en el botón de **Entrenar Datos** 
- Esperar hasta que se nos genere los 3 modelos de entrenamiento.
- Dar clic en el botón de **Regresar**

![](https://github.com/DanielLlumigusin/ReconocimientoFacial/blob/main/README_IMG/train.png)

4. Dar clic en el botón de **Reconocimiento**
- Disfruta del reconocedor de emociones y ve cuanto de porcentaje es certero.

![](https://github.com/DanielLlumigusin/ReconocimientoFacial/blob/main/README_IMG/emotion.png)

5. (Opcional) Ingresar a Créditos 
- Ver el Programador quien realizó el proyecto.

![](https://github.com/DanielLlumigusin/ReconocimientoFacial/blob/main/README_IMG/creditos.png)

