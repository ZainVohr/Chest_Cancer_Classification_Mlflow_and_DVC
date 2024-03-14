from Cnn_Chest_Cancer_Classification.constants import *
from Cnn_Chest_Cancer_Classification.utils.common import read_yaml , create_directories
from Cnn_Chest_Cancer_Classification.entity.config_entity import DataIngestionConfig
import os
class ConfigurationManager:
    def __init__( self,config_filepath = CONFIG_FILE_PATH, params_filepath = PARAMS_FILE_PATH):
            self.config =read_yaml(config_filepath)
            self.params = read_yaml(params_filepath)

            create_directories([self.config.artifacts_root])
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
          config = self.config.data_ingestion
          create_directories([config.root_dir])

          data_ingestion_config = DataIngestionConfig(
                root_dir=config.root_dir,
                source_URL=config.source_URL,
                local_data_file=config.local_data_file,
                unzip_dir=config.unzip_dir
          )
          return data_ingestion_config
    
    def get_data_directories_config(self):
            data_dirs = self.config.get("data_directories")
            base_dir = data_dirs.get("base_dir")
            train_dir = os.path.join(base_dir, data_dirs.get("train_dir"))
            valid_dir = os.path.join(base_dir, data_dirs.get("valid_dir"))
            test_dir = os.path.join(base_dir, data_dirs.get("test_dir"))
            return train_dir, valid_dir, test_dir

    
