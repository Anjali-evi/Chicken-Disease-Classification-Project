import os
from box.exceptions import BoxValueError
import yaml
from cnnClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


# function to read the yaml file
@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads the yaml file and returns
    Args:
        path_to_yaml (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty yaml file

    Returns:
        ConfigBox: ConfigBox type object
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    
    except BoxValueError:
        raise ValueError(f"yaml file: {path_to_yaml} is empty")
    
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directiories(path_to_directories:list, verbose = True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok= True)
        if verbose:
            logger.info(f"directory: {path} created successfully")


@ensure_annotations
def save_json(path:Path, data = dict):

    """
    save json file
    Args:
        path (Path): path like input
        data (dict): dict type object
    """
    with open(path, "w") as f:
        json.dump(data,f,indent=4)

    logger.info(f"json file saved at {path}")


# fucntions for your reference, not used in this project
@ensure_annotations
def load_json(path: Path) ->ConfigBox:

    with open(path) as f:
        content = json.load(f)
    logger.info(f"json file: {path} loaded successfully")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data:Any, path:Path):
    joblib.dump(value= data, filename = path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) ->Any:

    data = joblib.load(path)
    logger.info(f"binary file loaded at: {path}")
    return data

@ ensure_annotations
def get_size(path: Path) -> str:

    size_in_kb = round(os.path.getsize(path)/1024)
    return f"{size_in_kb} KB"
    
    
def decodeImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())