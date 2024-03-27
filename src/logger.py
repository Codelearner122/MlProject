#it is used to log any type of execution such as error,information and it will help to find the error
import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  #file name 
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)   #log file path
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(    #inside log file
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,

)

if __name__=="__main__": #test
    logging.info("Logging has started")
