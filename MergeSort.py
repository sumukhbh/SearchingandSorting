# Implementation of Merge Sort #

def merge_sort(array):

    if len(array) > 1:
        mid_value = len(array)//2
        # split the array into left and right halves #
        left_half = array[:mid_value]
        right_half = array[mid_value:]

        # make recursive calls on the left and right halves #
        merge_sort(left_half)
        merge_sort(right_half)

        i=0
        j=0
        k=0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1


        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1
    return array

print(merge_sort([3,100,1,20,6,5]))
print(merge_sort([11,2,5,4,7,6,1,8,19,3]))
            
     
