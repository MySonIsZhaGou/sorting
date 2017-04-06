#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#以下是错误的
from numpy import random
array=random.randint(0,100,10)
print array
def quickSort(array):
    if len(array) < 1:
        return array
    emptyStack=[]
    key=array[0]
    left=[]
    right=[]
    for j in range(1,len(array)): #问题就在于，for循环是从0开始的，或者说我在判断时，没有考虑array[0]这种情况，也就是说，array[0]在这里
                                  #每次都会加进left里，这样的话，left每递归一次，都会额外加进一个数，最后是不可能
                                  # 长度小于1的，也就是不会结束，这就是为什么报错报的是递归超过最大数量
                                  # 解决方法：1)在len(array)前加个1，去掉array[0]  2)参见方法二
        if array[j] > key :
            right.append(array[j])
        else:
            left.append(array[j])
    left = quickSort(left)
    right = quickSort(right)
    emptyStack = left + [key]+ right
    return emptyStack
print quickSort(array)

#方法二
'''from numpy import random
array=random.randint(0,100,10)
print array
def quickSort(array):
    if len(array) < 1:
        return array
    #emptyStack=[] 这个空list有没有都无所谓
    key=array[0]
    left=[]
    right=[]
    for j in array[1:]:
        if j > key:
            right.append(j)
        else:
            left.append(j)
    left = quickSort(left)
    right = quickSort(right)
    emptyStack = left + [key]+ right  #这边的key一定要加个[]
    return emptyStack
print quickSort(array)'''

