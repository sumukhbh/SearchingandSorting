# Implementation of Selection Sort #

def selection_sort(array):
    for i in range(len(array)-1, 0, -1):
        max_pos = 0
        for j in range(1,i+1):
            if array[j] > array[max_pos]:
                max_pos = j

        array[i],array[max_pos] = array[max_pos],array[i] 
    return array

print(selection_sort([5,2,15,25,1]))
print(selection_sort([100,1,200,1000,3]))
