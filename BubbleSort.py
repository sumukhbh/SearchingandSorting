# Implementation of Bubble Sort #

def bubble_sort(array):
    for i in range(len(array)-1, 0, -1):
       #print("The value of i is : ", i)
       for j in range(i):
            # if the current element is greater than the adjacent element #
           if array[j] > array[j+1]:
               (array[j],array[j+1]) = (array[j+1],array[j])
    return array

print(bubble_sort([1,19,3,4,20]))
print(bubble_sort([1,19,400,20,3,2,5,100,200]))
