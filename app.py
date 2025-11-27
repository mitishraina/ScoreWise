from src.ds_project.logger import logging
from src.ds_project.exception import CustomException
import sys

if __name__ == "__main__":
    logging.info("Application started executing")
    
    try:
        a=1/0 #testing custom exception
    except Exception as e:
        logging.info("this is custom exception")
        raise CustomException(e, sys)
