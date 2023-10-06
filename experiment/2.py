# 2--列表

# 2.1:构造四个元素的列表，并显示第一个元素
list_1 = ['physics', 'chemistry', 1997, 2000]
print("list_1[0] = ", list_1[0])

# 2.2:构造数字1到7的列表,显示数字2到5
list_2 = []
for i in range(1, 8):
    list_2.append(i)
print(list_2[1:5])

# 2.3:append添加字符串&替换元素
list_3 = []
list_3.append('Google')
list_3.append('ChatGPT')
list_3[1] = 'Baidu'

# 2.4:构造有四个元素的列表.并删除其中一个元素
list_4 = ['physics', 'chemistry', 1997, 2000]
list_4.pop(3)

# 2.5:显示列表长度,将2个列表连接为1个列表。生成一个由四个字符串组成的列表,判断元素是否在列表中,显示列表的每一个元素
list_5 = [1, 2, 3]
list_6 = [4, 5, 6]
list_7 = ['Hi']*4
print(len(list_5))  # 用len函数求list的尺寸
print(list_5+list_6)  # 合并2个列表
print(list_7)
print(3 in list_5)  # 使用in判断元素是否在列表中
print(*list_5)  # 默认用空格分隔
