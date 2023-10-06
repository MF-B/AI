# 1--控制语句

# 1.1:for循环输出字符串
data_string = ["C", "C++", "Java", "Python"]
for i in data_string:
    print(i)

# 1.2:for循环输出1到9
for i in range(1, 10):
    print(i)

# 1.3:while求100以内整数和
count = 100
num_sum = 0
while count:
    num_sum += count
    count = count - 1
print(num_sum)

# 1.4:使用判断语句判断人的年龄阶段
age = int(input("请输入年龄:"))
if 0 < age <= 14:
    print("少年儿童")
elif 14 < age <= 35:
    print("青年人")
elif 35 < age <= 65:
    print("中年人")
elif 65 < age:
    print("老年人")
else:
    print("年龄输入错误！")
