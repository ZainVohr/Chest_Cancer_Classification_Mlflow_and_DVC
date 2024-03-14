import os
import matplotlib.pyplot as plt
import tensorflow as tf
from Cnn_Chest_Cancer_Classification.config.configuration import ConfigurationManager


class ImageDataLoader:
    def __init__(self, train_dir, valid_dir, test_dir, image_size=(150, 150), batch_size=32):
        self.train_dir = train_dir
        self.valid_dir = valid_dir
        self.test_dir = test_dir
        self.image_size = image_size
        self.batch_size = batch_size

    def get_image_data_generators(self, augmentation=True, shuffle=True):
        train_generator = self._create_image_generator(self.train_dir, augmentation, shuffle)
        valid_generator = self._create_image_generator(self.valid_dir, False, shuffle)
        test_generator = self._create_image_generator(self.test_dir, False, shuffle=False)
        return train_generator, valid_generator, test_generator

    def _create_image_generator(self, directory, augmentation, shuffle):
        datagen = tf.keras.preprocessing.image.ImageDataGenerator(
            rescale=1./255,
            rotation_range=5 if augmentation else 0,
            width_shift_range=0.2 if augmentation else 0,
            height_shift_range=0.2 if augmentation else 0,
            shear_range=0.2 if augmentation else 0,
            zoom_range=0.2 if augmentation else 0,
            horizontal_flip=True if augmentation else False,
            vertical_flip=True if augmentation else False,
            fill_mode='nearest'
        )
        return datagen.flow_from_directory(
            directory,
            target_size=self.image_size,
            batch_size=self.batch_size,
            class_mode='categorical' if directory != self.test_dir else None,
            shuffle=shuffle
        )





def visualize_images(generator, num_images=12):
    images, labels = generator.next()
    plt.figure(figsize=(10, 10))
    for i in range(num_images):
        plt.subplot(4, 4, i + 1)
        plt.imshow(images[i])
        plt.title('Class: {}'.format(labels[i]))
        plt.axis('off')
    plt.show()


if __name__ == '__main__':
    config = ConfigurationManager()
    data_dirs = config.get_data_directories_config()
    preprocessed_data= ImageDataLoader(*data_dirs) #Passing *data_directories allows you to unpack the tuple data_directories and pass its elements as individual arguments to the ImageDataLoader constructor. data_directories = ("path/to/train", "path/to/valid", "path/to/test")  data_loader = ImageDataLoader(base_dir, *data_directories)
    train_generator, valid_generator, test_generator = preprocessed_data.get_image_data_generators()
    visualize_images(train_generator)
