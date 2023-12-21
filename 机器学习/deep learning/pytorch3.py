# 课堂讲解 y = w * x ，loss 用了两种，一种是（y_pred - y） ** 2 ，另一种是sum（y_pred - y）/ len(xs)
# import torch
# import matplotlib.pyplot as plt
#
# xs = [1.0,2.0,3.0]
# ys = [2.0,4.0,6.0]
#
# w = torch.Tensor([1.0])
# w.requires_grad = True
#
# def forward(x):
#     return w * x
#
# def loss(xs,ys):
#     l_sum = 0.0
#     for x,y in zip(xs,ys):
#         y_pred = forward(x)
#         l_sum += (y_pred - y) * (y_pred - y)
#     return l_sum / len(xs)
#
#
# # def loss(x,y):
# #     y_pred = forward(x)
# #     return (y_pred - y) * (y_pred - y)
#
# loss_list = []
# w_list = []
# epoch_list = []
# for epoch in range(100):
#     l = loss(xs,ys)
#     l.backward()
#     w.data -= 0.01 * w.grad.data
#     w.grad.data.zero_()
#     epoch_list.append(epoch)
#     loss_list.append(l.item())
#     w_list.append(w.data.item())
#
# # loss_list = []
# # w_list = []
# # epoch_list = []
# # for epoch in range(100):
# #     l = 0.0
# #     for x,y in zip(xs,ys):
# #         l = loss(x,y)
# #         l.backward()
# #         w.data -= 0.01 * w.grad.data
# #         w.grad.data.zero_()
# #         print(w.data.item())
# #     epoch_list.append(epoch)
# #     loss_list.append(l.item())
# #     w_list.append(w.data.item())
#
#
# plt.figure()
# plt.plot(epoch_list,w_list)
# plt.show()


# 作业简单变形 y = w * x + b
# import torch
# import matplotlib.pyplot as plt
#
# xs = [1.0,2.0,3.0]
# ys = [2.0,4.0,6.0]
#
# # w和b的初始值是1.0、2.0
# w = torch.Tensor([1.0])
# b = torch.Tensor([2.0])
#
# w.requires_grad = True
# b.requires_grad = True
#
# def forward(x):
#     return w * x + b
#
# def loss(x,y):
#     y_pred = forward(x)
#     return (y_pred - y) * (y_pred - y)
#
# epoch_list = []
# w_list = []
# loss_list = []
# b_list = []
#
# for epoch in range(1000):
#     l = 0.0
#     for x,y in zip(xs,ys):
#         l = loss(x,y)
#         l.backward()
#         w.data -= 0.01 * w.grad.data
#         b.data -= 0.01 * b.grad.data
#         w.grad.data.zero_()
#         b.grad.data.zero_()
#
#     epoch_list.append(epoch)
#     w_list.append(w.item())
#     loss_list.append(l.item())
#     b_list.append(b.item())
#
# plt.figure()
# plt.plot(epoch_list,b_list)
# plt.show()


# 作业 y = w1 * x * x + w2 * x + b
import torch
import matplotlib.pyplot as plt

xs = [1.0,2.0,3.0]
ys = [2.0,4.0,6.0]

w1 = torch.Tensor([1.0])
w2 = torch.Tensor([1.0])
b = torch.Tensor([1.0])
w1.requires_grad = True
w2.requires_grad = True
b.requires_grad = True


def forward(x):
    return w1 * x * x + w2 * x + b
#
# x_list = []
# y_list = []
# plt.figure()
# for x in range(100):
#     y_pred = forward(x)
#     x_list.append(x)
#     y_list.append(y_pred.item())
#
# plt.plot(x_list,y_list)
# plt.show()

def loss(x,y):
    y_pred = forward(x)
    return (y_pred - y) * (y_pred - y)

loss_list = []
epoch_list = []
w1_list = []
w2_list = []
b_list = []

for epoch in range(10000):
    l = 0.0
    for x,y in zip(xs,ys):
        l = loss(x,y)
        l.backward()
        w1.data -= 0.01 * w1.grad.data
        w2.data -= 0.01 * w2.grad.data
        b.data -= 0.01 * b.grad.data

        w1.grad.data.zero_()
        w2.grad.data.zero_()
        b.grad.data.zero_()
    epoch_list.append(epoch)
    loss_list.append(l.item())
    w1_list.append(w1.item())
    w2_list.append(w2.item())
    b_list.append(b.item())

plt.figure()
plt.plot(epoch_list,loss_list)
plt.show()
print(w1.item())
print(w2.item())
print(b.item())



