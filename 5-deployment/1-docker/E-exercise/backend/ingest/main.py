import requests
from pathlib import Path
from loguru import logger
import re


def download(url: str, datafile: Path):
    """Download a file from a URL if it doesn't already exist."""
    datadir = datafile.parent
    if not datadir.exists():
        logger.info(f"Creating directory {datadir}")
        datadir.mkdir(parents=True, exist_ok=True)

    if not datafile.exists():
        logger.info(f"Downloading {url} to {datafile}")
        response = requests.get(url)
        response.raise_for_status()  # ensure errors are caught
        with datafile.open("wb") as f:
            f.write(response.content)
    else:
        logger.info(f"File {datafile} already exists, skipping download")


def main():
    # Base directory for data
    datadir = Path("data/raw")

    # Download posts.json
    url = "https://raw.githubusercontent.com/jkingsman/JSON-QAnon/main/posts.json"
    datafile = datadir / "posts.json"
    download(url, datafile)

if __name__ == "__main__":
    main()