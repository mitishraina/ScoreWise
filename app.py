from src.ds_project.logger import logging
from src.ds_project.exception import CustomException
from src.ds_project.components.data_ingestion import DataIngestion
from src.ds_project.components.data_ingestion import DataIngestionConfig
import sys

if __name__ == "__main__":
    logging.info("Application started executing")
    
    try:
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        data_ingestion.initiate_data_ingestion()
        
    except Exception as e:
        logging.info("this is custom exception(app.py)")
        raise CustomException(e, sys)
