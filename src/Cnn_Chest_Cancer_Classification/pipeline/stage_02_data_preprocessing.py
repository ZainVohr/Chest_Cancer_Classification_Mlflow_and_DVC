from Cnn_Chest_Cancer_Classification.components.data_preprocessing import ImageDataLoader  
from Cnn_Chest_Cancer_Classification import logger
from Cnn_Chest_Cancer_Classification.config.configuration import ConfigurationManager
from Cnn_Chest_Cancer_Classification.utils.common import visualize_images

STAGE_NAME = "Data Preprocessing Stage"


class DataPreprocessingTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
       try:
        config = ConfigurationManager()
        data_dirs = config.get_data_directories_config()
        preprocessed_data= ImageDataLoader(*data_dirs) #Passing *data_directories allows you to unpack the tuple data_directories and pass its elements as individual arguments to the ImageDataLoader constructor. data_directories = ("path/to/train", "path/to/valid", "path/to/test")  data_loader = ImageDataLoader(base_dir, *data_directories)
        train_generator, valid_generator, test_generator = preprocessed_data.get_image_data_generators()
        visualize_images(train_generator)
       except Exception as e:
            raise e


if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<")
        obj = DataPreprocessingTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nx================x================x')
    except Exception as e:
        raise e