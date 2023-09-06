import torch
import pandas as pd

data = pd.read_csv("pytorch/data/test.csv")

torch_data = torch.from_numpy(data['kor'].values)
print(torch_data)

