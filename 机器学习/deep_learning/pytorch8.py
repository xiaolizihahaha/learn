#MNIST手写数字识别
import matplotlib.pyplot as plt
import torch
import torchvision
import torchvision.transforms as Transforms
from torch.utils.data import Dataset,DataLoader
import torch.nn.functional as F

#导入数据集
batch_size = 64
trans_form = Transforms.Compose([Transforms.ToTensor(),Transforms.Normalize((0.1307,),(0.3081,))]) # 数据从28*28变成了1*28*28（W*H*C -> C*W*H）
train_data = torchvision.datasets.MNIST(root='./data',train=True,download=True,transform=trans_form)
train_loader = DataLoader(train_data,batch_size=batch_size,shuffle=True,num_workers=1)

test_data = torchvision.datasets.MNIST(root='./data',train=False,download=True,transform=trans_form)
test_loader = DataLoader(test_data,batch_size=batch_size,shuffle=False,num_workers=1)


#定义模型
class Model(torch.nn.Module):
    def __init__(self):
        super(Model,self).__init__()
        self.linear1 = torch.nn.Linear(784,512)
        self.linear2 = torch.nn.Linear(512,256)
        self.linear3 = torch.nn.Linear(256,128)
        self.linear4 = torch.nn.Linear(128,64)
        self.linear5 = torch.nn.Linear(64,10)
    def forward(self, x):
        x = x.view(-1, 784)
        x = F.relu(self.linear1(x))
        x = F.relu(self.linear2(x))
        x = F.relu(self.linear3(x))
        x = F.relu(self.linear4(x))
        x = self.linear5(x)
        return x

# 构建损失函数和优化器
model = Model()
criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(),lr = 0.01,momentum=0.5)

#迭代之训练
batch_list = []
loss_list = []
def train(epoch):
    loss_sum = 0.0
    for batch_idx,data in enumerate(train_loader):
        x,y = data
        y_pred = model(x)
        loss = criterion(y_pred,y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        loss_sum += loss.item()
        batch_list.append(epoch * 1000 + batch_idx)
        loss_list.append(loss.item())

        if batch_idx % 300 == 299:
            print("(%d,%d) loss:%.3f" % (epoch+1,batch_idx+1,loss_sum/300.0))
            loss_sum = 0.0

def test():
    correct = 0
    total = 0
    with torch.no_grad():
        for data in test_loader:
            x,y = data
            output = model(x)
            _,y_pred = torch.max(output,dim=1)
            total += len(y)
            correct += (y_pred == y).sum().item()

    print("acc:",correct / total)

if __name__ == '__main__':
    for epoch in range(10):
        train(epoch)
        plt.figure()
        test()
    plt.plot(batch_list, loss_list)
    plt.show()


