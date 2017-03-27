#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#以上的这两行一定要加在代码开头，加在其他任何地方都不行
'''
wrong version[1]:

from numpy import random
array=random.randint(0,100,10)
print array
def insert(array):
    for i in range(1,len(array)):
        extract_element=array[i]
        for j in range(i)[::-1]:
            if array[j]>extract_element:
                #array[j],array[i],extract_element= extract_element,array[j],array[j]
                array[j],extract_element=extract_element,array[j]
            array[i]=array[j]
    return array
print insert(array)'''

'''
wrong version[2]:

from numpy import random
array=random.randint(0,100,10)
print array
def insert(array):
    for i in range(1, len(array)):
        extract_element = array[i]
        for j in range(i)[::-1]:
            if array[j] > extract_element:
                array[j+1] = array[j]
                array[j] = extract_element
            else: array[j+1] = extract_element
    return array
print insert(array)'''

# mine version:
from numpy import random
array=random.randint(0,100,10)
print array
def insert(array):
    for i in range(1, len(array)):
        extract_element = array[i]
        for j in range(i)[::-1]:
            if array[j] > extract_element:
                array[j+1] = array[j]
                array[j] = extract_element
            else: break
    return array
print insert(array)

# my son's version:
from numpy import random
array=random.randint(0,100,10)
print array
def insert(array):
    for i in range(1,len(array)):
        extract_element=array[i]
        for j in range(i)[::-1]:#两个冒号是逆序，-1代表倒数第二个数
            #if array[j]>extract_element:
            #错误为：交换了extract这个临时变量，而不是交换数组中的元素
            if array[j] > array[j+1]:
                #array[j],array[i],extract_element= extract_element,array[j],array[j]
                array[j],array[j+1]=array[j+1],array[j]
            #array[i]=array[j]
    return array
print insert(array)

