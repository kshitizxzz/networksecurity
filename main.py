from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.model_trainer import ModelTrainer

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig,ModelTrainerConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.components.data_transformation import DataTransformation
import sys


if __name__=='__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig) #came from entity.py
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info('Initiate the data ingestion')
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
        logging.info('Data Inititation Completed')
        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact , data_validation_config)
        logging.info('Initiate data validation')
        data_validation_artifact = data_validation.initiate_data_validation()
        logging.info('data validation completed')
        print(data_validation_artifact)
        data_transformation_config = DataTransformationConfig(trainingpipelineconfig)
        logging.info('data transformation started')
        data_transformation = DataTransformation(data_validation_artifact , data_transformation_config)
        data_transformation_artifact = data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info('data transformation is completed')

        logging.info('Model training is started ')
        model_trainer_config = ModelTrainerConfig(trainingpipelineconfig)
        model_trainer = ModelTrainer(model_trainer_config = model_trainer_config , data_transformation_artifact = data_transformation_artifact)
        model_trainer_artifact = model_trainer.initiate_model_trainer()

        logging.info('Model Training Artifact Completed')

    except Exception as e :
            raise NetworkSecurityException(e,sys)
    
    
    