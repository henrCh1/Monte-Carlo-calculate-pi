# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 15:22:07 2023

@author: 86319
"""

# 使用蒙特卡罗方法计算pi
# random库(梅森旋转算法)
import random

# 圆内点的数量
inside = 0

# 总点数
total = 10000000

# 迭代总点数
for i in range(total):
    # 生成随机的x，y坐标
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    
    # 检查点是否在圆内
    if x**2 + y**2 <= 1:
        inside += 1

# 使用蒙特卡罗方法计算pi
pi = 4 * inside / total

# 打印计算出的pi值
print(pi)
