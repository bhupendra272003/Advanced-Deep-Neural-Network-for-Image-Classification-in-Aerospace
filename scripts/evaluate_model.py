import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

def load_test_data(test_dir, img_size=(64, 64)):
    datagen = ImageDataGenerator(rescale=1./255)
    test_data = datagen.flow_from_directory(
        test_dir,
        target_size=img_size,
        batch_size=32,
        class_mode='binary'
    )
    return test_data

def evaluate_model(model, test_data):
    loss, accuracy = model.evaluate(test_data)
    print(f"Test Loss: {loss}, Test Accuracy: {accuracy}")

if __name__ == "_main_":
    test_dir = 'data/test'
    # Load your model here
    model = tf.keras.models.load_model('model_path.h5')
    test_data = load_test_data(test_dir)
    evaluate_model(model, test_data)