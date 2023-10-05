import numpy as np
import pandas as pd


def pdprint(*pandas_datas: pd.DataFrame | pd.Series) -> None:
    for data in pandas_datas:
        print(f"Data Type: {data.dtypes}, ", end="")
        print(f"Data dim: {data.ndim}, ", end="")
        print(f"Data Shape: {data.shape}")
        print("-" * 20)
        print(data)
        print()


def main():
    a = np.array([0])
    print(a)
    s1 = pd.Series(["마케팅", "경영", "개발", "기획", "전략"], index=list("abcde"), name="부서명")
    print(s1.shape)
    print(s1.name)