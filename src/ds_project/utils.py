import os
import sys
from src.ds_project.exception import CustomException
from src.ds_project.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

load_dotenv()

HOST=os.getenv("HOST")
USER=os.getenv("USER")
PASS=os.getenv("PASS")
DATABASE=os.getenv("DB")

def read_db():
    logging.info("reading database started") 
    try:
        mydb=pymysql.connect(
            host=HOST,
            user=USER,
            password=PASS,
            db=DATABASE
        )
        logging.info("connection established with %s",mydb)
        df=pd.read_sql_query('Select * from student',mydb)
        print(df.head())
        
        return df
    except Exception as e:
        raise CustomException(e, sys)