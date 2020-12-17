import time
import os.path
import numpy as np
# import matplotlib.pyplot as plt
import math

# 模拟退火算法
# --------------------------------------------------------------------
# 定义目标函数
# --------------------------------------


def aimFunction(x):
    y = x ** 3 - 60 * x ** 2 - 4 * x + 6
    return y
# --------------------------------------


# 初始化
# 初始温度（充分大）
T = 10000
# 稳定状态的温度
Tmin = 10
# 随机初始化x，定义域[0,100)
x = np.random.uniform(low=0, high=100)
# 每个温度下所要迭代的次数
k = 50
# 初始化y
y = 0
# 迭代次数初值
t = 0

# 开始退火
while T >= Tmin:
    # 当需要继续退火
    for i in range(k):
        # 计算当前温度下x对应的y
        y = aimFunction(x)
        # 以预设的邻域函数产生一个扰动量，从而得到新的x
        xNew = x + np.random.uniform(low=-0.05, high=0.05)
        if 0 <= xNew < 100:
            # 计算新y
            yNew = aimFunction(xNew)
            # 若ΔEk⩽0，即计算得到的y比上次小，该x可采纳
            if yNew < y:
                x = xNew
            else:
                # 按metropolis principle，以一定概率接受新解
                p = math.exp(-(yNew - y) / T)
                r = np.random.uniform(low=0, high=1)
                if r < p:
                    x = xNew
                else:
                    x = x
    # 缓慢降低温度，一开始T下降的慢，因此p接近于1，接受新解的概率更大
    T = 10000 / (1 + t)
    t += 0.1

print(x, aimFunction(x))
# --------------------------------------------------------------------

# 程序等待
# --------------------------------------------------------------------
if not os.path.exists('file_path'):
    time.sleep(1)
else:
    pass
    # read file
# --------------------------------------------------------------------
