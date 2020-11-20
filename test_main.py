import pandas as pd
from pandas._testing import assert_frame_equal

from main import change_column_int_to_float

def test_column_types():
    input_df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    output_df = change_column_int_to_float(input_df, 'b')
    print("\nOutput:", output_df)
    expected = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})

    print("Expected:", expected)
    assert_frame_equal(output_df, expected, check_dtype=False)