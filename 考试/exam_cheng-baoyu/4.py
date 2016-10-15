#!/usr/bin/python

def sub_sort(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        array[low] = array[high]
        while low < high and array[low] < key:
            low += 1
        array[high] = array[low]
    array[low] = key
    return low

def quick_sort(array,low,high):
    if low < high:
         key = sub_sort(array,low,high)

         quick_sort(array,low,key - 1)
         quick_sort(array,key + 1,high)


list = [2,9,4,6,3,8,1,5]

quick_sort(list,0,len(list) - 1)
print(list)


