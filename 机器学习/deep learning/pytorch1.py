# 模型：y = w * x 绘制 w-loss的二维图
# import numpy as np
# import matplotlib.pyplot as plt
#
# x_data = [1.0,2.0,3.0]
# y_data = [2.0,4.0,6.0]
#
# def forward(w,x):
#     return x * w
#
# def loss(x,y,w):
#     y_pred = forward(w,x)
#     return (y_pred - y) * (y_pred - y)
#
# w_list = []
# loss_list = []
#
# for w in range(0,41):
#     loss_sum = 0
#     for x,y in zip(x_data,y_data):
#         y_pred = forward(w/10,x)
#         loss_val = loss(x,y,w/10)
#         loss_sum += loss_val
#     w_list.append(w/10)
#     loss_list.append(loss_sum/3)
#
# plt.plot(w_list,loss_list)
# plt.xlabel('w')
# plt.ylabel('loss')
# plt.show()




# 模型：y = w * x + b 绘制 w、b-loss的二维图
import numpy as np
import matplotlib.pyplot as plt

x_value = [1.0,2.0,3.0]
y_value = [2.0,4.0,6.0]

def forward(w,x,b):
    return w * x + b

def loss(w,x,b,y):
    y_pred = forward(w,x,b)
    return (y_pred - y) * (y_pred - y)

w_list = []
b_list = []
loss_list = []

for w in range(0,41):
    for b in range(-10,10):
        loss_sum = 0
        for x,y in zip(x_value,y_value):
            y_pred = forward(w,x,b)
            loss_one = loss(w,x,b,y)
            loss_sum += loss_one
        w_list.append(w)
        b_list.append(b)
        loss_list.append(loss_sum/3.0)

w_list,b_list = np.meshgrid(w_list,b_list)
loss_list = np.array([loss_list])

plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(w_list,b_list,loss_list,rstride=1,cstride=1,cmap="rainbow")
plt.show()







