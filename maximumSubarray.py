from math import floor


def FindMaxCrossingSubarray(A, low, mid, high):
    leftSum = float("-inf")
    sum = 0
    for i in range(mid, low-1, -1):
        sum += A[i]
        if sum > leftSum:
            leftSum = sum
            maxLeft = i
    rightSum = float("-inf")
    sum = 0
    for j in range(mid+1, high+1, 1):
        sum += A[j]
        if sum > rightSum:
            rightSum = sum
            maxRight = j
    return [maxLeft, maxRight, leftSum + rightSum]


def FindMaximumSubarray(A, low, high):
    if high == low:
        return [low, high, A[low]]
    else:
        mid = floor((low+high)/2)

        temp = FindMaximumSubarray(A, low, mid)
        leftLow = temp[0]
        leftHigh = temp[1]
        leftSum = temp[2]
        temp = FindMaximumSubarray(A, mid+1, high)
        rightLow = temp[0]
        rightHigh = temp[1]
        rightSum = temp[2]
        temp = FindMaxCrossingSubarray(A, low, mid, high)
        crossLow = temp[0]
        crossHigh = temp[1]
        crossSum = temp[2]

        if leftSum >= rightSum and leftSum >= crossSum:
            return [leftLow, leftHigh, leftSum]
        elif rightSum >= leftSum and rightSum >= crossSum:
            return [rightLow, rightHigh, rightSum]
        else:
            return [crossLow, crossHigh, crossSum]


A = [1, 4, -5, -18, 68, -2, -
     5, -17, 29, 13, -29, 4, 2, -5, 7, -3, 6, 21, 6]
print(FindMaximumSubarray(A, 1, A.__len__() - 1))
