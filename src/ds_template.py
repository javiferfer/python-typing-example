import pandas as pd
from sklearn.preprocessing import StandardScaler


def basic_func(
    input_df: pd.DataFrame,
    feature_cols: list,
    standard_scaler_flag: bool = False
) -> pd.DataFrame:

    df = input_df[feature_cols]
    if standard_scaler_flag:
        scaler = StandardScaler()
        df = scaler.fit_transform(df)

    return df


df = pd.DataFrame([[1, 2], [1, 3]], columns=['first', 'second'])

df_ouput = basic_func(df, ['first'])
df_ouput = basic_func(df, ['first'], False)
df_ouput = basic_func(df, ['first'], True)

print(basic_func.__annotations__)
