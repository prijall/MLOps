import logging
import numpy as np
from abc import ABC, abstractmethod
from sklearn.metrics import r2_score, mean_squared_error

class Evaluation(ABC):

    @abstractmethod
    def calulate_score(self, y_pred:np.ndarray, y_true:np.ndarray):
        pass


class MSE(Evaluation):
    def calulate_score(self, y_pred:np.ndarray, y_true:np.ndarray):

        try:
            logging.info('Calculating MSE Loss')
            mse=mean_squared_error(y_true, y_pred)
            logging.info('MSE: {}'.format(mse))
            return mse
        except Exception as e:
            logging.error('Error while calculating error {}'.format(e))
            raise e

class R2(Evaluation):
    def calulate_score(self, y_pred:np.ndarray, y_true:np.ndarray):
        try:
            logging.info('Calculating R2 scoree')
            r2=r2_score(y_true, y_pred)
            logging.info('R2 Score: {}'.format(r2))
            return r2

        except Exception as e:
            logging.error('Error R2: {}'.format(e))
            raise e        