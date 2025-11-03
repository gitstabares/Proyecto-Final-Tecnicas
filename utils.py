def insertionSort(array:list,key:callable)->list:
    for i in range(1, len(array)):
        actual = array[i]
        j = i - 1
        while j >= 0 and key(actual) < key(array[j]):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = actual
    return array