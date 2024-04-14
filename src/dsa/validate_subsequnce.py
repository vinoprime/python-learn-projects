print("Validate_subsequence")


def solution_1(main_array, sub):
    # Time = O(n)
    # Space = O(1)
    mainIdx = 0
    seqIdx = 0
    while mainIdx < len(main_array) and seqIdx < len(sub):
        if main_array[mainIdx] == sub[seqIdx]:
            seqIdx += 1
        mainIdx += 1

    return seqIdx == len(sub)


def solution_2(main_array, sub):
    # Time = O(n)
    # Space = O(1)
    seqIdx = 0
    for value in main_array:
        if seqIdx == len(sub):
            break
        if sub[seqIdx] == value:
            seqIdx += 1

    return seqIdx == len(sub)


main_array = [5, 1, 22, 25, 6, -1, 8, 10]
sub_sequence_array = [1, 6, -1, 10]
result = solution_1(main_array, sub_sequence_array)
print(result)
result = solution_2(main_array, sub_sequence_array)
print(result)
