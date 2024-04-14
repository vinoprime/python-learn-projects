print("Hello")

# [3,5,-4,8,11,1,-1,6], 10


ary = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 11

def call():
    # O(n^2) time /O(1) space
    for i in range(len(ary)):
        firstNum = ary[i]
        for j in range(i+1, len(ary)):
            secondNum = ary[j]
            if firstNum+secondNum == targetSum:
                return [firstNum, secondNum]


def usingHash():
    # O(n) / O(n) space
    nums = {}
    for num in ary:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
        else:
            nums[num] = True
    return []


def usingPtr():
    # O(nlog(n)) | O(1) space
    x = sorted(ary)
    left = 0
    right = len(x)-1
    while left < right:
        currentSum = x[left]+x[right]
        if currentSum == targetSum:
            return [x[left], x[right]]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1

    return []


z = usingPtr()
print(z)
