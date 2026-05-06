# CNN 手写数字识别实验报告

## 实验目的
1. 理解卷积神经网络 CNN 的基本结构：卷积层、池化层、全连接层。
2. 实现简易 CNN 与经典 LeNet-5 网络，在 MNIST 手写数字数据集上完成分类。
3. 对比两种网络结构的性能与参数量差异。

## 实验环境
- Python
- PyTorch / TorchVision
- MNIST 手写数字数据集

## 网络结构介绍
### 1. 简易 SimpleCNN
- 1 层卷积 + 1 层最大池化
- 两层全连接
- 输入 1×28×28 灰度图像，输出 10 分类

### 2. LeNet-5
- 两层卷积+平均池化
- 一层卷积 + 两层全连接
- 使用 Tanh 激活，经典浅层 CNN 结构

## 实验结果
- SimpleCNN 测试准确率约 97%+
- LeNet-5 测试准确率可达 98.5%+

## 实验分析
LeNet-5 结构设计更合理，特征提取能力更强，在参数量更少的情况下精度更高；
简易 CNN 结构简单，训练更快，但特征表达能力较弱。

## 运行方法
```bash
# 安装依赖
pip install -r requirements.txt

# 运行简易CNN
python task1/train_simple.py

# 运行LeNet-5
python task2/train_lenet.py
