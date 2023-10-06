# 5-函数的定义与使用

# 5.1:实现一个判断字符串是否为浮点数的函数
def is_float(str_1):
    str_1 = str(str_1)
    if str_1.count('.') == 1:
        left = str_1.split('.')[0]
        right = str_1.split('.')[1]
        if left.isdigit() & right.isdigit():
            return True
        elif left.startswith('-') & left.count('-') == 1 \
                & left.split('-')[1].isdigit() & right.isdigit():
            return True
        else:
            return False
    else:
        return False


# 5.2:实现一个根据学生姓名查询学生信息的函数
students = {"张三": {"年龄": 18, "性别": "男"}}


def search_stu(name):
    name = str(name)
    if name in students:
        return students["张三"]
    else:
        return "查无此人"


# 调用测试
# 5.1
str1 = str(input('输入要判断的数字:'))
if is_float(str1):
    print("此数是浮点数")
else:
    print("此数不是浮点数")

# 5.2
stu = str(input("请输入学生姓名"))
print(search_stu(stu))
