# 1. COUNTDOWN
def countdown(num):
    vals = []
    for i in range(num, 0-1, -1):
        vals.append(i)
    return vals
print(countdown(5))

# 2. PRINT AND RETURN
def printAndReturn(arr):
    print(arr[0])
    return arr[1]
y = printAndReturn([1,2])
print(y)

# 3. FIRST PLUS LENGTH
def firstPlusLength(arr):
    return arr[0] + arr[len(arr)-1]
print(firstPlusLength([1,2,3,4,2]))

# 4. VALUES GREATER THAN SECOND
def greaterThanSecond(arr):
    newVals = []
    for i in range(len(arr)):
        if arr[i]>arr[1]:
            newVals.append(arr[i])
    return newVals
print(greaterThanSecond([5,2,3,2,1,4]))

# 5. THIS LENGTH, THAT VALUE
def lengthVal(length, value):
    vals = []
    for i in range(0, length):
        vals.append(value)
    return vals
print(lengthVal(6,2))