import os, sys
import yaml
import pickle
import numpy as np
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

def read_yaml_file(file_path) -> dict:
    try:
        with open(file_path, 'rb') as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    

def write_yaml_file(file_path, content, replace=False) -> None:
    try:
        if replace:
            if os.path.exist(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as file:
            yaml.dump(content, file)
    except Exception as e:
        raise NetworkSecurityException(e,sys)


def save_object(file_path, object) -> None:
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file:
            pickle.dump(object, file) 
    except Exception as e:
        raise NetworkSecurityException(e, sys)

    

def save_numpy_array_data(file_path, array) -> None:
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file:
            np.save(file, array)   # Correct order
    except Exception as e:
        raise NetworkSecurityException(e, sys)

