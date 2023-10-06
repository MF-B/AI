# 访问列表中的值
list1 = ['physics', 'chemistry', 1997, 2000]
print("list1[0]:", list1[0])
list2 = [1, 2, 3, 4, 5, 6, 7]
print("list2[1:5]:", list2[1:5])

# 更新列表
list = []  # 空列表
list.append('Google')  # 使用append()添加元素
list.append("ChatGpt")
print(list)
list[1] = "Baidu"
print(list)

# 删除列表元素
list1 = ['physics', 'chemistry', 1997, 2000]
print(list1)
del list1[2]
print(list1)

# 其他操作
print(len([1, 2, 3]))
print([1, 2, 3] + [4, 5, 6])
print(['Hi'] * 4)
print(3 in [1, 2, 3])
for x in [1, 2, 3]:
    print(x)
