# 3-数组
import numpy as np

# 3.1:将列表转换为numpy数组
list1 = [1, 2, 3, 4, 5]
list1 = np.array(list1)
print(list1)
list1 = list1.tolist()
print(list1)

# 3.2:构建列表,转换为二维numpy数组.再将此数组转换为列表
list2 = [[1, 2, 3], [5, 4, 1], [3, 6, 7]]
print(list2)
list2 = np.array(list2)
print(list2)
list2 = list2.tolist()
print(list2)
