# 蒙特卡罗算法求 PI
import random
from math import pi
count = 0
times = 1000000.0

for i in range(int(times)):
    x = random.random()
    y = random.random()
    c = (x - 1)*(x - 1) + (y - 1)*(y - 1)
    if c < 1:
        count += 1

p = count / times * 4

print(f"循环{times}计算出的值为：", p)
print("与实际PI的差值：", pi - p)
