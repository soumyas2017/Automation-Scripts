#check config file existence
import os
from pathlib import Path
config_file_location = Path("E:\\Img_reckognition_Config\\config.mlt")
if config_file_location.is_file() :
    print ("File Exists")
else:
    print ("Config File Not existing !!!")
#check mandatory values in config file

#check internet connection
#check camera
#check write access in the pic directory
