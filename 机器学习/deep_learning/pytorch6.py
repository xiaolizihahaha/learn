import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn.functional as F

#加载数据
x_data = np.loadtxt('diabetes_data.csv',delimiter=' ',dtype=np.float32)
y_data = np.loadtxt('diabetes_target.csv',delimiter=' ',dtype=np.float32)
print(x_data[-1,:])
x = x_data[:-1,:]
y = [[i] for i in y_data[:-1]]
y = np.array(y)
xs = torch.from_numpy(x)
ys = torch.from_numpy(y)
# print(len(xs))



#构建模型
class Model(torch.nn.Module):
    def __init__(self):
        super(Model,self).__init__()
        self.linear1 = torch.nn.Linear(10,8)
        self.linear2 = torch.nn.Linear(8,6)
        self.linear3 = torch.nn.Linear(6,4)
        self.linear4 = torch.nn.Linear(4,1)
        self.active = torch.nn.Sigmoid()

    def forward(self,x):
        x = self.active(self.linear1(x))
        x = self.active(self.linear2(x))
        x = self.active(self.linear3(x))
        x = self.linear4(x)
        return x

model = Model()
criterion = torch.nn.MSELoss(size_average=False)
optimizer = torch.optim.SGD(model.parameters(),lr = 0.000005)

epoch_list = []
loss_list = []

for epoch in range(100):
    y_pred = model(xs)
    loss = criterion(y_pred,ys)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    epoch_list.append(epoch)
    loss_list.append(loss.item())

plt.figure()
plt.plot(epoch_list,loss_list)
plt.show()

x = torch.Tensor([-0.04547248,-0.04464164,-0.0730303,  -0.08141377,  0.08374012,  0.02780893,
  0.17381579, -0.03949338, -0.00421986,  0.00306441])
print(model(x).item())
# print(y_data)

