def insertionSort(array:list,key:callable)->list:
    for i in range(1, len(array)):
        actual = array[i]
        j = i - 1
        while j >= 0 and key(actual) < key(array[j]):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = actual
    return array

def linealSearch(array:list, target, key:callable):
    if key(list[0]) == target: return list[0]
    return linealSearch(array[1:], target, key)

def binarySearch(array:list, target, key:callable):
    if len(array) == 1 and key(array[0]) == target: return array[0]
    if target in [key(i) for i in array[:len(array)//2]]: return binarySearch(array[:len(array)//2])
    else: return binarySearch(array[len(array)//2:])
