print("sorted_squared_array")


def solution_1(main_array):
    # Time = O(nLogn)
    # Space = O(n)

    sortedSquares = [0 for _ in main_array]
    print(sortedSquares)

    for idx in range(len(main_array)):
        value = main_array[idx]
        sortedSquares[idx] = value * value

    print(sortedSquares)
    sortedSquares.sort()
    return sortedSquares


def solution_2(main_array):

    sortedSquares = [0 for _ in main_array]
    print(sortedSquares)
    smallValueIdx = 0
    largerValueIdx = len(main_array) - 1
    print(largerValueIdx)

    for idx in reversed(range(len(main_array))):
        smallValueIdx = main_array[smallValueIdx]
        largerValueIdx = main_array[largerValueIdx]

        if abs(smallValueIdx) > abs(largerValueIdx):
            sortedSquares[idx] = smallValueIdx * smallValueIdx
            smallValueIdx += 1
        else:
            sortedSquares[idx] = largerValueIdx * largerValueIdx
            largerValueIdx -= 1

    return sortedSquares


main_array = [1, 3, 2, 5, 6, 8, 9]
result = solution_2(main_array)
print(result)

# print(result)
