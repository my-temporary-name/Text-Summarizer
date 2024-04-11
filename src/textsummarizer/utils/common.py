import os
from box.exceptions import BoxValueError
import yaml
from textsummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations # To prevent from taking wrong data type as input // refer to trials.ipynb
def read_yaml(path_to_yaml: Path)-> ConfigBox:
    """reads yaml file and returns

    Args:
        path_to_yaml (str): path like input

    Raise:
        ValueError: if yaml file is empty
        e: empty file
    
    Returns:
    ConfigBox: ConfigBox type # to call d.key instead of d['key'] // refer to trials.ipynb
    
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded Successfully")
            return ConfigBox(content)
    
    except BoxValueError:
        return ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list of directories
    
    Args:
        path_to_directories (list): list of path of directories
        ignore_log(bool, optional): ignore if multiple dirs is to be created. Defaults to True.
    
    """

    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created: {path}")

@ensure_annotations
def get_size(path: Path)->str:
    """
    get size in KB

    Args:
        path(Path): path of the file
    return:
        str: size of the file in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

