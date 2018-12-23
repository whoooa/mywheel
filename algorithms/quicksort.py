# coding:utf-8
from __future__ import unicode_literals

# 名称：快速排序(quicksort)
# 通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
# 然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。

# 最好：nlog(n)
# 平均：nlog(n)
# 最差：n²



def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        smaller_a = [ele for ele in array[1:] if ele <= pivot]
        greater_a = [ele for ele in array[1:] if ele > pivot]
        return quick_sort(smaller_a) + [pivot] + quick_sort(greater_a)


if __name__ == "__main__":
    test_array = [5, 6, 9, 3, 4, 6]
    print test_array
    print quick_sort(test_array)
