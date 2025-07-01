import os
import pandas as pd
from scripts.load import load_data

def test_load_data(tmp_path):
    # Create dummy DataFrame
    df = pd.DataFrame({
        "date": ["2023-01-01", "2023-01-02"],
        "value": [100, 200]
    })

    # Temporary path for test output
    test_file = tmp_path / "test_output.csv"
    
    # Call the function
    load_data(df, destination_path=str(test_file))

    # Check if file was created
    assert test_file.exists()

    # Read back and verify contents
    df_loaded = pd.read_csv(test_file)
    assert df_loaded.equals(df)
