import torch
import numpy
import torchvision
from torch.utils.data import Dataset,DataLoader
import torch.nn.functional as F

device = torch.device('mps')

#数据准备
batch_size = 64
trans_form = torchvision.transforms.Compose([torchvision.transforms.ToTensor(),torchvision.transforms.Normalize((0.1307,),(0.3081,))])
train_dataset = torchvision.datasets.MNIST(root='./data',train=True,download=False,transform=trans_form)
train_loader = DataLoader(train_dataset,batch_size=batch_size,shuffle=True,num_workers=1)
test_dataset = torchvision.datasets.MNIST(root='./data',train=False,download=False,transform=trans_form)
test_loader = DataLoader(test_dataset,batch_size=batch_size,shuffle=False,num_workers=1)

# 模型构建
# class Model(torch.nn.Module):
#     def __init__(self):
#         super(Model,self).__init__()
#         self.conv1 = torch.nn.Conv2d(1,10,kernel_size=5)
#         self.conv2 = torch.nn.Conv2d(10,20,kernel_size=5)
#         self.pooling = torch.nn.MaxPool2d(2)
#         self.linear1 = torch.nn.Linear(320,10)
#     def forward(self,x):
#         size = x.size(0)
#         x = F.relu(self.pooling(self.conv1(x)))
#         x = F.relu(self.pooling(self.conv2(x)))
#         x = x.view(size,-1)
#         x = self.linear1(x)
#         return x

# 普通形式的叠加更多层数的模型
# class Model(torch.nn.Module):
#     def __init__(self):
#         super(Model,self).__init__()
#         self.conv1 = torch.nn.Conv2d(1,10,kernel_size=5,padding=2)
#         self.conv2 = torch.nn.Conv2d(10,20,kernel_size=3)
#         self.conv3 = torch.nn.Conv2d(20,30,kernel_size=3,padding=1)
#         self.pooling = torch.nn.MaxPool2d(2)
#         self.linear1 = torch.nn.Linear(270,128)
#         self.linear2 = torch.nn.Linear(128,64)
#         self.linear3 = torch.nn.Linear(64,10)
#
#     def forward(self,x):
#         size = x.size(0)
#         x = F.relu(self.pooling(self.conv1(x)))
#         x = F.relu(self.pooling(self.conv2(x)))
#         x = F.relu(self.pooling(self.conv3(x)))
#
#         x = x.view(size,-1)
#         x = F.relu(self.linear1(x))
#         x = F.relu(self.linear2(x))
#         x = self.linear3(x)
#         return x

# 使用googleNet的小块inception作为一个小块
# class InceptionA(torch.nn.Module):
#     def __init__(self,in_channel):
#         super(InceptionA,self).__init__()
#         self.branch1_1 = torch.nn.Conv2d(in_channel,24,kernel_size=1)
#
#         self.branch2_1 = torch.nn.Conv2d(in_channel,16,kernel_size=1)
#
#         self.branch3_1 = torch.nn.Conv2d(in_channel,16,kernel_size=1)
#         self.branch3_2 = torch.nn.Conv2d(16,24,kernel_size=5,padding=2)
#
#         self.branch4_1 = torch.nn.Conv2d(in_channel,16,kernel_size=1)
#         self.branch4_2 = torch.nn.Conv2d(16,24,kernel_size=3,padding=1)
#         self.branch4_3 = torch.nn.Conv2d(24,24,kernel_size=3,padding=1)
#
#     def forward(self,x):
#         branch1 = F.avg_pool2d(x,kernel_size=3,padding=1,stride=1)
#         branch1 = self.branch1_1(branch1)
#
#         branch2 = self.branch2_1(x)
#
#         branch3 = self.branch3_1(x)
#         branch3 = self.branch3_2(branch3)
#
#         branch4 = self.branch4_1(x)
#         branch4 = self.branch4_2(branch4)
#         branch4 = self.branch4_3(branch4)
#
#         branches = [branch1,branch2,branch3,branch4]  # 输出通道 = 24+16+24+24
#         branches = torch.cat(branches,dim=1)
#         return branches
#
# class Model(torch.nn.Module):
#     def __init__(self):
#         super(Model,self).__init__()
#         self.conv1 = torch.nn.Conv2d(1,10,kernel_size=5)
#         self.conv2 = torch.nn.Conv2d(88,20,kernel_size=5)
#         self.inception1 = InceptionA(10)
#         self.inception2 = InceptionA(20)
#
#         self.linear1 = torch.nn.Linear(1408,1024)
#         self.linear2 = torch.nn.Linear(1024,512)
#         self.linear3 = torch.nn.Linear(512,256)
#         self.linear4 = torch.nn.Linear(256,128)
#         self.linear5 = torch.nn.Linear(128,64)
#         self.linear6 = torch.nn.Linear(64,10)
#
#         '''
#                 B 1 28 28
#             conv 1 10 5
#                 B 10 24 24
#             maxPOOL 2
#                 B 10 12 12
#             relu
#                 B 10 12 12
#             indep 10 88
#                 B 88 12 12
#             conv 88 20 5
#                 B 20 8 8
#             maxPOOL 2
#                 B 20 4 4
#             relu
#                 B 20 4 4
#             indep 20 88
#                 B 88 4 4
#
#                 B 1408
#             linear
#
#         '''
#     def forward(self,x):
#         size = x.size(0)
#         #卷积池化激活、inception、卷积池化激活、inception、linear激活、。。、linear
#         x = F.relu(F.max_pool2d(self.conv1(x),kernel_size=2))
#         x = self.inception1(x)
#         x = F.relu(F.max_pool2d(self.conv2(x),kernel_size=2))
#         x = self.inception2(x)
#         x = x.view(size,-1)
#         x = F.relu(self.linear1(x))
#         x = F.relu(self.linear2(x))
#         x = F.relu(self.linear3(x))
#         x = F.relu(self.linear4(x))
#         x = F.relu(self.linear5(x))
#         x = self.linear6(x)
#         return x


# 使用residualNet 的跳连接块
class ResidualBlock(torch.nn.Module):
    def __init__(self,in_channal):
        super(ResidualBlock,self).__init__()
        self.conv1 = torch.nn.Conv2d(in_channal,in_channal,kernel_size=3,padding=1)
        self.conv2 = torch.nn.Conv2d(in_channal, in_channal, kernel_size=3, padding=1)
    def forward(self,x):
        y = F.relu(self.conv1(x))
        y = self.conv2(y)
        y = F.relu(x+y)
        return y

class Model(torch.nn.Module):
    def __init__(self):
        super(Model,self).__init__()
        self.conv1 = torch.nn.Conv2d(1,16,kernel_size=5)
        self.conv2 = torch.nn.Conv2d(16,32,kernel_size=5)
        self.recv1 = ResidualBlock(16)
        self.recv2 = ResidualBlock(32)

        self.linear1 = torch.nn.Linear(512,256)
        self.linear2 = torch.nn.Linear(256,128)
        self.linear3 = torch.nn.Linear(128,64)
        self.linear4 = torch.nn.Linear(64,10)


        '''
            B 1 28 28
        conv1(1,16,5)
            B 16 24 24
        maxpooling(2)
            B 16 12 12
        relu()
            B 16 12 12
        recv()
            B 16 12 12
        conv2(16,32,5)
            B 32 8 8
        maxpooling(2)
            B 32 4 4
        relu()
            B 32 4 4
        recv()
            B 32 4 4
            
            B 512
        linear(,10)
        
        '''

    def forward(self,x):
        size = x.size(0)
        x = F.relu(F.max_pool2d(self.conv1(x),kernel_size=2))
        x = self.recv1(x)
        x = F.relu(F.max_pool2d(self.conv2(x),kernel_size=2))
        x = self.recv2(x)

        x = x.view(size,-1)
        x = F.relu(self.linear1(x))
        x = F.relu(self.linear2(x))
        x = F.relu(self.linear3(x))
        x = self.linear4(x)
        return x








# 选择设备
model = Model()
model.to(device)

# 构建损失函数优化器
criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(),lr = 0.01,momentum=0.5)

# 迭代训练
def train(epoch):
    loss_sum = 0.0
    for batch_idx,data in enumerate(train_loader):
        x,y = data
        x,y = x.to(device),y.to(device)
        y_pred = model(x)
        loss = criterion(y_pred,y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        loss_sum += loss.item()

        if batch_idx % 300 == 299:
            print('(%d,%d) loss:%.3f' %(epoch+1,batch_idx+1,loss_sum / 300.0))
            loss_sum = 0.0

# 迭代测试
def test():
    correct = 0
    total = 0

    with torch.no_grad():
        for batch_idx,data in enumerate(test_loader):
            x,y = data
            x,y = x.to(device),y.to(device)
            output = model(x)
            _,y_pred = torch.max(output,dim=1)
            total += len(y)
            correct += (y_pred == y).sum().item()
    print('acc:',correct/total)

if __name__ == '__main__':
    for epoch in range(10):
        train(epoch)
        test()
