import logging # keeps track of log activities
import pandas as pd
from zenml import step

@step
def clean_df(df:pd.DataFrame)->None:
    pass