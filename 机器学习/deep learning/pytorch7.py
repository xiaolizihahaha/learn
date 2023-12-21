# import torch
# from torch.utils.data import Dataset,DataLoader
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# # 构造数据集
# class DiabeteDataset(Dataset):
#     def __init__(self,filepath):
#         xy = np.loadtxt(filepath,delimiter=',',dtype=np.float32)
#         self.x = torch.from_numpy(xy[:,:-1])
#         self.y = torch.from_numpy(xy[:,[-1]])
#         self.len = xy.shape[0]
#
#     def __getitem__(self, index):
#         return self.x[index],self.y[index]
#
#     def __len__(self):
#         return self.len
#
# dataset = DiabeteDataset('xxx')
# dataLoader = DataLoader(dataset,batch_size=32,shuffle=True,num_workers=2)
#
# #构造模型
# class Model(torch.nn.Module):
#     def __init__(self):
#         super(model,self).__init__()
#         self.linear1 = torch.nn.Linear(8,6)
#         self.linear2 = torch.nn.Linear(6,4)
#         self.linear3 = torch.nn.Linear(4,1)
#         self.active = torch.nn.Sigmoid()
#
#     def forward(self,x):
#         x = self.active(self.linear1(x))
#         x = self.active(self.linear2(x))
#         x = self.active(self.linear3(x))
#         return x
#
# # 构造损失函数和优化器
# model = Model()
# criterion = torch.nn.BCELoss(size_average=False)
# optimizer = torch.optim.SGD(model.parameters(),lr = 0.01)
#
#
# epoch_list = []
# loss_list = []
# for epoch in range(100):
#     loss = 0.0
#     for i,data in enumerate(dataLoader):
#         x,y = data
#         y_pred = model(x)
#         loss = criterion(y_pred,y)
#         optimizer.zero_grad()
#         loss.backward()
#         optimizer.step()
#
#     epoch_list.append(epoch)
#     loss_list.append(loss.item())
#
# plt.figure()
# plt.plot(epoch_list,loss_list)
# plt.show()



# kaggle titanic泰坦尼克号存活预测
import numpy as np
import matplotlib.pyplot as plt
import torch
from torch.utils.data import DataLoader,Dataset
import pandas as pd
import math

def checkSex(sex):
    if sex == 'male':
        return 1
    else:
        return 0
def checkEmbarked(embarked):
    if embarked == 'S' or embarked == 'C' or embarked == 'Q':
        return True
    else:
        return False

train_all = pd.read_csv('data/TitanicTrain.csv')
# print(train_all)

train_x1 = []
pClass = list(train_all['Pclass'])
# print(pClass)
sex1 = list(train_all['Sex'])
sex2 =[s if checkSex(s) else 0 for s in sex1]
sex =list([s if not checkSex(s) else 1 for s in sex2])
# print(sex)

age1 = list(train_all['Age'])
age = [a if not math.isnan(a) else 29.7 for a in age1]
# print(age)

sibSp = list(train_all['SibSp'])

parch = list(train_all['Parch'])
fare = list(train_all['Fare'])
embarked1 = list(train_all['Embarked'])
embarked = [ord(e) if checkEmbarked(e) else ord('A') for e in embarked1]
# print(embarked)

train_x1.append(pClass)
train_x1.append(sex)
train_x1.append(age)
train_x1.append(sibSp)
train_x1.append(parch)
train_x1.append(fare)
train_x1.append(embarked)
# print(len(sex))

train_x1= list(map(list, zip(*train_x1)))
train_x = torch.Tensor(train_x1)
# print(train_x)


train_y1 = list(train_all['Survived'])
train_y2 =[[y] for y in train_y1]
train_y = torch.Tensor(train_y2)
# print(train_y)



test_all = pd.read_csv('data/TitanicTest.csv')
# print(train_all)

test_x1 = []
pClass = list(test_all['Pclass'])
# print(pClass)
sex1 = list(test_all['Sex'])
sex2 =[s if checkSex(s) else 0 for s in sex1]
sex =list([s if not checkSex(s) else 1 for s in sex2])
# print(sex)

age1 = list(test_all['Age'])
age = [a if not math.isnan(a) else 29.7 for a in age1]
# print(age)

sibSp = list(test_all['SibSp'])

parch = list(test_all['Parch'])
fare = list(test_all['Fare'])
embarked1 = list(test_all['Embarked'])
embarked = [ord(e) if checkEmbarked(e) else ord('A') for e in embarked1]
# print(embarked)

test_x1.append(pClass)
test_x1.append(sex)
test_x1.append(age)
test_x1.append(sibSp)
test_x1.append(parch)
test_x1.append(fare)
test_x1.append(embarked)
test_x1= list(map(list, zip(*test_x1)))
test_x = torch.Tensor(test_x1)
# print(test_x1)

# print(len(train_y))
class Dataset(Dataset):
    def __init__(self):
        self.x = train_x
        self.y = train_y
        self.len = len(train_y)

    def __getitem__(self, index):
        return self.x,self.y
    def __len__(self):
        return self.len

dataset = Dataset()
datasetLoader = DataLoader(dataset,batch_size=27,shuffle=True,num_workers=1)

class Model(torch.nn.Module):
    def __init__(self):
        super(Model,self).__init__()
        self.linear1 = torch.nn.Linear(7,5)
        self.linear2 = torch.nn.Linear(5,3)
        self.linear3 = torch.nn.Linear(3,1)
        self.active = torch.nn.Sigmoid()

    def forward(self,x):
        x = self.active(self.linear1(x))
        x = self.active(self.linear2(x))
        x = self.active(self.linear3(x))
        return x

model = Model()
criterion = torch.nn.BCELoss(reduction = 'mean')
oprimizer = torch.optim.SGD(model.parameters(),lr = 0.01)



if __name__ == '__main__':
    epoch_list = []
    loss_list = []

    for epoch in range(100):
        for index,data in enumerate(datasetLoader):
            x,y = data
            y_pred = model(x)
            loss = criterion(y_pred,y)
            print('epoch:',epoch,'loss:',loss.item())
            oprimizer.zero_grad()
            loss.backward()
            oprimizer.step()

            epoch_list.append(epoch)
            loss_list.append(loss.item())

    plt.figure()
    plt.plot(epoch_list,loss_list)
    plt.show()

