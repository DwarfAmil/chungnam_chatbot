import torch
import torch.nn as nn


class SingleLayer(nn.Module):
    def __init__(self, inputs):
        super().__init__()
        self.layer = nn.Linear(1, 2)
        self.activation = nn.Sigmoid()

    def forward(self, x):
        x = self.layer(x)
        x = self.activation(x)
        return x
    

class MLP(nn.Module):
    def __init__(self):
        super(MLP, self).__init__()
        self.layer1 = nn.Sequential(
            nn.Conv2d(in_channels=3, out_channels=64, kernel_size=5),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2)
        )

        self.layer2 = nn.Sequential(
            nn.Conv2d(in_channels=64, out_channels=30, kernel_size=5),
            nn.ReLU(inplace=True),
            nn.MaxPool2d(2)
        )

        self.layer3 = nn.Sequential(
            nn.Linear(in_features=30 * 5 * 5, out_features=10, bias=True),
            nn.ReLU(inplace=True)
        )

    def forward(self, x):
        x = self.layer1(x)
        x = self.layer2(x)
        x = x.view(x.shape[0], -1)
        x = self.layer3(x)
        return x

def main():
    # model = nn.Linear(1, 1) <= 5번 라인과 같은 뜻
    # model = nn.Linear(in_features=1, out_features=1, bias=1)
    # print(model.weight)
    # print(model.bias)

    model = MLP()

    print(list(model.children()))

if __name__ == "__main__":
    main()