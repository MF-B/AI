import numpy as np#导入模块
first_list=[1,2,3,4,5]#创建一个python列表
first_array = np.array(first_list)#转换为一维数组
first_list1=first_array.tolist
print(first_array)
print(first_list1)


second_list=[[1,2,3],[5,4,1],[3,6,7]]#创建一个元素为列表的python列表
second_array=np.array(second_list)#转换为二维数组
second_list1=second_array.tolist()
print(second_array)
print(second_list1)