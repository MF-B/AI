# 4-元素的索引

# 4.1:构造列表
list1 = []
for i in range(12):
    list1.append(i)
print(list1)

# 4.2:取列表的数字3
print(list1[3])

# 4.3:用负数索引取列表中的数字10
print(list1[-2])  # 负数索引从-1开始

# 4.4:通过带有冒号的索引取3,4,5
print(list1[list1.index(3):list1.index(5)+1])

# 4.5:通过冒号索引取0到5
print(list1[list1.index(0):list1.index(5)+1])

# 4.6:通过冒号索引取3到11
print(list1[list1.index(3):list1.index(11)+1])

# 4.7:通过冒号索引取列表中的数字3和5
print(list1[3:6:2])

# 4.8:通过冒号索引取列表的数字3,5,7,9,11
print(list1[3:12:2])
