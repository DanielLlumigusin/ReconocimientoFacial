import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Configuración del generador de datos
train_datagen = ImageDataGenerator(rescale=1./255)
val_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    'Reconocimiento/Dataset/train', 
    target_size=(64, 64),
    batch_size=32,
    class_mode='categorical'
)

validation_generator = val_datagen.flow_from_directory(
    'Reconocimiento/Dataset/validation', 
    target_size=(64, 64),
    batch_size=32,
    class_mode='categorical'
)

# Definición del modelo
model = tf.keras.models.Sequential([
    tf.keras.layers.Input(shape=(64, 64, 3)),  # Usar Input como primera capa
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(5, activation='softmax')  # Suponiendo 5 clases
])

# Compilación del modelo
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Entrenamiento del modelo
model.fit(train_generator, epochs=10, validation_data=validation_generator)

# Guardar el modelo
model.save('Reconocimiento/modelo_emociones.keras')
