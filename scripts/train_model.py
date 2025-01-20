import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from models.advanced_dnn import create_advanced_dnn

def load_data(train_dir, img_size=(64, 64)):
    datagen = ImageDataGenerator(rescale=1./255)
    train_data = datagen.flow_from_directory(
        train_dir,
        target_size=img_size,
        batch_size=32,
        class_mode='binary'
    )
    return train_data

def train_model(model, train_data, epochs=10):
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    history = model.fit(train_data, epochs=epochs)
    return history

if __name__ == "_main_":
    train_dir = 'data/train'
    model = create_advanced_dnn(input_shape=(64, 64, 3))  # Adjust input shape as needed
    train_data = load_data(train_dir)
    history = train_model(model, train_data, epochs=10)