import matplotlib.pyplot as plt
import torch
import numpy as np
import pandas as pd

# 获取数据
data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
# data放13个特征数据
data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
# target放1个房价值
target = raw_df.values[1::2, 2].reshape(-1, 1)

# 输入数据归一化处理
data = data.reshape([-1, 13])
maximums, minimums = data.max(axis=0), data.min(axis=0)
for i in range(13):
    data[:, i] = (data[:, i] - minimums[i]) / (maximums[i] - minimums[i])

# 定义训练集和测试集
x_train = torch.from_numpy(data[:300])
x_train = x_train.type(torch.float32)
y_train = torch.from_numpy(target[:300])
y_train = y_train.type(torch.float32)
x_test = torch.from_numpy(data[300:])
x_test = x_test.type(torch.float32)
y_test = torch.from_numpy(target[300:])
y_test = y_test.type(torch.float32)

# 定义网络层数与各层神经元数量
input_dim = 13
hidden1_dim = 5
output_dim = 1

# 一个有序的容器，神经网络模块将按照在传入构造器的顺序依次被添加到计算图中执行。
models = torch.nn.Sequential(
    # Linear为线性变换，第一个参数：每个输入样本的大小；第二个参数：每个输出样本的大小
    torch.nn.Linear(input_dim, hidden1_dim),
    torch.nn.ReLU(),
    torch.nn.Linear(hidden1_dim, output_dim),
)
# print(models)
# 进入训练模式
models.train()

epoch_n = 1000  # 训练次数
learning_rate = 0.01
loss_fn = torch.nn.MSELoss()  # MSELoss(均方损失函数)/L1Loss/CrossEntroyLoss
# 优化器:SGD就是随机梯度下降/Adam(自适应矩估计,Adaptive Moment Estimation)，利用梯度的一阶矩估计和二阶矩估计动态调整每个参数的学习率。
# 优化器就是需要根据网络反向传播的梯度信息来更新网络的参数，以起到降低loss函数计算值的作用。
optimzer = torch.optim.Adam(models.parameters(), lr=learning_rate)

for epoch in range(epoch_n):
    y_pred = models(x_train)
    loss = loss_fn(y_pred, y_train)
    print("Epoch:{}, Loss:{:.4f}".format(epoch, loss))
    # 将梯度初始化为零，避免影响下次循环
    optimzer.zero_grad()

    # 根据损失函数（错误准则函数）反向计算每一层的梯度。
    loss.backward()

    # 使用梯度法之类的优化方法来根据梯度调整w。
    optimzer.step()

# 保存训练好的模型
torch.save(models, 'ModelTest.pt')

# --------------------------------------------------------

# 读取训练好的模型
models = torch.load('ModelTest.pt')

# 进入预测模式
models.eval()
y_out = models(x_test)
predict_y = y_out.detach().numpy()

# 统计预测误差
error = y_out - y_test
error_mse = torch.mean(torch.pow(error, 2))
print(error)
print("均方误差:", error_mse)

# 制作图像直观显示预测效果
plt.rcParams['font.sans-serif'] = ['SimHei']
x = np.arange(y_test.shape[0])
y1 = np.array(predict_y)
y2 = np.array(y_test)
line1 = plt.scatter(x, y1, c="blue")
line2 = plt.scatter(x, y2, c='red')
plt.legend([line1, line2], ["预测值", "实际值"])
plt.title("预测房价与实际房价对比图")
plt.ylabel("价格")
plt.savefig('predict_groundtruth.png', dpi=400)
plt.show()
