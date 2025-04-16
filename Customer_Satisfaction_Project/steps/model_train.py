import logging # keeps track of log activities
import pandas as pd
from zenml import step

@step
def train_model(df:pd.DataFrame)-> None:
    pass