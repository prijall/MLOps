import logging
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from abc import ABC, abstractmethod
from typing import Union

#@ Creating an abstract class:
class DataStrategy(ABC):
     """
     abstract for defining strategy for handling data
     """
     @abstractmethod
     def handle_data(self, data:pd.DataFrame)->Union[pd.DataFrame, pd.Series]:
          pass
     
class DataPreProcessStrategy(DataStrategy):
     def handle_data(self, data:pd.DataFrame)->pd.DataFrame:
          """
          preprocesses Data
          """
          try:
            data=data.drop(
               [
                 "order_approved_at",
                 "order_delivered_carrier_date",    
                 "order_delivered_customer_date",
                 "order_estimated_delivery_date",
                 "order_purchase_timestamp"], axis=1)
            
            data["product_weight_g"] = data["product_weight_g"].fillna(data["product_weight_g"].median(), inplace=True)
            data["product_length_cm"] = data["product_length_cm"].fillna(data["product_length_cm"].median(), inplace=True)
            data["product_height_cm"] = data["product_height_cm"].fillna(data["product_height_cm"].median(), inplace=True)
            data["product_width_cm"] = data["product_width_cm"].fillna(data["product_width_cm"].median(), inplace=True)
            data["review_comment_message"] = data["review_comment_message"].fillna("No review", inplace=True)   

            data=data.select_dtypes(include=[np.number])
            cols_to_drop=["customer_zip_code_prefix", "order_item_id"]
            data=data.drop(cols_to_drop, axis=1)
            return data

          except Exception as e:
              logging.error("Error in preprocessing data:{}".format(e))
              raise e
          
class DataDivisionStrategy(DataStrategy):
    def handle_data(self, data:pd.DataFrame)-> Union[pd.DataFrame, pd.Series]:
        try:
            X=data.drop(['review_score'], axis=1)
            y=data['review_score']
            X_train, X_test, y_train, y_test=train_test_split(X, y, train_size=0.8, random_state=43)
            return X_train, X_test, y_train, y_test
        
        except Exception as e:
            logging.error("Error in data division:{}".format(e))
            raise e

class DataCleaning:
    def __init__(self, data:pd.DataFrame, strategy:DataStrategy):
        self.data=data
        self.stratgy=strategy

    def handle_data(self)->Union[pd.DataFrame, pd.Series]:
        try:
            return self.strategy.handle_data(self.data)
        except Exception as e:
            logging.error("Error in handling data {}".format(e))
            raise e
    

        

              

