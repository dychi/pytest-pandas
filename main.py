import pandas as pd

def change_column_int_to_float(frame: pd.DataFrame, col_name: str):
    frame = frame.astype({col_name: float})
    return frame
