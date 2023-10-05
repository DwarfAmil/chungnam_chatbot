import numpy as np
import pandas as pd


def main():
    a = np.array([0])
    print(a)
    s1 = pd.Series(["마케팅", "경영", "개발", "기획", "전략"], index=list("abcde"))
    print(s1)
    print(s1[0], s1["a"])


if __name__ == "__main__":
    main()