# logistic 回归 用于分类问题
import matplotlib.pyplot as plt
import torch
import torchvision
import torch.nn.functional as F
import numpy as np

xs = torch.Tensor([[1.0],[2.0],[3.0]])
ys = torch.Tensor([[0],[0],[1]])






class LogisticRegressionModel(torch.nn.Module):
    def __init__(self):
        super(LogisticRegressionModel,self).__init__()
        self.linear = torch.nn.Linear(1,1)

    def forward(self,x):
        y_pred = F.sigmoid(self.linear(x))
        return y_pred


model = LogisticRegressionModel()
criterion = torch.nn.BCELoss(size_average=False)
optimizer = torch.optim.SGD(model.parameters(),lr = 0.01)

loss_list = []
epoch_list = []
w_list = []
b_list = []


for epoch in range(7000):
    y_pred = model(xs)
    loss = criterion(y_pred,ys)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    epoch_list.append(epoch)
    loss_list.append(loss.item())
    w_list.append(model.linear.weight.item())
    b_list.append(model.linear.bias.item())

plt.figure()
plt.plot(epoch_list,b_list)
plt.show()

# test
x = torch.Tensor([4.0])
y = model(x)
print(y)
