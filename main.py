from src.Cnn_Chest_Cancer_Classification import logger
from Cnn_Chest_Cancer_Classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Cnn_Chest_Cancer_Classification.pipeline.stage_02_data_preprocessing import DataPreprocessingTrainingPipeline



# STAGE_NAME = "Data Igestion Pipeline"

# try:
#     logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<")
#     obj = DataIngestionTrainingPipeline()
#     obj.main()
#     logger.info(f'>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nx================x================x')
# except Exception as e:
#     raise e


STAGE_NAME = "Data Preprocessing Stage"

if __name__ == '__main__':
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<")
        obj = DataPreprocessingTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nx================x================x')
    except Exception as e:
        raise e