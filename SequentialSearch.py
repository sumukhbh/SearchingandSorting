# Implementation of Sequential Search #

def seq_search(array, target):
    found = False
    for element in array:
        if element == target:
            found = True
    return found

print(seq_search([1,3,45,100],100))
print(seq_search([32,45,3,4],105))
print(seq_search([1,3,2,5],1))
