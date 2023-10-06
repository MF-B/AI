# 1.1
# for语句
string = ["C", "C++", "Java", "Python"]
for x in string:
    print(x)

for i in range(1, 10):
    print(i)

# while语句
sum = 0
count = 0
while count <= 100:
    sum += count
    count += 1
    print(sum)

# if..elif..else语句
age = int(input("Please your age>>:"))
if 0 < age and age <= 20:
    print("teenager")
elif 20 < age and age <= 40:
    print("Man")
elif 40 < age and age <= 60:
    print("older")
else:
    print("older")
