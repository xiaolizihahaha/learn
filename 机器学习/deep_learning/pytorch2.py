# 整体的梯度下降
# import numpy as np
# import matplotlib.pyplot as plt
#
# xs = [1.0,2.0,3.0]
# ys = [2.0,4.0,6.0]
#
# w = 1.0
#
# def forward(w,x):
#     return w * x
#
# def cost(w,xs,ys):
#     cost_sum = 0.0
#     for x,y in zip(xs,ys):
#         y_pred = forward(w,x)
#         cost_sum += (y_pred-y) * (y_pred-y)
#     return cost_sum / len(xs)
#
# def gradient(w,xs,ys):
#     gra_sum = 0.0
#     for x,y in zip(xs,ys):
#         gra_sum += 2 * (w * x - y) * x
#     return gra_sum / len(xs)
#
# epoch_list = []
# w_list = []
# loss_list = []
# for epoch in range(1,100):
#   loss = cost(w,xs,ys)
#   w = w - 0.01 * gradient(w,xs,ys)
#   epoch_list.append(epoch)
#   w_list.append(w)
#   loss_list.append(loss)
#
# plt.figure()
# plt.plot(epoch_list,loss_list)
# plt.xlabel('epoch')
# plt.ylabel('loss')
# plt.show()

#随机梯度下降（和lhy版差不多，但是这里一个batch里面只有一个样本）
import numpy as np
import matplotlib.pyplot as plt

xs = [1.0,2.0,3.0]
ys = [2.0,4.0,6.0]

w = 1.0

def forward(w,x):
    return w * x

def loss(w,x,y):
    y_pred = forward(w,x)
    return (y_pred - y) * ( y_pred - y)

def gradient(w,x,y):
    return 2 * (w * x - y) * x

epoch_list = []
w_list = []
loss_list = []
for epoch in range(100):
    loss1 = 0
    for x,y in zip(xs,ys):
        loss1 = loss(w,x,y)
        w = w - 0.01 * gradient(w,x,y)
    epoch_list.append(epoch)
    w_list.append(w)
    loss_list.append(loss1)

plt.figure()
plt.plot(epoch_list,loss_list)
plt.show()


