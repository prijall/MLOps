# import numpy as np, pandas as pd
# from zenml import pipeline, step
# from zenml.config import DockerSettings
# from zenml.constants import DEFAULT_SERVICE_START_STOP_TIMEOUT
# from zenml.integrations.constants import MLFLOW
# from zenml.integrations.mlflow.model_deployers.mlflow_model_deployer import (
#     MLFlowModelDeployer)
# from zenml.integrations.mlflow.steps import mlflow_model_deployer_step
# from pydantic import BaseModel
# from zenml.steps import Output

# from steps.clean_data import clean_df
# from steps.evaluation import evaluate_model
# from steps.ingest_data import ingest_data
# from steps.model_train import train_model
# # from pipelines.materializer.custom_materializer import cs_materializer

# #@ Setting Docker:
# docker_settings=DockerSettings(required_integrations=[MLFLOW])

# #@ For Delpoyment Triggr:
# class DeploymentTriggerConfig(BaseModel):
#     min_accuracy:float = 0

# @step
# def deployment_trigger(
#     accuracy: float, 
#     config: DeploymentTriggerConfig
# ):
#     return accuracy > config.min_accuracy

# class MLFlowModelDeployerLoaderStepParameters(BaseModel):
#     pipeline_name: str
#     step_name: str
#     running: bool =True

# #For Continous Deployment(CD Pipeline)
# @pipeline(enable_cache=False, settings={'docker': docker_settings})
# def continous_deployment_pipeline(
#     data_path=str,
#     min_accuracy: float=0,
#     workers: int =1,
#     timeout: int =DEFAULT_SERVICE_START_STOP_TIMEOUT):
#     df=ingest_data(data_path=data_path)
#     X_train, X_test, y_train, y_test=clean_df(df)
#     model=train_model(  X_train, X_test, y_train, y_test)
#     mse, r2_score=evaluate_model(model, X_test, y_test)
#     deployment_decision=deployment_trigger(r2_score)
#     mlflow_model_deployer_step(
#         model=model,
#         deploy_decision=deployment_decision,
#         workers=workers,
#         timeout=timeout
#     )


import numpy as np
import pandas as pd
from zenml import pipeline, step
from zenml.config import DockerSettings
from zenml.constants import DEFAULT_SERVICE_START_STOP_TIMEOUT
from zenml.integrations.constants import MLFLOW
from zenml.integrations.mlflow.model_deployers.mlflow_model_deployer import (
    MLFlowModelDeployer)
from zenml.integrations.mlflow.steps import mlflow_model_deployer_step
from pydantic import BaseModel
from typing import Optional, Tuple

from steps.clean_data import clean_df
from steps.evaluation import evaluate_model
from steps.ingest_data import ingest_data
from steps.model_train import train_model

# Docker Settings
docker_settings = DockerSettings(required_integrations=[MLFLOW])

# Deployment Trigger Config
class DeploymentTriggerConfig(BaseModel):
    min_accuracy: float = 0.0

@step
def deployment_trigger(
    accuracy: float, 
    config: DeploymentTriggerConfig
) -> bool:
    """Decides whether to deploy the model"""
    return accuracy > config.min_accuracy

# Continuous Deployment Pipeline
@pipeline(enable_cache=False, settings={"docker": docker_settings})
def continous_deployment_pipeline(
    data_path: str,
    min_accuracy: float = 0.0,
    workers: int = 1,
    timeout: int = DEFAULT_SERVICE_START_STOP_TIMEOUT
):
    # Data Processing
    df = ingest_data(data_path=data_path)
    X_train, X_test, y_train, y_test = clean_df(df)
    
    # Model Training
    model = train_model(X_train, X_test, y_train, y_test)
    
    # Model Evaluation
    mse, r2_score = evaluate_model(model, X_test, y_test)
    
    # Deployment Decision
    deployment_decision = deployment_trigger(r2_score)
    
    # Model Deployment
    mlflow_model_deployer_step(
        model=model,
        deploy_decision=deployment_decision,
        workers=workers,
        timeout=timeout
    )