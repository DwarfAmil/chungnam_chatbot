import pandas as pd
from pandas04 import pdprint


def main():
    excel = pd.read_excel("my_pandas/test1.xlsx", sheet_name="Sheet1", engine="openpyxl", header=None)
    pdprint(excel)

    excel.to_excel("my_pandas/test2.xlsx", sheet_name="Sheet1", header=None, index=False)


if __name__ == "__main__":
    main()