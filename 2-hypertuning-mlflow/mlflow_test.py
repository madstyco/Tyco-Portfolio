import mlflow
import random
import torch
import loguru
from datetime import datetime
from torch import nn
from loguru import logger


# Define model
class CNN(nn.Module):
    def __init__(self, filters: int, units1: int, units2: int, input_size: tuple):
        super().__init__()
        self.in_channels = input_size[1] # (batch x channels x height x width), so we need the second element
        self.input_size = input_size
        self.filters = filters
        self.units1 = units1
        self.units2 = units2

        self.convolutions = nn.Sequential(
            nn.Conv2d(self.in_channels, filters, kernel_size=3, stride=1, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(filters, filters, kernel_size=3, stride=1, padding=0),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
            nn.Conv2d(filters, filters, kernel_size=3, stride=1, padding=0),
            nn.ReLU(),
            nn.MaxPool2d(kernel_size=2),
        )

        activation_map_size = self._conv_test(self.input_size)
        logger.info(f"Aggregating activationmap with size {activation_map_size}")
        self.agg = nn.AvgPool2d(activation_map_size)

        self.dense = nn.Sequential(
            nn.Flatten(),
            nn.Linear(filters, units1),
            nn.ReLU(),
            nn.Linear(units1, units2),
            nn.ReLU(),
            nn.Linear(units2, 10)
        )

    def _conv_test(self, input_size):
        x = torch.ones(input_size, dtype=torch.float32)
        x = self.convolutions(x)
        return x.shape[-2:]

    def forward(self, x):
        x = self.convolutions(x)
        x = self.agg(x)
        logits = self.dense(x)
        return logits


experiment = 'cnn_test_run'

mlflow.set_experiment(experiment)

# Dummy input
input_size = (1,1,28,28)
model = CNN(filters=32, units1=64, units2=32, input_size=input_size)

with mlflow.start_run(run_name="test"):
    
    # hyperparamter 
    mlflow.log_param("filters", model.filters)
    mlflow.log_param("units1", model.units1)
    mlflow.log_param("units2", model.units2)


    #simuleer een accuracy metric
    accuracy= random.uniform(0.8, 0.95)
    mlflow.log_metric("accuracy", accuracy)

    
    # Log het model
    mlflow.pytorch.log_model(model, "cnn_model")


    print(f"New run with filters={model.filters} and accuracy = {accuracy:.4f}")

