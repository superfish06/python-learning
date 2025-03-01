'''假设我们有一个待排序的数组 [5, 3, 4, 1, 2]，下面来逐步分析插入排序的过程。'''

#插入排序的实现是一个很有意思的事情，他新建了一个数组，然后再插入新数组，一般是先提取首个下标带入其他学科
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]#对key进行赋值，方便后面条件判断
        j = i - 1#这个j在此处较为关键
        while j >= 0 and key < arr[j]:#从小到大排序
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key
    return arr

arr = [5, 3, 4, 1, 2]
sorted_arr = insertion_sort(arr)
print(sorted_arr)
#for in的循环，对key赋值，while的变量来自range()