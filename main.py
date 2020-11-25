import pandas as pd


def add_one_to_column(frame: pd.DataFrame, col_name: str):
    """指定したカラムに1を足す

    Args:
        frame (pd.DataFrame): 入力のDataFrame
        col_name (str): DataFrameのカラム名

    Returns:
        frame (pd.DataFrame): 出力のDataFrame
    """
    frame.loc[:, col_name] += 1
    return frame