#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from numpy import random
Array=random.randint(0,100,10)
Array=list(Array)
print Array

def merge(left,right):
    l,r=0,0
    emptyStack=[]
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            emptyStack.append(left[l])
            l += 1
        else:
            emptyStack.append(right[r])
            r += 1
    emptyStack.extend(left[l:])#这里千万不要用append，append是打包添加到列表中，即后面的list不管有多少内容，都会作为一个整体list加进去，
                               # 而extend是合并，不会作为整体加入，注意区别
    emptyStack.extend(right[r:])
    return emptyStack

def mergeSort(Array):
    if len(Array) <= 1:
        return Array            #一定要注意有这个if，否则就错了，没有返回值了
    num=int(len(Array)/2)
    left=mergeSort(Array[:num])
    right=mergeSort(Array[num:])
    return merge(left,right)

print mergeSort(Array)



