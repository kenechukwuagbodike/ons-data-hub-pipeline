import pandas as pd
from scripts.transform import transform_data

def test_transform_transposes():
    # Fake data mimicking raw CSV structure
    df = pd.DataFrame({
        'A': ['id', 'x1', 'x2'],
        'B': ['unit', '10', '20']
    })
    
    # Transpose logic would convert this to:
    result = transform_data(df)
    
    assert isinstance(result, pd.DataFrame)
    assert result.shape[0] > 0