from managers.bookManager import BookManager

# Stack's recursive method
def totalValue(author, books = BookManager.booksByDate):
    '''
    Calculate the sum of the prices of all the books written by the given author
    Args:
        author(str): Author's name
        books(list): List of books in which to look for. All the books's list by default
    Returns:
        float: Total price of books
    '''
    # Base case: there's one last remaining element
    if len(books) == 0:
        return 0
    
    # Recursive call
    if books[0].author == author:
        return books[0].price + BookManager.totalValue(author, books[1:])
    return BookManager.totalValue(author, books[1:])

# Tail's recursive method
@classmethod
def meanWeight(author, index=0, total_weight=0, count=0):
    '''
    Calculate the average of the weights in a list of books of a given author
    Args:
        author(str): Author's name
        index(int): Current book's index in the list. Zero by default
        total_weight(float): Current total weight of the books that fulfill the criteria. Zero by default
        count(int): Current number of books that fullfill the criteria. Zero by default
    Returns:
        float: Average weight of books
    '''

    print(f"Recursive call: index={index}, total_weight={total_weight}, count={count}")

    # Base case: Booklist finished
    if index == len(BookManager.booksByDate):
        if count == 0:
            return 0  # There's no books of this author
        return total_weight / count

    # If there are books of the author, add them
    if BookManager.booksByDate[index].author == author:
        new_total = total_weight + BookManager.booksByDate[index].weight
        new_count = count + 1
    else:
        new_total = total_weight
        new_count = count

    # Next recursive call
    return BookManager.meanWeight(
        author,
        index + 1,
        new_total,
        new_count
    )