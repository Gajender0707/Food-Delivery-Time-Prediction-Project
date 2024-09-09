from exception import CustomException
from logger import logging


try:
    a+b 
    logging.info("adding the files")

except Exception as e:
    raise CustomException(e)