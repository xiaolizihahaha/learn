'''
    模型要求：输入一个英文名，模型能够自动判别出这个名字所属的国家
    数据集：一共有若干条数据，每条数据包括两列，一列是名字，另一列是国家（国家一共只有18个类别）
'''
import csv
import gzip

import torch
from torch.utils.data import DataLoader,Dataset

# 0.常量定义
batch_size = 256
epochs = 100
input_size = 128 # 这个也叫n_chars 每个特征（字符）用ascii码值来表示，独热向量一个ascii值变成一个列表，如12表示为 一个列表[0,0,0,0,0,0,0,0,0,0,0,12,0,0,0,...]，列表中只有第12个数值为1 剩下的都是0
hidden_size = 100
emdedding_size = 100
# seq_size = xx   这个得通过计算得到，是max（name）for name in names

num_larers = 2
num_direction = 1

#虽然我们知道一共有18个国家类型，但是这个值还是交给程序算吧
# num_class = 18
use_mps = True



# 1.0 数据准备 自己定义数据集
class MyDateset(Dataset):
    def __init__(self,train):
        filename ='train.gz' if train else 'test.gz'
        with gzip.open(filename,'rt') as f:
            reader = csv.reader(f)
            rows = list(reader)

            self.names = [row[0] for row in rows]
            self.countries = [row[1] for row in rows]
            self.len = len(self.names)

            # 构造国家set列表，再排序，建立了使得编号和国家一一对应，我们可以通过编号找到国家
            self.num2country = list(sorted(set(self.countries)))
            self.total_country_num = len(self.num2country)

            #再建立一个国家到编号的映射
            self.country2num = self.countryDict()

    def __getitem__(self, index):
        return self.names[index], self.country2num[self.countries[index]]

    def __len__(self):
        return self.len
    def countryDict(self):
        countryDict = dict()
        for index,data in enumerate(self.num2country):
            countryDict[data] = index
        return countryDict

    def numToCountry(self,index):
        return self.num2country[index]

    def countryToNum(self,country):
        return self.country2num[country]

train_dataset = MyDateset(train=True)
train_loader = DataLoader(train_dataset,batch_size=batch_size,shuffle=True)

test_dataset = MyDateset(train=False)
test_loader = DataLoader(test_dataset,batch_size=batch_size,shuffle=False)

# 1.1 对dataset/dataloader里面的name进行转换 ->独热向量 并排序，因为要排序所以引入了countries
def make_tensors(names,countries):
    # 把names拉开成矩阵  batch * seq(不规则)
    name_metrix0 = []
    for name in names:
        onename = [c for c in name]
        name_metrix0.append(onename)

    namelenth_list = []
    for name in names:
        namelenth_list.append(len(name))
    namelenth_list = torch.LongTensor(namelenth_list)
    countries = countries.long()

    # 把不规则的矩阵变成规则的 batch * seq（规则）
    name_metrix = torch.zeros(len(name_metrix0) * namelenth_list.max()).long()
    for index,(name,name_len) in enumerate(zip(name_metrix,namelenth_list)):
        name_metrix[index,:name_len] = torch.LongTensor(name)


    # 把规则的矩阵进行排序
    namelenth_list,sortedindex = namelenth_list.sort(dim = 0,descending=True)
    name_metrix = name_metrix[sortedindex]
    countries = countries[sortedindex]

    return create_tensor(namelenth_list),create_tensor(name_metrix),create_tensor(countries)


def create_tensor(thing):
    if use_mps is True:
        device = torch.device('mps')
        thing.to(device)
    return thing

# 2.构建模型
class Model(torch.nn.Module):
    def __init__(self,num_class):
        super(Model,self).__init__()
        self.embedding = torch.nn.Embedding(input_size,emdedding_size)
        self.gru = torch.nn.GRU(input_size = emdedding_size,hidden_size=hidden_size,num_layers=num_larers,bidirectional=False)
        self.fc = torch.nn.Linear(hidden_size * num_direction,num_class)

    def forward(self,x,namelength_list):
        x = x.T()  # 转置  batch * seq  -> seq * batch
        x = self.embedding(x)
        batch = x.size(0)
        hidden0 = torch.zeros(num_larers * num_direction,batch,hidden_size)

        x = torch.nn.utils.rnn.pack_padded_sequence(x,namelength_list)
        output,hiddenn = self.gru(x,hidden0)
        if num_direction == 2:
            hiddenn = torch.cat(hiddenn[-1],hiddenn[-2])
        else:
            hiddenn = hiddenn

        y = self.fc(hiddenn)
        return y

# 3. 定义损失函数、优化器
num_class = train_dataset.total_country_num
model = Model(num_class=num_class)
if use_mps:
    device = torch.device('mps')
    model.to(device)

criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(),lr = 0.01)


# 4.训练迭代
def train():
    loss_sum = 0
    for index,data in enumerate(train_loader):
        x,y = data
        namelenth_list,name_metrix,countries = make_tensors(x,y)
        y_pred = model(name_metrix,namelenth_list)
        loss = criterion(y_pred,countries)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        loss_sum += loss.item()

    return loss_sum

# 5.测试迭代
def test():
    correct = 0
    total = 0


    for index,data in enumerate(test_loader):
        x,y = data
        namelenth_list, name_metrix, countries = make_tensors(x, y)
        y_pred = model(name_metrix,namelenth_list)
        predict = y_pred.max(dim = 1,keepfim = True)[1]

        total += len(data)
        correct += predict.eq(countries.view_as(predict)).sum().item()

        print("acc",correct/total)
        return  correct/total

# 6. 主函数
if __name__ == '__main__':
    for epoch in range(epochs):
        loss_sum = train()
        print(epoch+1,loss_sum)
        acc = test()
        print(epoch+1,acc)















