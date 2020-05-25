# Implementation of Binary Search #

# Returns the index of the element if it's found else return -1 #

def binary_search(array,target):
    low = 0
    high = len(array)-1


    while low <= high:
        mid = (low+high)//2
        if array[mid] == target:
            return mid
        else:
            if array[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
    return -1

print(binary_search([1,2,3,4,5,6,7,8,9,10],10))
print(binary_search([18,19,20,22,45,78],-2))
print(binary_search([100,200,300,400], 500))
