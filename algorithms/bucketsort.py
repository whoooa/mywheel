# coding:utf-8
from __future__ import unicode_literals

# 名称：桶排序
#如果有一个数组A，包含N个整数，值从1到M，我们可以得到一种非常快速的排序，桶排序（bucket sort）。留置一个数组S，里面含有M个桶，初始化为0。然后遍历数组A，读入Ai时，S[Ai]增一。所有输入被读进后，扫描数组S得出排好序的表。该算法时间花费O(M+N)，空间上不能原地排序。

#最好 O(n);
#平均 O(n)
#最坏 O(n)

def bucket_sort(array):

    max_num = max(array)
    bucket_init = [0 for i in range(max_num+1)]
    for i in array:
        bucket_init[i] += 1

    sortd_array = []
    for i, v in enumerate(bucket_init):
        for j in range(v):
            sortd_array.append(i)

    return sortd_array

if __name__ == "__main__":
    test_a = [1, 3, 4, 5, 2, 2, 8,6, 6, 10]
    sorted_array = bucket_sort(test_a)
    print sorted_array
