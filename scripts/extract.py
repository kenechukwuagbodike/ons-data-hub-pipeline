import os
import pandas as pd
from utils.logging_config import setup_logger
from utils.config import RAW_DATA_PATH

logger = setup_logger(__name__)


def extract_data(source_path=RAW_DATA_PATH) -> pd.DataFrame:
    """
    Extract raw data from a CSV file.
    
    Args:
        source_path (str): Path to the raw data file (local or GCS).
    
    Returns:
        pd.DataFrame: Loaded data as a DataFrame.
    """
    try:
        logger.info(f"Loading data from {source_path}...")
        df = pd.read_csv(source_path)
        logger.info(f"Loaded {len(df)} rows.")
        return df
    except FileNotFoundError as e:
        logger.error(f"Error: File not found at {source_path}")
        raise e
    except Exception as e:
        logger.error(f"An error occurred while extracting data: {e}")
        raise e
if __name__ == "__main__":
    extract_data()