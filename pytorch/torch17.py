# 라이브러리 호출
import numpy as np
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.nn.functional as F

import torchvision
import torchvision.transforms as transforms
from torch.utils.data import Dataset, DataLoader


# CPU 혹은 GPU 장치 확인
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


# fashion_mnist 데이터셋 내려받기
train_dataset = torchvision.datasets.FashionMNIST("pytorch/data",
                                                  download=True,
                                                  transform=transforms.Compose([transforms.ToTensor()]))
test_dataset = torchvision.datasets.FashionMNIST("pytorch/data",
                                                 download=True,
                                                 train=False,
                                                 transform=transforms.Compose([transforms.ToTensor()]))


# fashion_mnist 데이터를 데이터로더에 전달
train_loader = DataLoader(train_dataset, batch_size=100)
test_loader = DataLoader(test_dataset, batch_size=100)


# 분류에 사용될 클래스 정의
labels_map = {0 : 'T-Shirt',
              1 : 'Trouser',
              2 : 'Pullover',
              3 : 'Dress',
              4 : 'Coat',
              5 : 'Sandal',
              6 : 'Shirt',
              7 : 'Sneaker',
              8 : 'Bag',
              9 : 'Ankle Boot'}

fig = plt.figure(figsize=(8, 8))
columns = 4
rows = 5

# for i in range(1, columns * rows + 1):
#     img_xy = np.random.randint(len(train_dataset))
#     img = train_dataset[img_xy][0][0, :, :]
#     fig.add_subplot(rows, columns, i)
#     plt.title(labels_map[train_dataset[img_xy][1]])
#     plt.axis('off')
#     plt.imshow(img, cmap='gray')
# plt.show()


# 심층 신경망 모델 생성
class FashionDNN(nn.Module):
    def __init__(self):
        super(FashionDNN, self).__init__()
        self.fc1 = nn.Linear(in_features=784, out_features=256)
        self.drop = nn.Dropout(0.25)
        self.fc2 = nn.Linear(in_features=256, out_features=128)
        self.fc3 = nn.Linear(in_features=128, out_features=10)

    def forward(self, input_data):
        out = input_data.view(-1, 784)
        out = F.relu(self.fc1(out))
        out = self.drop(out)
        out = F.relu(self.fc2(out))
        out = self.fc3(out)
        return out
    

# 심층 신경망에서 필요한 파라미터 정의
learning_rate = 0.001
model = FashionDNN()
model.to(device)

criterion = nn.CrossEntropyLoss()
optimazer = torch.optim.Adam(model.parameters(), lr=learning_rate)
print(model)


# 심층 신경망을 이용한 모델 학습
num_epochs = 5
count = 0
loss_list = []
iteration_list = []
accuracy_list = []

predictions_list = []
labels_list = []

for epoch in range(num_epochs):
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)

        train = Variable(images.view(100, 1, 28, 28))
        labels = Variable(labels)

        outputs = model(train)
        loss = criterion(outputs, labels)
        optimazer.zero_grad()
        loss.backward()
        optimazer.step()
        count += 1

        if not (count % 50):
            total = 0
            correct = 0
            for images, labels in test_loader:
                images, labels = images.to(device), labels.to(device)
                labels_list.append(labels)
                test = Variable(images.view(100, 1, 28, 28))
                outputs = model(test)
                predictions = torch.max(outputs, 1)[1].to(device)
                predictions_list.append(predictions)
                correct += (predictions == labels).sum()
                total += len(labels)
            
            accuracy = correct * 100 / total
            loss_list.append(loss.data)
            iteration_list.append(count)
            accuracy_list.append(accuracy)

        if not (count % 500):
            print(f"Iteration : {count}, loss : {loss.data}, Accuracy : {accuracy}%")