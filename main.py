from src.Cnn_Chest_Cancer_Classification import logger
from Cnn_Chest_Cancer_Classification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from Cnn_Chest_Cancer_Classification.pipeline.stage_02_data_preprocessing import DataPreprocessingTrainingPipeline


STAGE_NAME = "Data Igestion Pipeline"

try:
     logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<")
     obj = DataIngestionTrainingPipeline()
     obj.main()
     logger.info(f'>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nx================x================x')
except Exception as e:
     raise e



    
from Cnn_Chest_Cancer_Classification import logger
from Cnn_Chest_Cancer_Classification.pipeline.stage_03_prepare_base_model import PreparingBaseModelTrainingPipeline
STAGE_NAME = "Prepare Base Model"
try:
       logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<")
       obj = PreparingBaseModelTrainingPipeline()
       obj.main()
       logger.info(f'>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nx================x================x')
except Exception as e:
        raise e

from Cnn_Chest_Cancer_Classification.pipeline.stage_04_model_trainer import ModelTrainingPipeline
STAGE_NAME = "Model training"
#if __name__ == '__main__':
try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nx================x================x')
except Exception as e:
        raise e


from Cnn_Chest_Cancer_Classification.pipeline.stage_05_model_evaluation_mlflow import ModelEvaluationTrainingPipeline

STAGE_NAME = "Model Evaluation stage"

try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f'>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nx================x================x')
except Exception as e:
        raise e


