from numpy import random
array=random.randint(0,100,10)
print array
def select(array):
    min_num=array[0]
    for i in range(len(array)):
        min_num = array[i]
        for j in range(len(array)-i):
            if array[j+i]<min_num:
                min_num=array[j+i]
                temp=j+i
        array[temp],array[i]=array[i],min_num
    return array
print select(array)