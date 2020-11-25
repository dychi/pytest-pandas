import pandas as pd
from pandas._testing import assert_frame_equal

from main import add_one_to_column


def test_dataframe_equal():
    """パラメータなしで、厳密にチェックする=>DF内のデータ型が異なるのを許容しない
    GIVEN: 3行2列のDataFrameを入力
    WHEN: 指定したカラムの値に1を加える
    THEN: 指定したカラムの値が1増えて同じshapeのDataFrameが返ってくる
    """
    # 入力を定義
    input_df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})

    # テストする関数に入力
    actual_df = add_one_to_column(input_df, 'b')
    print("\nOutput:\n", actual_df)
    expected = pd.DataFrame({'a': [1, 2, 3], 'b': [5, 6, 7]})

    print("Expected:\n", expected)
    # データ型をチェックするためエラーとなる
    assert_frame_equal(actual_df, expected)


def test_dataframe_without_dtype():
    """データ型をチェックしない=>DF内のデータ型が異なっていても許容する
    GIVEN: 3行2列のDataFrameを入力
    WHEN: 指定したカラムの値に1を加える
    THEN: 指定したカラムの値が1増えて同じshapeのDataFrameが返ってくる
    """
    # 入力を定義
    input_df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})

    # テストする関数に入力
    actual_df = add_one_to_column(input_df, 'b')
    print("\nOutput:\n", actual_df)
    expected = pd.DataFrame({'a': [1, 2, 3], 'b': [5, 6, 7]})

    print("Expected:\n", expected)
    assert_frame_equal(actual_df, expected, check_dtype=False)