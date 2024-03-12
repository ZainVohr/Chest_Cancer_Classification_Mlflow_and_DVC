from src.Cnn_Chest_Cancer_Classification import logger
from Cnn_Chest_Cancer_Classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline




STAGE_NAME = "Data Igestion Pipeline"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nx================x================x')
except Exception as e:
    raise e