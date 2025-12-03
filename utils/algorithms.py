def insertionSort(array, key):
    '''
    Sort an arraylist according to the key using the Insertion Sort algorithm
    Args:
        array(list): List to be sorted
        key(lambda function): Sorting criteria. It must return the property used as criteria
    Returns:
        list: Sorted list
    '''
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

def mergeSort(array, key):
    '''
    Sort an arraylist according to the key using the Merge Sort algorithm
    Args:
        array(list): List to be sorted
        key(lambda function): Sorting criteria. It must return the property used as criteria
    Returns:
        list: Sorted list
    '''
    # Base case: ordered list of one element
    if len(array) == 1:
        return array
    # Recursive calling for both halves (Divide)
    mid = len(array) // 2
    left = mergeSort(array[:mid], key)
    right = mergeSort(array[mid:], key)
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

def linealSearch(array, target, key):
    '''
    Look for an element in a sorted/unsorted list and returns all the ocurrences in the list
    Args:
        array(list): List in which the element is searched
        target(object): Atribute to look for in the elements of the list
        key(lambda function): Searching criteria. It must return the property used as criteria
    Returns:
        list: List with all the element that fulfill the criteria. Returns [] if the element wasn't found
    '''
    # Lineal search function to look for ALL the target's ocurrences in the list
    if len(array) > 0: 
        if key(array[0]) == target:
            return [array[0]] + linealSearch(array[1:], target, key)
        return linealSearch(array[1:], target, key)
    else:
        return []

def binarySearch(array:list, target, key):
    '''
    Look for an element in a sorted list of unique elements and returns the unique ocurrence
    Args:
        array(list): List in which the element is searched
        target(object): Atribute to look for in the elements of the list
        key(lambda function): Searching criteria. It must return the property used as criteria
    Returns:
        object: Element found in the list that fulfill the criteria. None if the element wasn't found
    '''
    # Binary search looks for the UNIQUE target's ocurrences in the list
    if len(array) == 1:
        # If the target is the remaining element, returns it, else returns None
        if key(array[0]) == target:
            return array[0]
        else:
            return None
    # Recursive calling to look for in the half that could contain the element
    mid = len(array) // 2
    if target < key(array[mid]):
        return binarySearch(array[:mid], target, key)
    else:
        return binarySearch(array[mid:], target, key)

# Stack's recursive method
def recursiveAddition(array, key):
    '''
    Calculate the sum of the atributtes of elements in a list
    Args:
        array(list): List of elements whose atributtes must be summed
        key(lambda function): Summing criteria. It must return the property used as criteria
    Returns:
        float: Total sum
    '''
    # Base case: there's no remaining elements
    if len(array) == 0:
        return 0
    
    # Recursive call
    return key(array[0]) + recursiveAddition(array[1:])

# Tail's recursive method
def recursiveMean(array, key, index=0, total=0, count=0):
    '''
    Calculate the average of the atributtes of elements in a list
    Args:
        array(list): List of elements whose atributtes must be averaged
        key(lambda function): Summing criteria. It must return the property used as criteria
        index(int): Current element's index in the list. Zero by default
        total(float): Current total value of the atribute of the books. Zero by default
        count(int): Current number of elementes. Zero by default
    Returns:
        float: Average weight of books
    '''

    print(f"Recursive call: index={index}, total={total}, count={count}")

    # Base case: there's one last remaining element
    if index == len(array):
        if count == 0:
            return 0  # There's no elements in the original list
        return total / count
    
    # Next recursive call with next element
    return recursiveMean(
        array,
        key,
        index + 1,
        total + key(array[index]),
        count + 1
    )