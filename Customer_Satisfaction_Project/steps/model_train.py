import logging # keeps track of log activities
import pandas as pd
from zenml import step
from src.model_dev import LinearRegressionModel, RandomForestModel
from sklearn.base import RegressorMixin
from .config import ModelNameConfig

@step
def train_model(
    X_train:pd.DataFrame, 
    X_test: pd.DataFrame,
    y_train: pd.DataFrame, 
    y_test: pd.DataFrame,
    config: ModelNameConfig
)-> RegressorMixin:
    try:
        model=None
        if config.model_name == "LinearRegression":
            model=LinearRegressionModel()
            trained_model=model.train(X_train, y_train)
            return trained_model
        
        if config.model_name=='RandomForestRegressor':
            model=RandomForestModel()
            trained_model=model.train(X_train, y_train)
            return trained_model
           

        else:
            raise ValueError('Model {} not supported'.format(config.model_name))
        
    except Exception as e:
        logging.error('Error in training code:{}'.format(e))
        raise e
