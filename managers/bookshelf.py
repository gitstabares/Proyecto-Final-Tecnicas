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

        def backtrack(index, currentWeight, currentPrice, currentCombination):
            nonlocal bestValue, bestCombination

            # Base case: all the books have been evaluated
            if index == len(books):
                if currentPrice > bestValue:
                    bestValue = currentPrice
                    bestCombination = currentCombination.copy()
                return

            currentBook = books[index]

            print(f"Exploring the book in the index {index} of the list: {currentBook}\n",
                  f"The current combination is {currentCombination}, which weighs {currentWeight} ",
                  f"and it costs {currentPrice}")

            # First case: Evaluate the actual book (If it doesn't break the weight rule)
            if currentWeight + currentBook.weight <= maxWeight:
                currentCombination.append(currentBook)
                backtrack(
                    index + 1,
                    currentWeight + currentBook.weight,
                    currentPrice + currentBook.price,
                    currentCombination
                )
                currentCombination.pop()  # Backtracking: Remove the element to evaluate the second case

            # Second case: Do not evaluate the actual book
            backtrack(
                index + 1,
                currentWeight,
                currentPrice,
                currentCombination
            )

        # First call
        backtrack(0, 0, 0, [])
        return bestValue, bestCombination