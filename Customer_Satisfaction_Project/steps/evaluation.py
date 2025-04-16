import logging # keeps track of log activities
import pandas as pd
from zenml import step

@step
def evaluate_model(df:pd.DataFrame)->None:
    pass