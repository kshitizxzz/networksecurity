import sys
import os
import numpy as np
import pandas as pd
from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline 

from networksecurity.constant.training_pipeline import TARGET_COLUMN
from networksecurity.constant.training_pipeline import DATA_TRANSFORMATION_IMPUTER_PARAMS

from networksecurity.entity.artifact_entity import  DataTransformationArtifact , DataValidationArtifact

from networksecurity.entity.config_entity import DataTransformationConfig
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.utils.main_utils import save_numpy_array_data , save_object

class DataTransformation:
    def __init__(self , data_validation_artifact : DataValidationArtifact,
                        data_transformation_config : DataTransformationConfig):
        try:
            self.data_validation_artifact = data_validation_artifact
            self.data_transformation_config = data_transformation_config

        except Exception as e :
            raise NetworkSecurityException(e,sys)
        

    def get_data_transformer_obkect(cls)->Pipeline:

        '''
        Docstring for get_data_transformer_obkect
        
        :param cls: DataTransformation
        :return: A Pipeline object
        initializes KNNImputer object with parameters specified in training_pipeline.py file and returns a 
        pipeline object 
        '''
        logging.info(
            'Enter get_data_transformer_object method of Transformation class'
        )

        try:
            imputer:KNNImputer = KNNImputer(** DATA_TRANSFORMATION_IMPUTER_PARAMS )
            logging.info(
                f'Initialize KNNImputer with {DATA_TRANSFORMATION_IMPUTER_PARAMS}'
            )
            processor : Pipeline = Pipeline([('imputer' )])
            return processor
        
        except Exception as e:
            raise NetworkSecurityException(e,sys)


    def initiate_data_transformation(self)-> DataTransformationArtifact:
        try:
            
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        


        
        
 


   
    

