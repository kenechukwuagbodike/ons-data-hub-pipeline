import os
import pandas as pd
from utils.logging_config import setup_logger
from utils.config import TRANSFORMED_DATA_PATH

logger = setup_logger(__name__)

def load_data(df: pd.DataFrame, destination_path: str = TRANSFORMED_DATA_PATH):
    """
    Load transformed data into a CSV file.

    Args:
        df (pd.DataFrame): Transformed data to be saved.
        destination_path (str, optional): Path to save the output CSV file.
                                         Defaults to TRANSFORMED_DATA_PATH.     
    """
    logger.info(f"Saving cleaned data to {destination_path}...")
    df.to_csv(destination_path, index=False)
    logger.info("Data saved successfully.")

if __name__ == "__main__":
    from extract import extract_data
    from transform import transform_data
    logger.info("Starting data extraction, transformation, and loading process...")
    
    raw_df = extract_data()
    clean_df = transform_data(raw_df)
    load_data(clean_df)
    logger.info("Data loading complete.")