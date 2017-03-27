from numpy import random
array=random.randint(0,100,10)
print array
def bubble(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array
print bubble(array)