import os
import numpy as np

"""
DEFINING COMMON CONSTANT VARIABLES FOR TRAINING PIPELINE
"""
TARGET_COLUMN = "Result"
PIPELINE_NAME : str = "NetworkSecurity"
ARTIFACT_DIR : str = 'artifacts'
FILE_NAME : str = 'phisingData.csv'
TRAIN_FILE_NAME : str = "train.csv"
TEST_FILE_NAME : str = "test.csv"
SCHEMA_FILE_PATH = os.path.join("data_schema", "schema.yaml")
PROCESSING_OBJECT_FILE_NAME = "preprocessing.pkl"
MODEL_FILE_NAME = "model.pkl"
SAVED_MODEL_DIR = os.path.join("saved_models")


"""
DATA INGESTION RELATED CONSTANTS STARTING WITH DATA_INGESTION VAR NAME
"""

DATA_INGESTION_COLLECTION_NAME : str = "NetworkData"
DATA_INGESTION_DATABASE_NAME : str = "AmmarAI"
DATA_INGESTION_DIR_NAME : str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR : str = "feature_store"
DATA_INGESTION_INGESTED_DIR : str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION : float = 0.20


"""
DATA VALIDATION RELATED CONSTANTS STARTING WITH DATA_VALIDATION VAR NAME
"""

DATA_VALIDATION_DIR_NAME = "data_validation"
DATA_VALIDATION_VALID_DIR = "valid"
DATA_VALIDATION_INVALID_DIR = "invalid"
DATA_VALIDATION_DRIFT_REPORT_DIR = "drift_report"
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME = "report.yaml"


"""
DATA TRANSFORMATION RELATED CONSTANTS STARTING WITH DATA_TRANSFORMATION VAR NAME
"""

DATA_TRANSFORMATION_DIR_NAME = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR = "transformed_object"
DATA_TRANSFORMATION_IMPUTER_PARAMS = {
    "missing_values" : np.nan, 
    "n_neighbors" : 3, 
    "weights" : "uniform"
}

DATA_TRANSFORMATION_TRAIN_FILE_PATH = "train.npy"
DATA_TRANSFORMATION_TEST_FILE_PATH = "test.npy"

"""
MODEL TRAINER RELATED CONSTANTS STARTING WITH MODEL_TRAINER VAR NAME
"""

MODEL_TRAINER_DIR_NAME = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME = "model.pkl" 
MODEL_TRAINER_EXPECTED_SCORE = 0.6
MODEL_TRAINER_OVERFITTING_UNDERFITTING_THRESHOLD = 0.05