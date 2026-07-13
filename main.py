from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.logging.logger import logging
from networksecurity.exceptions.exception import NetworkSecurityException
from networksecurity.entity.config_entity import DataIngestionConfig , DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys


if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(training_pipeline_config=trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate data ingestsion")
        dataingestionartifact = data_ingestion.initiate_data_ingestion() 
        logging.info("Data ingestion completed")
        print(dataingestionartifact)
        data_validation_config = DataValidationConfig(training_pipeline_config= trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact, data_validation_config)
        logging.info("Initiating Data Validation")
        data_validation_arifact = data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")

    except Exception as e : 
        raise NetworkSecurityException(e,sys)
        