import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

# def gcd(x,y):
#     if x%y == 0:
#         return y
#     else:
#         return gcd(y, x%y)
# print(gcd(100,60))

# 汉诺塔问题
# count = 0


# def move(n, a, b, c):
#     global count
#     if n == 1:
#         print("{}-->{}".format(a, c))
#         count += 1
#     else:
#         move(n - 1, a, c, b)
#         move(1, a, b, c)
#         move(n - 1, b, a, c)
#
# move(3, "a", "b", "c")
# print(count)

# def find(a, x):
#     for i in range(len(a)):
#         if a[i] == x:
#             return i
#     return -1
# a=[]
# for i in range(10):
#     x = random.randint(1, 100)
#     a.append(x)
# x = 5
# print(find(a, x))

def search(x, num):
    low = 0
    high = len(x)
    mid = 0
    number = 0
    while high>low:
        number = number+1

        mid = (high+low)//2

        if x[mid] == num:
            return mid, number
        elif x[mid] > num:
            high = mid - 1
        elif x[mid] < num:
            low = mid + 1

    return -1, number

average = {}
for time in range(5, 101):
    aver = 0
    for i in range(100):
        l = []
        for y in range(time):
            num = random.randint(1,10000)
            l.append(num)
        num = random.randint(1, 10000)
        aver = aver + search(l, num)[1]
    average.update({time: aver/100})
print(average)

x=[]
y=[]
y1=[]
for i in average.keys():
    x.append(i)

for i in average.values():
    y.append(i)

for i in range(len(x)):
    y1.append(math.log(int(i+1), 2))

plt.plot(x, y, color='blue', label='O of search')
plt.plot(x, y1, color='red', label='logn')
plt.xlim((5, 100))
my_x_ticks = np.arange(5, 100, 10)
plt.xticks(my_x_ticks)

plt.show()
