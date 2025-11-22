def insertionSort(array:list,key:callable)->list:
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if key(array[j]) < key(array[j-1]):
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break
    return array

def linealSearch(array:list, target, key:callable):
    if len(array) > 0: 
        if key(array[0]) == target: return [array[0]]+linealSearch(array[1:], target, key)
        return linealSearch(array[1:], target, key)
    else : return []

def binarySearch(array:list, target, key:callable):
    if len(array) == 1 and key(array[0]) == target: return array[0]
    if target in [key(i) for i in array[:len(array)//2]]: return binarySearch(array[:len(array)//2])
    else: return binarySearch(array[len(array)//2:])
