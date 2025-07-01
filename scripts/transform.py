import os

import pandas as pd

from utils.logging_config import setup_logger

logger = setup_logger(__name__)


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    logger.info("Transforming data...")

    # Transpose so time-series dates become rows
    df = df.transpose().reset_index()

    # First row becomes the header
    df.columns = df.iloc[0]
    df = df[1:]

    # Rename the first column to 'date' regardless of original name
    df.rename(columns={df.columns[0]: "date"}, inplace=True)

    # Convert date column
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Drop completely empty columns
    df = df.dropna(axis=1, how="all")

    logger.info(f"Transformed data has {len(df)} rows and {len(df.columns)} columns.")
    return df


if __name__ == "__main__":
    raw_df = extract_data()
    clean_df = transform_data(raw_df)
    logger.info(f"Transformed data:\n{clean_df.head(5)}")
