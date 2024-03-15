
from Cnn_Chest_Cancer_Classification import logger
from Cnn_Chest_Cancer_Classification.config.configuration import ConfigurationManager
from Cnn_Chest_Cancer_Classification.components.prepare_base_model import PrepareBaseModel

STAGE_NAME = "Prepare Base Model"



class PreparingBaseModelTrainingPipeline:
    def __init__(self) -> None:
        pass
    
    def main(self):
       try:
            config = ConfigurationManager()
            prepare_base_model_config = config.get_prepare_base_model_config()
            prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()
       except Exception as e:
            raise e


if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<")
        obj = PreparingBaseModelTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nx================x================x')
    except Exception as e:
        raise e