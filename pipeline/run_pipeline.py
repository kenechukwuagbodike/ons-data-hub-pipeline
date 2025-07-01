from scripts.extract import extract_data
from scripts.load import load_data
from scripts.transform import transform_data
from utils.config import RAW_DATA_PATH, TRANSFORMED_DATA_PATH
from utils.logging_config import setup_logger

logger = setup_logger(__name__)


def main():
    logger.info("Starting ONS Data Pipeline...")

    # Step 1: Extract
    df = extract_data(RAW_DATA_PATH)

    # Step 2: Transform
    transformed_df = transform_data(df)

    # Step 3: Load
    load_data(transformed_df, TRANSFORMED_DATA_PATH)

    logger.info("ONS Data Pipeline completed successfully.")


if __name__ == "__main__":
    main()
