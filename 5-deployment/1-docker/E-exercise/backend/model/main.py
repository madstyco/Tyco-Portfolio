from model import TextClustering
import pandas as pd
from pathlib import Path
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from loguru import logger
import time
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (for simplicity)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def read_root():
    """A simple root endpoint to check if the backend is running."""
    return {"message": "Backend is running!"}

@app.post("/run")
def plot():
    # Ensure processed data directory exists
    datadir = Path("data/processed")
    if not datadir.exists():
        logger.info(f"Creating directory {datadir}")
        datadir.mkdir(parents=True)

    # Load parquet file
    datafile = datadir / "posts.parquet"
    while not datafile.exists():
        print("Waiting for datafile to be created...")
        time.sleep(5)
        
    df = pd.read_parquet(datafile)
    logger.info(f"Loaded dataframe with shape {df.shape}")

    # Initialize clustering model
    clustering = TextClustering()

    # Perform clustering
    k = 100
    X = clustering(df["text"], k=k, batch=True, method="PCA")

    logger.info(f"Embedding shape: {X.shape}")
    labels = clustering.get_labels(df)
    logger.info(f"Generated {len(set(labels))} clusters")

    # Plot results
    plt.figure(figsize=(10, 10))
    sns.scatterplot(x=X[:, 0], y=X[:, 1], hue=labels, palette="tab10")

    # Save image
    imgdir = Path("img")

    if not imgdir.exists():
        logger.info(f"Creating directory {imgdir}")
        imgdir.mkdir(parents=True)
    imgfile = imgdir / "clustering.png"
    plt.savefig(imgfile)
    logger.info(f"Saved clustering plot to {imgfile}")