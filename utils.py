def insertionSort(array, key):
    # Loop towards for each element from second one
    for i in range(1,len(array)):
        # Loop backwards to compare each element with the ordered list
        for j in range(i,0,-1):
            if key(array[j-1]) > key(array[j]):
                array[j],array[j-1] = array[j-1],array[j]
            else:
                # If element has been sorted, then break its loop
                break
    return array

def merge_sort(array, key):
    # Base case: ordered list of one element
    if len(array) == 1:
        return array
    # Recursive calling for both halves (Divide)
    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    # Ordering of elements in merged list (Merge)
    i = j = 0
    while i < len(left) and j < len(right):
        if key(left[i]) < key(right[j]):
            array[i+j] = left[i]
            i+=1
        else:
            array[i+j] = right[j]
            j+=1
    # If one of the sides has finished, all the elements in the other one are greater
    if i == len(left):
        array[i+j:] = right[j:]
    if j == len(right):
        array[i+j:] = left[i:]

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
