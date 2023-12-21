# 这节使用循环神经网络，输入数据为序列化数据（文本）

#1.RNNCell法
# import torch
#
# # 1.准备数据，文本要转换成独热向量
# idx2char = ['e','h','l','o'] # e对应0，h对应1，l对应2，o对应3，方便字符和数字之间的转换，辅助变量
# x = 'hello'  #我们的数据样本数量为1，所以只有一个x一个y
# y = 'ohlol'
# x_data1 =[idx2char.index(c) for c in x]  #x数据用数字来表示 [1,0,2,2,3] 这里的数字被后面的0，1来代替
# y_data1 =[idx2char.index(c) for c in y]  #y数据用数字来表示 [3,1,2,3,2]
#
# one_hot_temp = [
#     [1,0,0,0],
#     [0,1,0,0],
#     [0,0,1,0],
#     [0,0,0,1]
# ] # 独热向量的辅助变量，用独热向量是为了将所有数据都用0、1来表示
# one_hot_x =[one_hot_temp[x] for x in x_data1] # 至此我们的x用独热向量表示，只有0、1 维度：seq_size * input_size
#
# batch_size = 1
# input_size = 4
# hidden_size = 4
# x_data = torch.Tensor(one_hot_x).view(-1,batch_size,input_size)  # 将x进一步转换成 seq_size * batch_size * input_size
# y_data = torch.LongTensor(y_data1).view(-1,1) #y数据得是longTensor类型的变量 并且维度为 seq_size * 1
#
# # 构建模型
# class Model(torch.nn.Module):
#     def __init__(self,input_size,hidden_size,batch_size):
#         super(Model,self).__init__()
#         self.input_size = input_size
#         self.hidden_size = hidden_size
#         self.batch_size = batch_size
#         self.RNNCell = torch.nn.RNNCell(input_size = self.input_size,hidden_size = self.hidden_size)
#     def forward(self,x,hidden0):
#         hidden = self.RNNCell(x,hidden0)
#         return hidden
#     def init_hidden(self):
#         return torch.zeros(self.batch_size,self.hidden_size)
#
# model = Model(input_size, hidden_size, batch_size)
#
# # 构建损失函数优化器
# criterion = torch.nn.CrossEntropyLoss()
# optimizer = torch.optim.Adam(model.parameters(),lr=0.01)
#
# # 迭代训练
# for epoch in range(15):
#     loss = 0.0
#     hidden0 = model.init_hidden()
#     optimizer.zero_grad()
#
#     for x_feature,y_feature in zip(x_data,y_data):  # 注意这里循环并不是遍历batch，而是遍历seq_size ，是遍历特征
#         y_feature_pred1 = model(x_feature,hidden0)
#         loss += criterion(y_feature_pred1,y_feature)  # 这里的y_feature_pred1维度为 batch_size * hidden_size;  y_feature维度为 1 所以得出结论 CrossEntropyLoss的损失函数要求y_pred 和y的维度满足 y_pred 有batch_size,有hidden_size，而y是batch_size * 1就可以了
#         _,idx = y_feature_pred1.max(dim = 1)
#         print(idx2char[idx.item()])
#
#     loss.backward()
#     optimizer.step()
#     print(epoch+1,loss.item())

# 2.RNN + 独热 法
# import torch
#
# # 1.准备数据，文本要转换成独热向量
# idx2char = ['e','h','l','o'] # e对应0，h对应1，l对应2，o对应3，方便字符和数字之间的转换，辅助变量
# x = 'hello'  #我们的数据样本数量为1，所以只有一个x一个y
# y = 'ohlol'
# x_data1 =[idx2char.index(c) for c in x]  #x数据用数字来表示 [1,0,2,2,3] 这里的数字被后面的0，1来代替
# y_data1 =[idx2char.index(c) for c in y]  #y数据用数字来表示 [3,1,2,3,2]
#
# one_hot_temp = [
#     [1,0,0,0],
#     [0,1,0,0],
#     [0,0,1,0],
#     [0,0,0,1]
# ] # 独热向量的辅助变量，用独热向量是为了将所有数据都用0、1来表示
# one_hot_x =[one_hot_temp[x] for x in x_data1] # 至此我们的x用独热向量表示，只有0、1 维度：seq_size * input_size
#
# batch_size = 1
# input_size = 4
# hidden_size = 4
#
# x_data = torch.Tensor(one_hot_x).view(-1,batch_size,input_size)
# y_data = torch.LongTensor(y_data1)
#
# # 2.构建模型
# class Model(torch.nn.Module):
#     def __init__(self,input_size,hidden_size,batch_size,num_layers = 1):
#         super(Model,self).__init__()
#         self.input_size = input_size
#         self.hidden_size = hidden_size
#         self.batch_size = batch_size
#         self.num_layers = num_layers
#         self.rnn = torch.nn.RNN(input_size = input_size,hidden_size = hidden_size,num_layers = num_layers)
#     def forward(self,x):
#         hidden0 = torch.zeros(self.num_layers,self.batch_size,self.hidden_size)
#         out,hiddenn = self.rnn(x,hidden0)
#         out = out.view(-1,self.hidden_size)
#         return out
#
# # 3. 构建损失函数和优化器
# model = Model(input_size,hidden_size,batch_size,num_layers=1)
# criterion = torch.nn.CrossEntropyLoss()
# optimizer = torch.optim.Adam(model.parameters(),lr = 0.05)
#
# # 4. 迭代训练
# for epoch in range(15):
#     optimizer.zero_grad()
#     out = model(x_data)
#     loss = criterion(out,y_data)
#     loss.backward()
#     optimizer.step()
#
#     _,idx = out.max(dim = 1)
#     print("predict:",[idx2char[i]for i in idx])
#     print(epoch+1,loss.item())


# 3.RNN + embedding 法
# import torch
# import torch.nn.functional as F
#
# # 数据准备
# idx2char = ['e','h','l','o']
# x_data1 = [[1,0,2,2,3]] # 'hello' 1 , 5
# y_data1 = [3,1,2,3,2] # 'ohlol'  batch * seq_size
#
# x_data = torch.LongTensor(x_data1)  # batch_size , seq_size
# y_data = torch.LongTensor(y_data1)  # batch_size * seq_size
#
# #常量设置
# input_size = 4
# hidden_size = 8
# embedding_size = 10
# batch_size = 1
# num_layers = 2
# seq_size = 5
# num_class = 4
#
# # 构建模型
# class Model(torch.nn.Module):
#     def __init__(self):
#         super(Model,self).__init__()
#         self.emd = torch.nn.Embedding(input_size,embedding_size)
#         self.rnn = torch.nn.RNN(input_size=embedding_size,hidden_size=hidden_size,num_layers=num_layers,batch_first=True)
#         self.lc = torch.nn.Linear(hidden_size,num_class)
#     def forward(self,x):
#         hidden0 = torch.zeros(num_layers,batch_size,hidden_size)
#         # 输出 batch_size * seq_size
#         x = self.emd(x)  # batch_size * seq_size * embedding_size
#         x,_ = self.rnn(x,hidden0) # seq_size * batch_size * hidden_size
#         x = F.relu(self.lc(x))  # seq_size * batch_size * num_class
#         #拉直一点 要 (seq_size * batch_size) ,num_class
#         x = x.view(-1,num_class)
#         return x
# model = Model()
# # 损失函数优化器
# criterion = torch.nn.CrossEntropyLoss()
# oprimizer = torch.optim.Adam(model.parameters(),lr = 0.05)
#
# # 迭代训练
# for epoch in range(15):
#     oprimizer.zero_grad()
#     y_pred = model(x_data)
#     loss = criterion(y_pred,y_data)
#     loss.backward()
#     oprimizer.step()
#
#     _,idx = y_pred.max(dim= 1)
#     idx = idx.data.numpy()
#     print("predict:",[idx2char[i] for i in idx])
#     print(epoch+1,loss.item())


# 4.试一下lstm
# import torch
# import torch.nn.functional as F
# idx2char = ['e','h','l','o']
# x_data1 = [[1,0,2,2,3]] # 'hello' 1 , 5 batch_size,seq_size
# y_data1 = [3,1,2,3,2] # 'ohlol'  seq_size * batch_size
#
# x_data = torch.LongTensor(x_data1)
# y_data = torch.LongTensor(y_data1)  # seq_size * batch_size
#
# input_size = 4
# hidden_size = 8
# num_layers = 2
# num_class = 4
# num_direction = 1
# batch_size = 1
# embedding_size = 10
# seq_size = 5
#
# class Model(torch.nn.Module):
#     def __init__(self):
#         super(Model,self).__init__()
#         self.ebd = torch.nn.Embedding(input_size,embedding_size)
#         self.lstm = torch.nn.LSTM(input_size = embedding_size,hidden_size = hidden_size,num_layers = num_layers,bidirectional=False,batch_first=True)
#         self.fc = torch.nn.Linear(hidden_size,num_class)
#
#     def forward(self,x):
#         h0 = torch.zeros(num_layers*num_direction,batch_size,hidden_size)
#         c0 = torch.zeros(num_layers*num_direction,batch_size,hidden_size)
#         x = self.ebd(x)
#         x,(hn,cn) = self.lstm(x,(h0,c0))
#         x = F.relu(self.fc(x))  # seq_size , batch_size , hidden_size
#         x = x.view(-1,num_class)
#         return x
#
# model = Model()
# criterion = torch.nn.CrossEntropyLoss()
# optimizer = torch.optim.Adam(model.parameters(),lr = 0.05)
#
# for epoch in range(15):
#     optimizer.zero_grad()
#     y_pred = model(x_data)
#     loss = criterion(y_pred,y_data)
#     loss.backward()
#     optimizer.step()
#
#     _,idx = y_pred.max(dim = 1)
#     print("predict:",[idx2char[i]for i in idx])
#     print(epoch+1,loss.item())


# 试一下gru
import torch
import torch.nn.functional as F
idx2char = ['e','h','l','o']
x_data1 = [[1,0,2,2,3]] # 'hello' 1 , 5 batch_size,seq_size
y_data1 = [3,1,2,3,2] # 'ohlol'  seq_size * batch_size

x_data = torch.LongTensor(x_data1)
y_data = torch.LongTensor(y_data1)  # seq_size * batch_size

input_size = 4
hidden_size = 8
num_layers = 2
num_class = 4
num_direction = 1
batch_size = 1
embedding_size = 10
seq_size = 5

class Model(torch.nn.Module):
    def __init__(self):
        super(Model,self).__init__()
        self.ebd = torch.nn.Embedding(input_size,embedding_size)
        self.gru = torch.nn.GRU(input_size = embedding_size,hidden_size = hidden_size,num_layers = num_layers,bidirectional=False,batch_first=True)
        self.fc = torch.nn.Linear(hidden_size,num_class)

    def forward(self,x):
        h0 = torch.zeros(num_layers*num_direction,batch_size,hidden_size)
        x = self.ebd(x)
        x,hn = self.gru(x,h0)
        x = F.relu(self.fc(x))  # seq_size , batch_size , hidden_size
        x = x.view(-1,num_class)
        return x

model = Model()
criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(),lr = 0.05)

for epoch in range(15):
    optimizer.zero_grad()
    y_pred = model(x_data)
    loss = criterion(y_pred,y_data)
    loss.backward()
    optimizer.step()

    _,idx = y_pred.max(dim = 1)
    print("predict:",[idx2char[i]for i in idx])
    print(epoch+1,loss.item())

































