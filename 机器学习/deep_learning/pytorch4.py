# 开始使用pytorch的工具来训练
'''
    主要分为4步
    1.准备数据集
    2.构造模型
    3.构造损失函数和优化器
    4.训练迭代（前向、后向、更新）
'''

import torch
import matplotlib.pyplot as plt

xs = torch.Tensor([[1.0],[2.0],[3.0]])
ys = torch.Tensor([[2.0],[4.0],[6.0]])

class LinearModel(torch.nn.Module):
    def __init__(self):
        super(LinearModel,self).__init__()
        self.linear = torch.nn.Linear(1,1)

    def forward(self,x):
        y_pred = self.linear(x)
        return y_pred

model = LinearModel()
criterion = torch.nn.MSELoss(size_average=False)
optimizer = torch.optim.SGD(model.parameters(),lr=0.01)

loss_list = []
epoch_list = []
w_list = []
b_list = []

plt.figure()

for epoch in range(1000):
    y_pred = model(xs)
    loss = criterion(y_pred,ys)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    epoch_list.append(epoch)
    loss_list.append(loss.item())
    w_list.append(model.linear.weight.item())
    b_list.append(model.linear.bias.item())


plt.plot(epoch_list,b_list)
plt.show()

# test
x = torch.Tensor([4.0])
y = model(x)
print(y)



