test_list=[6,2,7,4,12,13,99]

# 冒泡排序

for i in range(len(test_list)-1):
    for j in range(len(test_list)-1):
        if test_list[j] > test_list[j+1]:
            test_list[j],test_list[j+1]=test_list[j+1],test_list[j]

# 创建排序函数（返回一个新列表)
def sort(a):
    result=[]
    while True:
        result.append(min(a))
        a.remove(min(a))
        if len(a)==0:
            return result
            break
