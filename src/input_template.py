import typing

import pandas as pd


def input_type_func(
    df: pd.DataFrame,
    columns: typing.Optional[list] = None,
    flag: bool = False
):
    pass


df = pd.DataFrame([])

input_type_func(df)
input_type_func(df, flag=True)
# input_type_func(df, columns=True)
input_type_func(df, columns=['a'])
input_type_func(df, columns=None)
