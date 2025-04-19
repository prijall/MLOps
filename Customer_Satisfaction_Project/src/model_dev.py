import logging
from abc import ABC, abstractmethod
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

class Model(ABC):
   
    @abstractmethod
    def train(self, X_train, y_train):
        pass


class LinearRegressionModel(Model):
    
    def train(self, X_train, y_train, **kwargs):

        try:
            reg=LinearRegression(**kwargs)
            reg.fit(X_train, y_train)
            logging.info('Model training completed')
        
        except Exception as e:
            logging.error('Error in training model:{}'.format(e))
            raise e
  
class RandomForestModel(Model):
    def train(X_train, y_train, **kwargs):
        try:
            rf=RandomForestRegressor()
            rf.fit(X_train, y_train)
            logging.info('Model training completed sucessfully')
        
        except Exception as e:
            logging.error('Error while training;{}'.format(e))
            raise e
