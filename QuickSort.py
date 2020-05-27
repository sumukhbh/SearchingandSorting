# Implementation of Quick Sort #

def quick_sort(array):
    sort_helper(array,0,len(array)-1)
    return array

def sort_helper(array,first,last):
    if first < last:
        split = partition(array,first,last)

        sort_helper(array,first,split-1)
        sort_helper(array,split+1,last)


def partition(array,first,last):
    pivot_element = array[first]

    left = first + 1
    right = last

    done = False

    while done != True:

        while left <= right and array[left] <= pivot_element:
            left += 1

        while right >= left and array[right] >= pivot_element:
            right -= 1

        if right < left:
            done = True
        else:
            array[left],array[right] = array[right],array[left]

    array[first], array[right] = array[right],array[first]

    return right
    
print(quick_sort([2,5,4,6,7,3,1,4,12,11]))
print(quick_sort([4,3,7,19,1]))

