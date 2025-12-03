from .singleton import _Singleton

class Bookshelf(_Singleton):

    # Brute force method to look for the worst books combination
    @classmethod
    def poorBookshelf(cls, books, maxWeight = 8):
        n = len(books)
        combination = []
        # If there's less than 4 books, so there's no combination that fullfill the conditions
        if n < 4:
            return combination

        # Look for all the combinations (No considering the order)
        for i in range(0, n-3):
            for j in range(i+1, n-2):
                for k in range(j+1, n-1):
                    for l in range(k+1, n):
                        totalWeight = (books[i].weight +
                                    books[j].weight +
                                    books[k].weight +
                                    books[l].weight)
                        if totalWeight > maxWeight:
                            combination.append((books[i], books[j], books[k], books[l]))
        return combination
    
    # Backtracking algorithm to look for the optimal book combination (Knapsack algorithm)
    @classmethod
    def optimalBookshelf(cls, books, maxWeight = 8):
        bestValue = 0
        bestCombination = []

        def backtrack(index, actualWeight, actualPrice, actualCombination):
            nonlocal bestValue, bestCombination

            # Base case: all the books have been evaluated
            if index == len(books):
                if actualPrice > bestValue:
                    bestValue = actualPrice
                    bestCombination = actualCombination.copy()
                return

            actualBook = books[index]

            # First case: Evaluate the actual book (If it doesn't break the weight rule)
            if actualWeight + actualBook.weight <= maxWeight:
                actualCombination.append(actualBook)
                backtrack(
                    index + 1,
                    actualWeight + actualBook.weight,
                    actualPrice + actualBook.price,
                    actualCombination
                )
                actualCombination.pop()  # Backtracking: Remove the element to evaluate the second case

            # Second case: Do not evaluate the actual book
            backtrack(
                index + 1,
                actualWeight,
                actualPrice,
                actualCombination
            )

        # First call
        backtrack(0, 0, 0, [])
        return bestValue, bestCombination