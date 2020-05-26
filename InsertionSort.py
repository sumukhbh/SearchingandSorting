# Implementation of Insertion Sort #

def insertion_sort(array):
    for i in range(1,len(array)):
        position = i
        curr_value = array[i]

        while position > 0 and array[position-1] > curr_value:
            #print(position)
            #print(curr_value)
            array[position] = array[position-1]
            position = position -1

        array[position] = curr_value
    return array

print(insertion_sort([6,2,100,1,40]))
print(insertion_sort([100,2,300,5,10]))
            
        
