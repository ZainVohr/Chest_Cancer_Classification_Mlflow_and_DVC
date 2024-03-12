from Cnn_Chest_Cancer_Classification.constants import *
from Cnn_Chest_Cancer_Classification.utils.common import read_yaml , create_directories
from Cnn_Chest_Cancer_Classification import logger
from Cnn_Chest_Cancer_Classification.entity.config_entity import DataIngestionConfig
import gdown
import zipfile
import os

class DataIngestion:
    def __init__(self , config:DataIngestionConfig):
        self.config = config

    def download_file(self)-> str:
        '''
        Fetch Data from url

        '''
        try:
            dataset_url=self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifatcs/data_ingestion" , exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")
            file_id = dataset_url.split("/")[-2]
            prefix = 'https://drive.google.com/uc?/export=download&id='
            gdown.download(prefix+file_id , zip_download_dir)
        except Exception as e:
            raise e


    def extract_zip_file(self):
        """
        zip_file_path:str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path , exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
