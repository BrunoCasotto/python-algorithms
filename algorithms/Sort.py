
# basic sort select using min var to store the current min index and replace the current list index instead
def select_sort(list):
    listLength = len(list)

    for i in range(listLength):

        minIndex = i
        for j in range(i + 1, listLength):
            if list[minIndex] > list[j]:
                minIndex = j

        list[i], list[minIndex] = list[minIndex], list[i]

    return list
