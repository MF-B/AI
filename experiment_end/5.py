#函数的定义和使用
from L05FuncDef import is_float
num = input('请输入:')
res = is_float(num)
print(res)



dic = {}
a = input("请输入一个学生的(姓名,成绩)：")
d = 0
with open("date.txt","w") as fp:
    while True:
        fp.write(a + '\n')
        d+=1
        n=input('是否继续：y/n')
        if n=='n':
            break
        a= input("请输入一个学生的姓名和成绩：")
c=input("请输入学生姓名：")
with open("date.txt",'r') as fp:
    for i in fp.readlines():
        a,b  = i.split(",")
        dic[a] = b
if c in dic.keys():
    print(c+',',dic[c])
else:print("没找到")

