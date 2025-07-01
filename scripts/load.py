import os

import pandas as pd

from utils.config import TRANSFORMED_DATA_PATH
from utils.logging_config import setup_logger

logger = setup_logger(__name__)


def load_data(df: pd.DataFrame, destination_path: str = TRANSFORMED_DATA_PATH):
    logger.info(f"Saving cleaned data to {destination_path}...")
    df.to_csv(destination_path, index=False)
    logger.info("Data saved successfully.")


if __name__ == "__main__":
    raw_df = extract_data()
    clean_df = transform_data(raw_df)
    load_data(clean_df)
    logger.info("Data loading complete.")
