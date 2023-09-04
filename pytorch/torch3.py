import torch

print(torch.tensor([[1, 2], [3, 4]]))
print(torch.tensor([[1, 2], [3, 4]], dtype=torch.float64))

a = torch.tensor([[1, 2, 3, 4], [3, 4, 5, 6]], dtype=torch.int8)
b = torch.tensor([[1, 2, 3, 4], [3, 4, 5, 6]], dtype=torch.int8) + 3
print(a[0][0])
print(a[0, 0])
print(a[0][1:3])
print(b)
print(a.shape)
c = a + b
print(c.view(8, 1))
print(c.view(1, 8))
print(c.view(2, 2, 2))
print(c.view(2, -1, 2))
print(c.view(2, -1, 2).shape)