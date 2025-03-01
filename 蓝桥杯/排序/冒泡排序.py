'''给定一个整数数组，通过对数组进行冒泡排序，将数组分为两部分，使得两部分元素和的差值最大，
求这个最大差值。例如，给定数组 [3, 1, 2, 4]，排序后为 [1, 2, 3, 4]，前半部分 [1, 2] 元素
和为 3，后半部分 [3, 4] 元素和为 7，差值为 4'''
#冒泡排序是直接在数组上面操作

def bubble_sort(arr):#首先定义函数bubble_sort用来将数组排序，每一轮循环确定一个大值位置
    n = len (arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j] >arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def max_difference(arr):
    sorted_arr = bubble_sort(arr)#引用上述函数，让代码可读性更强
    n= len(sorted_arr)
    sum_front = sum(sorted_arr[:n//2])#这两个下标是一样的，所以必然二分，如果他数组为奇数就会有点难办，
    sum_back = sum(sorted_arr[n//2:])
    return sum_back - sum_front

arr = [3,1,2,4]
print(bubble_sort(arr))
print(max_difference(arr))

#现在输出的是最大值和最小值的差