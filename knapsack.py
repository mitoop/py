#!/usr/bin/env python

# 类似 Knapsack problem 源代码来自于知乎

import random
random.seed()

# 组数 自定义
groups = 5

# 一百组0-1000内的随机数
values = [random.randint(0, 1000) for i in range(100)]
# 从大到小 减小之后的误差
values.sort(reverse=True)

# 生成对应数目的空列表数
target_groups = [[] for grp in range(groups)]

for v in values:
    # 计算列表值得和 并从小到大排序
    target_groups.sort(key=lambda x: sum(x))
    # 给最小和的列表添加一个值
    target_groups[0].append(v)
    # 重复上面两项操作 趋近目标

# 结果是趋近的 可能并不是最优解 初始从大到小排序 会降低误差
for per in target_groups:
    # 打印每一项
    print(per)
    # 打印总和
    print(sum(per))
