# Implementation of Counting Sort #

def counting_sort(array, max_range_value):
    output_array = [0] * (max_range_value +1)

    for val in array:
        output_array[val] += 1

    ans = [] 

    for i,value in enumerate(output_array):
        for j in range(value):
            ans.append(i)

    return ans

print(counting_sort([2,3,1,4,2,2,3,1,1],4))
print(counting_sort([8,3,1,2,4,9,2,2,2,1],9))
    
