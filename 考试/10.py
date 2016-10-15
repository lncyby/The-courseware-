#!/usr/bin/python 

class List():

    a = [2,1,8,3,5,7,4,6]


    def bubble(l):
        for i in range(len(l)):
            for j in range(len(l)-i-1):
                if l[j] > l[j + 1]:
                    l[j],l[j + 1] = l[j + 1],l[j]

        print l
    
    bubble(a)
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

            guick_sort(array,low,key - 1)
            quick_sort(array,key + 1,high)


list = List()

list.bubble()




        
