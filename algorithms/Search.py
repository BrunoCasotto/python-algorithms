from math import ceil

# function to search an target into the list using linear method
def basic_linear_search(list, target):
    result = -1
    for index, item in enumerate(list):
        if item == target:
            result = index

    return result

# function to search an target into the list using perfomatic linear method
def perf_linear_search(list, target):
    for index, item in enumerate(list):
        if item == target:
            return index

    return -1

# binary search
def recursive_binary_search(list, target):
    total = len(list)
    middle = ceil(total/2)
    if len(list) == 1:
        if list[0] == target:
            return target
        else:
            return -1


    if list[middle] == target:
        return middle

    if list[middle] > target:
        return recursive_binary_search(list[0:middle], target)

    return recursive_binary_search(list[middle:total], target)